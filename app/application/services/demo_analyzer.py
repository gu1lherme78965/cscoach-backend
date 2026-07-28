from app.domain.entities.match import Match
from app.domain.entities.player import Player
from app.domain.entities.tick import Tick
from app.domain.timeline.tick_store import TickStore
from app.domain.timeline.event_timeline import EventTimeline
from app.domain.state.player_state import PlayerState
from app.domain.enums.maps import Map
from app.infrastructure.demo_parser.weapon_mapper import convert_weapon_name, get_unknown_weapons
from app.infrastructure.demo_parser.parser import CS2DemoParser
from app.domain.value_objects.steamid import SteamID
from app.domain.value_objects.position import Position
from app.domain.value_objects.velocity import Velocity
from app.domain.value_objects.view_angle import ViewAngle

unknown_maps = set()

class DemoAnalyzer:

    @staticmethod
    def analyze(file_path: str) -> Match:
        parser = CS2DemoParser(file_path)

        map = DemoAnalyzer.convert_map_name(parser.get_header()["map_name"])

        players = DemoAnalyzer.extract_player_list(parser)

        tick_store = DemoAnalyzer.build_tick_store(parser)

        event_timeline = DemoAnalyzer.build_event_timeline(parser)

        # TODO populate EventTimeline and list of Rounds
        unknown_weapons = get_unknown_weapons()
        if (unknown_weapons):
            print(f"Encountered unknown weapons in this game: {unknown_weapons}")
        if (unknown_maps):
            print(f"Encountered unknown maps in this game: {unknown_maps}")

        return Match(map, [], players, None, tick_store)
    
    @staticmethod
    def extract_player_list(parser: CS2DemoParser) -> list[Player]:
        players = []
        player_info  = parser.get_player_info()

        for _, row in player_info.iterrows():
            name = row["name"]
            id = row["steamid"]
            team = row["team_number"]
            players.append(Player(id, name, team))

        return players

    @staticmethod
    def convert_map_name(name: str) -> Map:
        match name:
            case "de_mirage":
                return Map.MIRAGE
            case _:
                if type(name) == str:
                    unknown_maps.add(name)
                return Map.UNKNOWN

    @staticmethod
    def build_tick_store(parser: CS2DemoParser) -> TickStore:
        tick_dict = {}
        ticks_df = parser.parse_ticks([
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

        for row in ticks_df.itertuples(index=False):
            tick = row.tick

            if tick not in tick_dict:
                tick_dict[tick] = Tick(tick, {})

            tick_dict[tick].player_states[row.steamid] = PlayerState(
                player_steamid=SteamID(row.steamid),
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

    @staticmethod
    def build_event_timeline(parser: CS2DemoParser) -> EventTimeline:
        pass