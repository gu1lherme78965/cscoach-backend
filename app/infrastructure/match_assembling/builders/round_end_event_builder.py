from pandas import DataFrame

from app.infrastructure.match_assembling.builders.event_builder import EventBuilder
from app.infrastructure.match_assembling.mappers.win_condition_mapper import convert_win_condition
from app.infrastructure.match_assembling.mappers.team_mapper import convert_team_name
from app.domain.events.round_end_event import RoundEndEvent
from app.domain.enums.event_type import EventType

class RoundEndEventBuilder(EventBuilder):

    EVENT_TYPE = EventType.ROUND_END

    def build_event(self, event_data: DataFrame) -> list[RoundEndEvent]:
        events = list()
        for row in event_data.itertuples(index=False):
            events.append(RoundEndEvent(
                tick=row.tick,
                round_number=row.round,
                winning_team=convert_team_name(row.winner),
                win_condition=convert_win_condition(row.reason),
            ))
        return events