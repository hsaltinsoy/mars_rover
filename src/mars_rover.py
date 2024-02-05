NORTH = "N"
EAST = "E"
SOUTH = "S"
WEST = "W"


class MarsRover:
    def __init__(self) -> None:
        self.location = [0, 0]
        self.direction = NORTH

    def move_forward_east(self) -> None:
        self.location[0] += 1

    def move_backwards(self) -> None:
        if self.direction == NORTH:
            self.location[1] -= 1
        elif self.direction == EAST:
            self.location[0] -= 1
        elif self.direction == SOUTH:
            self.location[1] += 1
        elif self.direction == WEST:
            self.location[0] += 1
