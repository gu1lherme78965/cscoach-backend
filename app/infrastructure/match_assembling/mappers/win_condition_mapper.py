from app.domain.enums.win_condition import WinCondition

unknown_win_conditions = set()

ct_killed = ["ct_killed"]
t_killed = ["t_killed"]
bomb_exploded = ["bomb_exploded"]

WIN_CONDITION_MAP = {
    **{name: WinCondition.CT_ELIMINATED for name in ct_killed},
    **{name: WinCondition.T_ELIMINATED for name in t_killed},
    **{name: WinCondition.BOMB_EXPLOSION for name in bomb_exploded}
}

def convert_win_condition(condition: str) -> WinCondition:
    if condition not in WIN_CONDITION_MAP:
        if type(condition) == str and condition:
            unknown_win_conditions.add(condition)
        return WinCondition.UNKNOWN
    return WIN_CONDITION_MAP[condition]

def get_unknown_win_conditions() -> set[str]:
    return unknown_win_conditions
