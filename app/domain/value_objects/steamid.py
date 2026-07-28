from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class SteamID:

    value: int
