from dataclasses import dataclass, field

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

    map: Map = Map.UNKNOWN  # Map on which the match was played
    rounds: list[Round] = field(default_factory=list)  # List of rounds in the match
    players: list[Player] = field(default_factory=list)
    event_timeline: EventTimeline | None = None
    tick_store: TickStore | None = None

    def summarize(self):
        print("________________")
        print(f"Map: {self.map}")
        print("Players:")
        for player in self.players:
            print(f"    {player.name} - Team {player.team}")
