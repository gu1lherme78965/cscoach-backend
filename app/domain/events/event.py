from dataclasses import dataclass
from datetime import deltatime
from uuid import UUID

from ..value_objects.position import Position

@dataclass(frozen=True)
class Event:
    """
    Represents an event that occurs in the game world.
    """

    timestamp: deltatime
    player_id: UUID
    position: Position
