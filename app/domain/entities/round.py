from dataclasses import dataclass

from ..events.event import Event
from ..enums.teams import Team

@dataclass
class Round:
    """
    Represents one round in a match.
    """

    round_number: int
    winning_team: Team
    events: list[Event]  # List of events that occurred during the round
