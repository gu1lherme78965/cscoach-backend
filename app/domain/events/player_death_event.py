from dataclasses import dataclass

from app.domain.enums.weapons import Weapon
from app.domain.enums.body_part import BodyPart
from app.domain.events.event import Event
from app.domain.value_objects.steamid import SteamID

@dataclass(frozen=True, slots=True)
class PlayerDeathEvent(Event):
    attacker_id: SteamID
    victim_id: SteamID
    assister_id: SteamID

    weapon: Weapon
    hit_location: BodyPart

    distance: float
    dmg_health: int
    dmg_armor: int

    attacker_in_air: bool
    is_noscope: bool
    is_penetrated: bool
    is_through_smoke: bool
