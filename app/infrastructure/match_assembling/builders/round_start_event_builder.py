from pandas import DataFrame

from app.infrastructure.match_assembling.builders.event_builder import EventBuilder
from app.domain.events.round_start_event import RoundStartEvent
from app.domain.enums.event_type import EventType

class RoundStartEventBuilder(EventBuilder):

    EVENT_TYPE = EventType.ROUND_START

    def build_event(self, event_data: DataFrame) -> list[RoundStartEvent]:
        events = list()
        for row in event_data.itertuples(index=False):
            events.append(RoundStartEvent(
                tick=row.tick,
                round_number=row.round
            ))
        return events