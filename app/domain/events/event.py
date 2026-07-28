from dataclasses import dataclass

from ..value_objects.position import Position

@dataclass(frozen=True)
class Event:
    """
    Represents an event that occurs in the game world.
    """

    tick: int
