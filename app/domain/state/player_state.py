from dataclasses import dataclass

from ..value_objects.position import Position
from ..value_objects.velocity import Velocity
from ..value_objects.view_angle import ViewAngle
from ..value_objects.steamid import SteamID
from ..entities.weapon import Weapon

@dataclass(frozen=True)
class PlayerState:
    player_steamid: SteamID

    position: Position
    velocity: Velocity
    view_angle: ViewAngle

    health: int
    armor: int

    active_weapon: Weapon

    scoped: bool
    flashed: bool
    alive: bool
