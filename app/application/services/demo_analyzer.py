from app.domain.entities.match import Match
from app.domain.entities.player import Player
from app.domain.enums.maps import Map
from app.infrastructure.demo_parser.parser import CS2DemoParser

class DemoAnalyzer:

    def __init__(self):
        pass

    @staticmethod
    def analyze(file_path: str) -> Match:
        parser = CS2DemoParser(file_path)

        match = Match()
        match.map = DemoAnalyzer.conver_map_name(parser.get_header()["map_name"])

        match.players = DemoAnalyzer.extract_player_list(parser)

        # TODO populate EventTimeline, TickStore and list of Rounds
        return
    
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
    def conver_map_name(name: str) -> Map | None:
        match name:
            case "de_mirage":
                return Map.MIRAGE
            case _:
                return None
            