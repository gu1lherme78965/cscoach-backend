from abc import ABC, abstractmethod
from pandas import DataFrame

from app.domain.enums.event_type import EventType
from app.domain.events.event import Event

class EventBuilder(ABC):

    EVENT_TYPE: EventType

    @abstractmethod
    def build_event(self, event_data: DataFrame) -> list[Event]:
        pass
    