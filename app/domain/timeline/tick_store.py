from dataclasses import dataclass, field

from ..entities.tick import Tick

@dataclass
class TickStore:
    ticks: dict[int, Tick] = field(default_factory=dict)

    def add_tick(self, tick: Tick) -> None:
        self.ticks[tick.tick] = tick

    def get_tick(self, tick: int) -> Tick | None:
        return self.ticks[tick]

    def get_ticks_between(self, tick_start: int, tick_end: int) -> list[Tick] | None:
        return [tick for tick in self.ticks.values() if tick_start <= tick.tick <= tick_end]
    