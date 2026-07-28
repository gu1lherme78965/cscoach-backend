from dataclasses import dataclass

from app.domain.events.event import Event
from app.domain.enums.win_condition import WinCondition
from app.domain.enums.teams import Team

@dataclass(frozen=True, slots=True)
class RoundEndEvent(Event):
    round_number: int
    win_condition: WinCondition
    winning_team: Team
