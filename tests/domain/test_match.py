from datetime import timedelta
from uuid import UUID

from app.domain.entities.player import Player
from app.domain.entities.match import Match
from app.domain.entities.round import Round
from app.domain.events.event import Event
from app.domain.value_objects.position import Position

def test_create_match_with_rounds_and_events():
    # Create players
    player1 = Player(id=UUID("12345678-1234-5678-1234-567812345678"), name="Player1")
    player2 = Player(id=UUID("87654321-4321-8765-4321-876543218765"), name="Player2")

    # Create events
    event1 = Event(
        timestamp=timedelta(seconds=10),
        player_id=player1.id,
        position=Position(x=100.0, y=200.0, z=50.0)
    )
    event2 = Event(
        timestamp=timedelta(seconds=20),
        player_id=player2.id,
        position=Position(x=150.0, y=250.0, z=50.0)
    )

    # Create rounds
    round1 = Round(
        round_number=1,
        winning_team="Terrorists",
        events=[event1, event2]
    )

    # Create match
    match = Match(
        map_name="de_mirage",
        rounds=[round1]
    )

    # Assertions
    assert match.map_name == "de_mirage"
    assert len(match.rounds) == 1
    assert match.rounds[0].round_number == 1
    assert match.rounds[0].winning_team == "Terrorists"
    assert len(match.rounds[0].events) == 2
    assert match.rounds[0].events[0].player_id == player1.id
    assert match.rounds[0].events[1].player_id == player2.id
    