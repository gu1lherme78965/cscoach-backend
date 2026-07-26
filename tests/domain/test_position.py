from app.domain.value_objects.position import Position

def test_position_initialization():
    position = Position(x=1.0, y=2.5, z=3.0)

    assert position.x == 1.0
    assert position.y == 2.5
    assert position.z == 3.0