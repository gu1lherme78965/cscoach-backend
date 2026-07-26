from dataclasses import dataclass
from uuid import UUID

from .event import Event

@dataclass(frozen=True)
class FlashEvent(Event):
    """
    Represents a flash event that occurs in the game world.
    """

    victim_id: UUID
    duration: float  # Duration of the flash effect in seconds
    