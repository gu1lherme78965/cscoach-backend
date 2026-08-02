from demoparser2 import DemoParser
from pandas import DataFrame

from app.domain.enums.event_type import EventType
from app.domain.entities.player import Player

events_player_props_dict = {
    EventType.WEAPON_FIRE: ["X", "Y", "Z", "pitch", "yaw"],
    }
events_other_props_dict = {}

class CS2DemoParser:
    """
    Wrapper around demoparser2 that exposes
    CSCoach-friendly methods.
    """
    demo_path: str
    parser: DemoParser

    def __init__(self, demo_file_path: str):
        self.demo_path = demo_file_path
        self.parser = DemoParser(demo_file_path)

    def get_event_df_dict(self) -> dict[EventType, DataFrame]:
        event_df_dict = dict()
        for event_type in EventType:
            event_df_dict[event_type] = self.parser.parse_event(event_type.value, player=events_player_props_dict.get(event_type, None), other=events_other_props_dict.get(event_type, None))
        return event_df_dict

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
    
    def extract_player_list(self) -> list[Player]:
        players = []
        player_info  = self.get_player_info()

        for _, row in player_info.iterrows():
            name = row["name"]
            id = row["steamid"]
            team = row["team_number"]
            players.append(Player(id, name, team))

        return players
