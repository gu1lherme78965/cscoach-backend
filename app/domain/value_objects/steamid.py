from dataclasses import dataclass

@dataclass(frozen=True)
class SteamID:

    value: int
