from dataclasses import dataclass

from .round import Round

@dataclass
class Match:
    """
    Represents a match in the game.
    """

    map_name: str
    rounds: list[Round]  # List of rounds in the match
    