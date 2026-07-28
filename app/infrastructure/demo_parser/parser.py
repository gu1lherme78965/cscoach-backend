from demoparser2 import DemoParser
from app.domain.entities.match import Match
from app.domain.entities.player import Player
from app.domain.entities.tick import Tick
from app.domain.timeline.tick_store import TickStore
from app.domain.timeline.event_timeline import EventTimeline
from app.domain.state.player_state import PlayerState
from app.domain.enums.maps import Map
from app.domain.enums.body_part import BodyPart
from app.domain.enums.win_condition import WinCondition
from app.domain.enums.teams import Team
from app.domain.value_objects.steamid import SteamID
from app.domain.value_objects.position import Position
from app.domain.value_objects.velocity import Velocity
from app.domain.value_objects.view_angle import ViewAngle
from app.infrastructure.demo_parser.weapon_mapper import convert_weapon_name, get_unknown_weapons
from app.domain.events import (
    PlayerDeathEvent,
    PlayerHurtEvent,
    WeaponFireEvent,
    BeginNewMatchEvent,
    RoundStartEvent,
    RoundEndEvent,
)

unknown_maps = set()
unknown_teams = set()
unknown_locations = set()
unknown_win_conditions = set()
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
        if (unknown_locations):
            print(f"Encountered unknown locations in this game: {unknown_locations}")
        if (unknown_teams):
            print(f"Encountered unknown teams in this game: {unknown_teams}")
        if (unknown_win_conditions):
            print(f"Encountered unknown win conditions in this game: {unknown_win_conditions}")


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
                if type(name) == str and name:
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

    def convert_hit_location(self, location: str) -> BodyPart:
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
                if type(location) == str and location:
                    unknown_locations.add(location)
                return BodyPart.UNKNOWN

    def convert_win_condition(self, condition: str) -> WinCondition: 
        match condition:
            case "ct_killed":
                return WinCondition.CT_ELIMINATED
            case "t_killed":
                return WinCondition.T_ELIMINATED
            case "bomb_exploded":
                return WinCondition.BOMB_EXPLOSION
            case _:
                if type(condition) == str and condition:
                    unknown_win_conditions.add(condition)
                return WinCondition.UNKNOWN

    def convert_team(self, team: str) -> Team:
        match team:
            case "CT":
                return Team.COUNTER_TERRORIST
            case "T":
                return Team.TERRORIST
            case _:
                if type(team) == str and team:
                    unknown_teams.add(team)
                return Team.UNKNOWN

    def build_event_timeline(self) -> EventTimeline:
        start_tick = self.get_match_start_tick()
        events = list()

        events.extend(self.build_player_death_events(start_tick))
        events.extend(self.build_weapon_fire_events(start_tick))
        events.extend(self.build_player_hurt_events(start_tick))
        events.extend(self.build_begin_new_match_events(start_tick))
        events.extend(self.build_round_start_events(start_tick))
        events.extend(self.build_round_end_events(start_tick))

        events.sort(key=lambda e: e.tick)

    def build_player_death_events(self, start_tick: int) -> list[PlayerDeathEvent]:
        events = list()
        df = self.parser.parse_event("player_death")
        df = df[df["tick"] >= start_tick]

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

    def build_weapon_fire_events(self, start_tick: int) -> list[WeaponFireEvent]:
        events = list()
        df = self.parser.parse_event("weapon_fire", player=["X", "Y", "Z", "pitch", "yaw"])
        df = df[df["tick"] >= start_tick]

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

    def build_player_hurt_events(self, start_tick: int) -> list[PlayerHurtEvent]:
        events= list()
        df = self.parser.parse_event("player_hurt")
        df = df[df["tick"] >= start_tick]

        for row in df.itertuples(index=False):
            events.append(PlayerHurtEvent(
                tick=row.tick,
                attacker_id=row.attacker_steamid,
                victim_id=row.user_steamid,
                weapon=convert_weapon_name(row.weapon),
                hit_location=self.convert_hit_location(row.hitgroup),
                dmg_health=row.dmg_health,
                dmg_armor=row.dmg_armor,
                remaining_health=row.health,
                remaining_armor=row.armor
            ))
        return events

    def build_begin_new_match_events(self, start_tick: int) -> list[BeginNewMatchEvent]:
        events = list()
        df = self.parser.parse_event("begin_new_match")
        df = df[df["tick"] >= start_tick]

        for row in df.itertuples(index=False):
            events.append(BeginNewMatchEvent(
                tick=row.tick
            ))
        return events

    def build_round_start_events(self, start_tick: int) -> list[RoundStartEvent]:
        events = list()
        df = self.parser.parse_event("round_start")
        df = df[df["tick"] >= start_tick]

        for row in df.itertuples(index=False):
            events.append(RoundStartEvent(
                tick=row.tick,
                round_number=row.round
            ))
        return events

    def build_round_end_events(self, start_tick: int) -> list[RoundStartEvent]:
            events = list()
            df = self.parser.parse_event("round_end")
            df = df[df["tick"] >= start_tick]
    
            for row in df.itertuples(index=False):
                events.append(RoundEndEvent(
                    tick=row.tick,
                    round_number=row.round,
                    win_condition=self.convert_win_condition(row.reason),
                    winning_team=self.convert_team(row.winner)
                ))
            return events
        