from app.infrastructure.demo_parser.parser import CS2DemoParser

parser = CS2DemoParser("data/demos/test_demo.dem")

players = parser.get_player_info()
grenades = parser.get_grenades()
event_list = parser.list_game_events()

print(players)
print(grenades)
print(event_list)

parser.print_self()