from dataclasses import dataclass
from datetime import timedelta
from uuid import UUID

from ..value_objects.position import Position
from ..enums.event_types import EventType

@dataclass(frozen=True)
class Event:
    """
    Represents an event that occurs in the game world.
    """

    tick: int
    event_type: EventType = EventType.BASE_EVENT
