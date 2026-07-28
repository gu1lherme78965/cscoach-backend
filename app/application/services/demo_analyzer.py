from app.domain.entities.match import Match
from app.domain.entities.player import Player
from app.domain.entities.tick import Tick
from app.domain.timeline.tick_store import TickStore
from app.domain.state.player_state import PlayerState
from app.domain.enums.maps import Map
from app.domain.enums.weapons import Weapon
from app.infrastructure.demo_parser.parser import CS2DemoParser
from app.domain.value_objects.steamid import SteamID
from app.domain.value_objects.position import Position
from app.domain.value_objects.velocity import Velocity
from app.domain.value_objects.view_angle import ViewAngle

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
                return Map.UNKNOWN

    @staticmethod
    def convert_weapon_name(name: str) -> Weapon:
        match name:
            case "AK-47":
                return Weapon.AK_47
            case "AWP":
                return Weapon.AWP
            case "Bowie Knife":
                return Weapon.BOWIE_KNIFE
            case "C4 Explosive":
                return Weapon.C4_EXPLOSIVE
            case "CZ75-Auto":
                return Weapon.CZ75_AUTO
            case "Desert Eagle":
                return Weapon.DESERT_EAGLE
            case "Dual Berettas":
                return Weapon.DUAL_BERETTAS
            case "FAMAS":
                return Weapon.FAMAS
            case "Five-SeveN":
                return Weapon.FIVE_SEVEN
            case "Flashbang":
                return Weapon.FLASHBANG
            case "Galil AR":
                return Weapon.GALIL_AR
            case "Glock-18":
                return Weapon.GLOCK_18
            case "High Explosive Grenade":
                return Weapon.HE_GRENADE
            case "Incendiary Grenade":
                return Weapon.INCENDIARY_GRENADE
            case "knife" | "knife_t":
                return Weapon.KNIFE
            case "M4A1-S":
                return Weapon.M4A1_S
            case "M4A4":
                return Weapon.M4A4
            case "MAG-7":
                return Weapon.MAG_7
            case "MP5-SD":
                return Weapon.MP5_SD
            case "MP7":
                return Weapon.MP7
            case "MP9":
                return Weapon.MP9
            case "Molotov":
                return Weapon.MOLOTOV
            case "Nova":
                return Weapon.NOVA
            case "P250":
                return Weapon.P250
            case "P90":
                return Weapon.P90
            case "R8 Revolver":
                return Weapon.R8_REVOLVER
            case "Sawed-Off":
                return Weapon.SAWED_OFF
            case "SG 553":
                return Weapon.SG_553
            case "Smoke Grenade":
                return Weapon.SMOKE_GRENADE
            case "SSG 08":
                return Weapon.SSG_08
            case "USP-S":
                return Weapon.USP_S
            case "XM1014":
                return Weapon.XM1014
            case "Zeus x27":
                return Weapon.ZEUS_X27
            case _:
                if (name != "nan ") and (name!= "nan"): 
                    print(f"unknown weapon -> {name}")
                return Weapon.UNKNOWN

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

        players = ticks_df["steamid"].unique()
        ticks = ticks_df["tick"].unique()

        for tick in ticks:
            players_dict = {}
            for player in players:
                player_row = ticks_df[(ticks_df["steamid"] == player) & (ticks_df["tick"] == tick)]
                state = PlayerState(
                    player_steamid=SteamID(player),
                    position=Position(player_row["X"].item(), player_row["Y"].item(), player_row["Z"].item()),
                    velocity=Velocity(player_row["velocity_X"].item(), player_row["velocity_Y"].item(), player_row["velocity_Z"].item()),
                    view_angle=ViewAngle(player_row["yaw"].item(), player_row["pitch"].item()),
                    health=player_row["health"].item(),
                    armor=player_row["armor_value"].item(),
                    active_weapon=DemoAnalyzer.convert_weapon_name(player_row["active_weapon_name"].item()),
                    scoped=player_row["is_scoped"].item(),
                    flashed=(player_row["flash_duration"].item() > 0),
                    alive=player_row["is_alive"].item()
                )
                players_dict[player] = state

            tick_entity = Tick(tick=tick, player_states=players_dict)
            tick_dict[tick] = tick_entity

        return TickStore(
            ticks=tick_dict
        )
    