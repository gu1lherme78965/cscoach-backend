from app.domain.entities.match import Match


class DemoAnalyzer:
    match: Match

    def __init__(self, match: Match):
        self.match = match
