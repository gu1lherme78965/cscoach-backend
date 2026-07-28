from dataclasses import dataclass

from app.domain.events.event import Event

@dataclass(frozen=True, slots=True)
class RoundStartEvent(Event):
    round_number: int