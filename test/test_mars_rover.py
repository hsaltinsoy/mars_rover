from src.mars_rover import MarsRover, EAST, SOUTH


def test_dummy():
    assert True == True


def test_move_backwards_north():
    rover = MarsRover()
    rover.move_backwards()
    assert rover.location == [0, -1]


def test_move_backwards_east():
    rover = MarsRover()
    rover.direction = EAST
    rover.move_backwards()
    assert rover.location == [-1, 0]


def test_move_backwards_south():
    rover = MarsRover()
    rover.direction = SOUTH
    rover.move_backwards()
    assert rover.location == [0, 1]
