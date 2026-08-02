from pandas import DataFrame

from app.infrastructure.match_assembling.builders.event_builder import EventBuilder
from app.domain.events.begin_new_match_event import BeginNewMatchEvent
from app.domain.enums.event_type import EventType

class BeginNewMatchEventBuilder(EventBuilder):
    EVENT_TYPE = EventType.BEGIN_NEW_MATCH

    def build_event(self, event_data: DataFrame) -> list[BeginNewMatchEvent]:
        events = list()
        for row in event_data.itertuples(index=False):
            events.append(BeginNewMatchEvent(
                tick=row.tick
            ))
        return events