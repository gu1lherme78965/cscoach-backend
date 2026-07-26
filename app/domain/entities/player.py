from dataclasses import dataclass
from uuid import UUID

@dataclass
class Player:
    """
    Represents a player in the game world.
    """

    id: UUID
    name: str
    