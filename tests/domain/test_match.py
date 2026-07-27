from app.domain.entities.player import Player
from app.domain.entities.match import Match
from app.domain.entities.round import Round
from app.domain.events.event import Event
from app.domain.value_objects.steamid import SteamID
from app.domain.enums.event_types import EventType
from app.domain.enums.maps import Map

def test_create_match_with_rounds_and_events():
    # Create players
    player1 = Player(id=SteamID(50), name="Player1", team=2)
    player2 = Player(id=SteamID(3), name="Player2", team=3)

    # Create events
    event1 = Event(
        tick=498,
        event_type=EventType.BASE_EVENT
    )
    event2 = Event(
        tick=30,
        event_type=EventType.BASE_EVENT
    )

    # Create rounds
    round1 = Round(
        round_number=1,
        winning_team="Terrorists",
        events=[event1, event2]
    )

    # Create match
    match = Match(
        map=Map.MIRAGE,
        rounds=[round1],
        players=[player1, player2],
        event_timeline=None,
        tick_store=None
    )

    # Assertions
    assert match.map == Map.MIRAGE
    assert len(match.rounds) == 1
    assert match.rounds[0].round_number == 1
    assert match.rounds[0].winning_team == "Terrorists"
    assert len(match.rounds[0].events) == 2
    assert match.rounds[0].events[0].tick == 498
    assert match.rounds[0].events[1].event_type == EventType.BASE_EVENT
    