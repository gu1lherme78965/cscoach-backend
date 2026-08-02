from app.domain.enums.teams import Team

unknown_teams = set()

ct = ["ct", "counter_terrorist", "CT"]
t = ["t", "terrorist", "T"]

TEAM_MAP = {
    **{name: Team.COUNTER_TERRORIST for name in ct},
    **{name: Team.TERRORIST for name in t}
}

def convert_team_name(name: str) -> Team:
    if name not in TEAM_MAP:
        if type(name) == str and name:
            unknown_teams.add(name)
        return Team.UNKNOWN
    return TEAM_MAP[name]

def get_unknown_teams() -> set[str]:
    return unknown_teams
