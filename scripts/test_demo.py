from app.infrastructure.demo_parser.parser import CS2DemoParser

STEAMID = 76561198400981116

parser = CS2DemoParser("data/demos/test_demo.dem")

events = parser.get_all_events()
print(type(events))
for event_name, event_df in events:
    print(f"Event: {event_name}")
    if "user_steamid" in event_df.columns:
        print(event_df[event_df["user_steamid"] == str(STEAMID)])

ticks = parser.parse_ticks(["health", "X"])
print(ticks)

parser.print_self()
print(parser.get_header())