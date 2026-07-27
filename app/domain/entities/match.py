from dataclasses import dataclass

from .round import Round
from ..enums.maps import Map
from ..timeline.event_timeline import EventTimeline
from ..timeline.tick_store import TickStore

@dataclass
class Match:
    """
    Represents a match in the game.
    """

    map_name: Map
    rounds: list[Round]  # List of rounds in the match
    event_timeline: EventTimeline
    tick_store: TickStore
