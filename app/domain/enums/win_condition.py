from enum import Enum

class WinCondition(Enum):
    UNKNOWN = "Unknown"
    T_ELIMINATED = "T Eliminated"
    CT_ELIMINATED = "CT Eliminated"
    BOMB_EXPLOSION = "Bomb Explosion"
    TIME_EXPIRED = "Time Expired"