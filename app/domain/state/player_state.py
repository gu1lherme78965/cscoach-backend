from dataclasses import dataclass

from ..value_objects.position import Position
from ..value_objects.velocity import Velocity
from ..value_objects.view_angle import ViewAngle
from ..entities.weapon import Weapon

@dataclass(frozen=True)
class PlayerState:
    player_steamid: int

    position: Position
    velocity: Velocity
    view_angle: ViewAngle

    health: int
    armor: int
    money: int

    active_weapon: Weapon

    scoped: bool
    flashed: bool
    alive: bool
