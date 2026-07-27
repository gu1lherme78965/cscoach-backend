from app.infrastructure.demo_parser.parser import CS2DemoParser

from app.domain.entities.player import Player

STEAMID = 76561198400981116

parser = CS2DemoParser("data/demos/test_demo.dem")

events = parser.get_all_events()
print(type(events))
for event_name, event_df in events:
    print(f"Event: {event_name}")
    if "user_steamid" in event_df.columns:
        print(event_df[event_df["user_steamid"] == str(STEAMID)])

player_info  = parser.get_player_info()
print(player_info)
for index, row in player_info.iterrows():
    name = row["name"]
    id = row["steamid"]
    team = row["team_number"]
    print(Player(id, name, team))