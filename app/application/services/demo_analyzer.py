from app.domain.entities.match import Match
from app.infrastructure.demo_parser.parser import CS2DemoParser

class DemoAnalyzer:

    def __init__(self):
        pass

    def analyze(file_path: str) -> Match:
        parser = CS2DemoParser(file_path)

        match = Match()
        match.map_name = parser.get_header()["map_name"]
        # TODO populate EventTimeline, TickStore and list of Rounds
        return
    