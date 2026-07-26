from dataclasses import dataclass

from ..events.event import Event

@dataclass
class Round:
    """
    Represents one round in a match.
    """

    round_number: int
    winning_team: str
    events: list[Event]  # List of events that occurred during the round
    