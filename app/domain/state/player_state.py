from dataclasses import dataclass

from ..value_objects.steamid import SteamID
from ..entities.weapon import Weapon

@dataclass(frozen=True, slots=True)
class PlayerState:
    player_steamid: SteamID

    x: float
    y: float
    z: float

    velocity_x: float
    velocity_y: float
    velocity_z: float

    pitch: float
    yaw: float

    health: int
    armor: int

    active_weapon: Weapon

    scoped: bool
    flashed: bool
    alive: bool
