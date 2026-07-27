from demoparser2 import DemoParser

class CS2DemoParser:
    """
    Wrapper around demoparser2 that exposes
    CSCoach-friendly methods.
    """

    def __init__(self, demo_file_path: str):
        self.demo_path = demo_file_path
        self.parser = DemoParser(demo_file_path)

    def get_all_events(self):
        return self.parser.parse_events(["all"])

    def get_player_info(self):
        return self.parser.parse_player_info()

    def get_grenades(self):
        return self.parser.parse_grenades()

    def list_game_events(self):
        return self.parser.list_game_events()

    def parse_specific_game_event(self, event_name: str):
        return self.parser.parse_event(event_name)

    def print_self(self):
        print(dir(self.parser))

    def parse_ticks(self, props):
        return self.parser.parse_ticks(props)