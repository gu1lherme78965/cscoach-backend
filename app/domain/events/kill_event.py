from dataclasses import dataclass
from uuid import UUID

from .event import Event

@dataclass(frozen=True)
class KillEvent(Event):
    """
    Represents a kill event that occurs in the game world.
    """

    victim_id: UUID
    