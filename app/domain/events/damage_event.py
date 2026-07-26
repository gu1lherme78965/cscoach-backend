from dataclasses import dataclass
from uuid import UUID

from .event import Event
from ..enums.body_part import BodyPart

@dataclass(frozen=True)
class DamageEvent(Event):
    """
    Represents a damage event that occurs in the game world.
    """

    victim_id: UUID
    damage_amount: float # Amount of damage inflicted
    hit_location: BodyPart # Location on the body where the damage occurred
