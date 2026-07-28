from dataclasses import dataclass

from app.domain.events.event import Event

@dataclass(frozen=True, slots=True)
class BeginNewMatchEvent(Event):
    pass
