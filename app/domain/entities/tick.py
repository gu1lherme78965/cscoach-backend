from dataclasses import dataclass

from ..state.player_state import PlayerState

@dataclass(frozen=True)
class Tick:
    tick: int

    player_states: dict[int, PlayerState]
    