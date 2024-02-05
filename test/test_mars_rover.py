import pytest

from src.mars_rover import MarsRover, EAST, SOUTH, WEST, NORTH


def test_dummy():
    assert True == True


@pytest.mark.parametrize(
    "location, direction, expected",
    [
        ([0, 0], NORTH, [0, 1]),
        ([0, 0], EAST, [1, 0]),
        ([0, 0], SOUTH, [0, -1]),
        ([0, 0], WEST, [-1, 0]),
    ],
)
def test_move_forward(location: list[int], direction: str, expected: list[int]):
    rover = MarsRover(location=location, direction=direction)
    rover.move_forward()
    assert rover.location == expected


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
