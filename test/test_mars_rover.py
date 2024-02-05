from src.mars_rover import MarsRover


def test_dummy():
    assert True == True


def test_move_forward_east():
    rover = MarsRover()
    rover.move_forward_east()
    moved_forwarded_location = [1, 0]
    assert rover.location == moved_forwarded_location
