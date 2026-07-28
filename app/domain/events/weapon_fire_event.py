from dataclasses import dataclass

from app.domain.enums.weapons import Weapon
from app.domain.events.event import Event
from app.domain.value_objects.steamid  import SteamID

@dataclass(frozen=True, slots=True)
class WeaponFireEvent(Event):
    user_id: SteamID

    weapon: Weapon
    is_silenced: bool

    user_x: float
    user_y: float
    user_z: float
    user_pitch: float
    user_yaw: float