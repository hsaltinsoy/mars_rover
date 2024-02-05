import pytest

from src.mars_rover import MarsRover, EAST, SOUTH, WEST, NORTH


def test_dummy():
    assert True == True


def test_move_forward_east():
    rover = MarsRover(location=[0, 0], direction=EAST)
    rover.move_forward_east()
    moved_forwarded_location = [1, 0]
    assert rover.location == moved_forwarded_location


@pytest.mark.parametrize(
    "location, direction, expected",
    [
        ([0, 0], NORTH, [0, -1]),
        ([0, 0], EAST, [-1, 0]),
        ([0, 0], SOUTH, [0, 1]),
        ([0, 0], WEST, [1, 0]),
    ],
)
def test_move_backwards_north(location: list[int], direction: str, expected: list[int]):
    rover = MarsRover(location=location, direction=direction)
    rover.move_backwards()
    assert rover.location == expected
