from dataclasses import dataclass

from ..value_objects.steamid import SteamID

@dataclass
class Player:
    """
    Represents a player in the game world.
    """

    id: SteamID
    name: str
    