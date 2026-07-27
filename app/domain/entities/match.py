from dataclasses import dataclass

from .round import Round
from .player import Player
from ..enums.maps import Map
from ..timeline.event_timeline import EventTimeline
from ..timeline.tick_store import TickStore

@dataclass
class Match:
    """
    Represents a match in the game.
    """

    map: Map
    rounds: list[Round]  # List of rounds in the match
    players: list[Player]
    event_timeline: EventTimeline
    tick_store: TickStore
