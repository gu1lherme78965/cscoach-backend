from dataclasses import dataclass
from datetime import timedelta
from uuid import UUID

from ..value_objects.position import Position

@dataclass(frozen=True)
class Event:
    """
    Represents an event that occurs in the game world.
    """

    timestamp: timedelta
    player_id: UUID
    position: Position
