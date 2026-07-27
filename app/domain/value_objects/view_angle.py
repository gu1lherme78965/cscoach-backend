from dataclasses import dataclass

@dataclass(frozen=True)
class ViewAngle:

    yaw: float
    pitch: float
    