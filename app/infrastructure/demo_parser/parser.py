from demoparser2 import DemoParser
from app.domain.entities.match import Match
from app.domain.entities.player import Player
from app.domain.entities.tick import Tick
from app.domain.timeline.tick_store import TickStore
from app.domain.timeline.event_timeline import EventTimeline
from app.domain.state.player_state import PlayerState
from app.domain.events.player_death_event import PlayerDeathEvent
from app.domain.events.weapon_fire_event import WeaponFireEvent
from app.domain.enums.maps import Map
from app.domain.enums.body_part import BodyPart
from app.domain.value_objects.steamid import SteamID
from app.domain.value_objects.position import Position
from app.domain.value_objects.velocity import Velocity
from app.domain.value_objects.view_angle import ViewAngle
from app.infrastructure.demo_parser.weapon_mapper import convert_weapon_name, get_unknown_weapons

unknown_maps = set()
steamid_cache = dict()

class CS2DemoParser:
    """
    Wrapper around demoparser2 that exposes
    CSCoach-friendly methods.
    """
    demo_path: str
    parser: DemoParser
    match: Match

    def __init__(self, demo_file_path: str):
        self.demo_path = demo_file_path
        self.parser = DemoParser(demo_file_path)
        self.match = self.parse

    def get_player_info(self):
        return self.parser.parse_player_info()

    def print_self(self):
        print(dir(self.parser))

    def parse_ticks(self, props: list):
        return self.parser.parse_ticks(props)

    def get_header(self):
        return self.parser.parse_header()

    def get_match_start_tick(self) -> int:
        events = self.parser.parse_events(["begin_new_match"])
        
        begin_new_match_df = next((df for event_name, df in events if event_name == 'begin_new_match'), None)
        return begin_new_match_df['tick'].iloc[0] if begin_new_match_df is not None else 0

    def parse(self) -> Match:

        map = self.convert_map_name(self.get_header()["map_name"])

        players = self.extract_player_list()

        #tick_store = self.build_tick_store()

        event_timeline = self.build_event_timeline()

        # TODO populate EventTimeline and list of Rounds
        unknown_weapons = get_unknown_weapons()
        if (unknown_weapons):
            print(f"Encountered unknown weapons in this game: {unknown_weapons}")
        if (unknown_maps):
            print(f"Encountered unknown maps in this game: {unknown_maps}")

        self.match = Match(map, [], players, None, None)
        return self.match
    
    def extract_player_list(self) -> list[Player]:
        players = []
        player_info  = self.get_player_info()

        for _, row in player_info.iterrows():
            name = row["name"]
            id = row["steamid"]
            team = row["team_number"]
            players.append(Player(id, name, team))

        return players

    def convert_map_name(self, name: str) -> Map:
        match name:
            case "de_mirage":
                return Map.MIRAGE
            case _:
                if type(name) == str:
                    unknown_maps.add(name)
                return Map.UNKNOWN

    def build_tick_store(self) -> TickStore:
        tick_dict = {}
        ticks_df = self.parse_ticks([
            "health",
            "armor_value",
            "is_alive",
            "X",
            "Y",
            "Z",
            "velocity_X",
            "velocity_Y",
            "velocity_Z",
            "pitch",
            "yaw",
            "is_scoped",
            "flash_duration",
            "active_weapon_name",
            "is_connected"
            ])
        ticks_df = ticks_df[ticks_df["tick"] >= self.get_match_start_tick()]

        for row in ticks_df.itertuples(index=False):
            tick = row.tick

            if tick not in tick_dict:
                tick_dict[tick] = Tick(tick, {})

            if row.steamid not in steamid_cache:
                steamid_cache[row.steamid] = SteamID(row.steamid)

            tick_dict[tick].player_states[row.steamid] = PlayerState(
                player_steamid=steamid_cache[row.steamid],
                position=Position(row.X, row.Y, row.Z),
                velocity=Velocity(row.velocity_X, row.velocity_Y, row.velocity_Z),
                view_angle=ViewAngle(row.yaw, row.pitch),
                health=row.health,
                armor=row.armor_value,
                active_weapon=convert_weapon_name(row.active_weapon_name),
                scoped=row.is_scoped,
                flashed=(row.flash_duration > 0),
                alive=row.is_alive
            )

        return TickStore(
            ticks=tick_dict
        )

    def convert_hit_location(self, location: str):
        match location:
            case "head":
                return BodyPart.HEAD
            case "chest":
                return BodyPart.CHEST
            case "right_arm":
                return BodyPart.RIGHT_ARM
            case "left_arm":
                return BodyPart.LEFT_ARM
            case "stomach":
                return BodyPart.STOMACH
            case "left_leg":
                return BodyPart.LEFT_LEG
            case "right_leg":
                return BodyPart.RIGHT_LEG
            case "generic":
                return BodyPart.UNKNOWN
            case _:
                print(f"hit location -> {location}")
                return BodyPart.UNKNOWN

    def build_event_timeline(self) -> EventTimeline:
        events = list()

        events.extend(self.build_player_death_events())
        events.extend(self.build_weapon_fire_events())

        events.sort(key=lambda e: e.tick)

    def build_player_death_events(self) -> list[PlayerDeathEvent]:
        events = list()
        df = self.parser.parse_event("player_death")

        for row in df.itertuples(index=False):
            events.append(PlayerDeathEvent(
                tick=row.tick,
                attacker_id=row.attacker_steamid,
                victim_id=row.user_steamid,
                assister_id=row.assister_steamid,
                weapon=convert_weapon_name(row.weapon),
                hit_location=self.convert_hit_location(row.hitgroup),
                distance=row.distance,
                dmg_health=row.dmg_health,
                dmg_armor=row.dmg_armor,
                attacker_in_air=row.attackerinair,
                is_noscope=row.noscope,
                is_penetrated=row.penetrated,
                is_through_smoke=row.thrusmoke
            ))
        return events

    def build_weapon_fire_events(self) -> list[WeaponFireEvent]:
        events = list()
        df = self.parser.parse_event("weapon_fire", player=["X", "Y", "Z", "pitch", "yaw"])

        for row in df.itertuples(index=False):
            events.append(WeaponFireEvent(
                tick=row.tick,
                user_id=row.user_steamid,
                weapon=convert_weapon_name(row.weapon),
                is_silenced=row.silenced,
                user_x=row.user_X,
                user_y=row.user_Y,
                user_z=row.user_Z,
                user_pitch=row.user_pitch,
                user_yaw=row.user_yaw
            ))
        return events
    