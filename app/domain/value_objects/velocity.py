from dataclasses import dataclass

@dataclass(frozen=True)
class Velocity:
    
    x: float
    y: float
    z: float
