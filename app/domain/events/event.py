from dataclasses import dataclass
from datetime import deltatime

@dataclass(frozen=True)
class Event:
    """
    Represents an event that occurs in the game world.
    """

    timestamp: deltatime
