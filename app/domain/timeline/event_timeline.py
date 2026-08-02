from dataclasses import dataclass, field

from ..events.event import Event

@dataclass
class EventTimeline:
    """
    Represents a timeline of events in a CS2 demo.
    """

    events: list[Event] = field(default_factory=list)

    def add_event(self, event: Event):
        self.events.append(event)

    def sort_events(self):
        self.events.sort(key=lambda event: event.tick)

    def get_all_events(self):
        return self.events

    def extend_events(self, events: list[Event]):
        self.events.extend(events)

    def get_between_ticks(self, start_tick: int, end_tick: int):
        return [event for event in self.events if start_tick <= event.tick <= end_tick]
    