from dataclasses import dataclass
from uuid import UUID

from .event import Event
from ..enums.weapons import Weapon
from ..enums.body_part import BodyPart

@dataclass(frozen=True)
class KillEvent(Event):
    """
    Represents a kill event that occurs in the game world.
    """

    victim_id: UUID
    weapon: Weapon
    hit_location: BodyPart  # Location on the body where the kill occurred
    