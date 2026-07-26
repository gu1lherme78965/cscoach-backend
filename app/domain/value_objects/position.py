from dataclasses import dataclass

@dataclass(frozen=True)
class Position:
    """
    Represents a position in 3D space withing the game world.
    """

    x: float
    y: float
    z: float
    