from src.mars_rover import MarsRover


def test_dummy():
    assert True == True


def test_move_backwards_north():
    rover = MarsRover()
    rover.move_backwards()
    assert rover.location == [0, -1]
