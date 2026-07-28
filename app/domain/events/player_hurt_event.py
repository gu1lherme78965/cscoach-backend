from dataclasses import dataclass

from app.domain.enums.weapons import Weapon
from app.domain.enums.body_part import BodyPart
from app.domain.events.event import Event
from app.domain.value_objects.steamid import SteamID

@dataclass(frozen=True, slots=True)
class PlayerHurtEvent(Event):
    attacker_id: SteamID
    victim_id: SteamID

    weapon: Weapon
    hit_location: BodyPart

    dmg_health: int
    dmg_armor: int
    remaining_health: int
    remaining_armor: int
