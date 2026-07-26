from dataclasses import dataclass
from uuid import UUID

from .event import Event

@dataclass(frozen=True)
class DamageEvent(Event):
    """
    Represents a damage event that occurs in the game world.
    """

    victim_id: UUID
    damage_amount: float # Amount of damage inflicted
    hit_location: str # Location on the bode where the damage occured
    