from pandas import DataFrame

from app.domain.entities.match import Match
from app.domain.entities.tick import Tick
from app.domain.timeline.event_timeline import EventTimeline
from app.domain.timeline.tick_store import TickStore
from app.domain.state.player_state import PlayerState
from app.domain.enums.event_type import EventType
from app.domain.enums.body_part import BodyPart
from app.domain.value_objects.position import Position
from app.domain.value_objects.velocity import Velocity
from app.domain.value_objects.view_angle import ViewAngle
from app.domain.value_objects.steamid import SteamID
from app.infrastructure.demo_parser.parser import CS2DemoParser
from app.infrastructure.match_assembling.mappers.weapon_mapper import get_unknown_weapons, convert_weapon_name
from app.infrastructure.match_assembling.mappers.map_mapper import get_unknown_maps, convert_map_name
from app.infrastructure.match_assembling.mappers.win_condition_mapper import get_unknown_win_conditions, convert_win_condition
from app.infrastructure.match_assembling.mappers.team_mapper import get_unknown_teams, convert_team_name
from app.infrastructure.match_assembling.mappers.hit_location_mapper import get_unknown_locations, convert_hit_location
from app.infrastructure.match_assembling.builders import (
    PlayerDeathEventBuilder,
    PlayerHurtEventBuilder,
    RoundEndEventBuilder,
    WeaponFireEventBuilder,
    BeginNewMatchEventBuilder,
    RoundStartEventBuilder,
)

builders = [
    PlayerDeathEventBuilder(),
    PlayerHurtEventBuilder(),
    RoundEndEventBuilder(),
    WeaponFireEventBuilder(),
    BeginNewMatchEventBuilder(),
    RoundStartEventBuilder()
]

class MatchAssembler:

    match: Match
    parser: CS2DemoParser
    event_df_dict: dict[EventType, DataFrame]

    def __init__(self, file_path: str):
        self.parser = CS2DemoParser(file_path)
        self.event_df_dict = self.parser.get_event_df_dict()
        self.unknown_teams = set()
        self.unknown_locations = set()
        self.unknown_win_conditions = set()
        self.steamid_cache = dict()
        self.match = Match()

    def assemble_match(self) -> Match:
        # TODO
        header = self.parser.get_header()
        players = self.parser.extract_player_list()
        player_info = self.parser.get_player_info()
        self.match.map = convert_map_name(header["map_name"])

        tick_store = self.build_tick_store()

        event_timeline = self.build_event_timeline()

        unknown_weapons = get_unknown_weapons()
        unknown_maps = get_unknown_maps()
        unknown_win_conditions = get_unknown_win_conditions()
        unknown_teams = get_unknown_teams()
        unknown_locations = get_unknown_locations()
        if (unknown_weapons):
            print(f"Encountered unknown weapons in this game: {unknown_weapons}")
        if (unknown_maps):
            print(f"Encountered unknown maps in this game: {unknown_maps}")
        if (unknown_locations):
            print(f"Encountered unknown locations in this game: {unknown_locations}")
        if (unknown_teams):
            print(f"Encountered unknown teams in this game: {unknown_teams}")
        if (unknown_win_conditions):
            print(f"Encountered unknown win conditions in this game: {unknown_win_conditions}")

        return self.match

    def build_event_timeline(self) -> EventTimeline:
        event_timeline = EventTimeline()

        for builder in builders:
            if builder is not None:
                events = builder.build_event(self.event_df_dict[builder.EVENT_TYPE])
                if not events:
                    continue
                event_timeline.extend_events(events)
        event_timeline.sort_events()
        return event_timeline

    def build_tick_store(self) -> TickStore:
        tick_dict = {}
        ticks_df = self.parser.parse_ticks([
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
        ticks_df = ticks_df[ticks_df["tick"] >= self.parser.get_match_start_tick()]

        for row in ticks_df.itertuples(index=False):
            tick = row.tick

            if tick not in tick_dict:
                tick_dict[tick] = Tick(tick, {})

            if row.steamid not in self.steamid_cache:
                self.steamid_cache[row.steamid] = SteamID(row.steamid)

            tick_dict[tick].player_states[row.steamid] = PlayerState(
                player_steamid=self.steamid_cache[row.steamid],
                x=row.X,
                y=row.Y,
                z=row.Z,
                velocity_x=row.velocity_X,
                velocity_y=row.velocity_Y,
                velocity_z=row.velocity_Z,
                pitch=row.pitch,
                yaw=row.yaw,
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
    