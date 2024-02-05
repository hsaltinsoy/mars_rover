NORTH = "N"
EAST = "E"
SOUTH = "S"
WEST = "W"


class MarsRover:
    def __init__(self, location: list[int], direction: str) -> None:
        self.location = location
        self.direction = direction

    def move_forward(self) -> None:
        if self.direction == NORTH:
            self.location[1] += 1
        elif self.direction == EAST:
            self.location[0] += 1
        elif self.direction == SOUTH:
            self.location[1] -= 1
        elif self.direction == WEST:
            self.location[0] -= 1

    def move_backwards(self) -> None:
        if self.direction == NORTH:
            self.location[1] -= 1
        elif self.direction == EAST:
            self.location[0] -= 1
        elif self.direction == SOUTH:
            self.location[1] += 1
        elif self.direction == WEST:
            self.location[0] += 1
