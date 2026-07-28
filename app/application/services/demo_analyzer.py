from app.domain.entities.match import Match
from app.domain.entities.player import Player
from app.domain.timeline.tick_store import TickStore
from app.domain.enums.maps import Map
from app.infrastructure.demo_parser.parser import CS2DemoParser

class DemoAnalyzer:

    def __init__(self):
        pass

    @staticmethod
    def analyze(file_path: str) -> Match:
        parser = CS2DemoParser(file_path)

        map = DemoAnalyzer.convert_map_name(parser.get_header()["map_name"])

        players = DemoAnalyzer.extract_player_list(parser)

        tick_store = DemoAnalyzer.build_tick_store(parser)

        # TODO populate EventTimeline, TickStore and list of Rounds
        return Match(map, [], players, None, None)
    
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
                return Map.UNKNOWN

    @staticmethod
    def build_tick_store(parser: CS2DemoParser) -> TickStore:
        # TODO
        pass