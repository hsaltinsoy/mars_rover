NORTH = "N"
EAST = "E"
SOUTH = "S"
WEST = "W"


class MarsRover:
    location = [0, 0]
    direction = NORTH

    def move_forward_east(self) -> None:
        self.location[0] += 1

    def move_backwards(self) -> None:
        if self.direction == NORTH:
            self.location[1] -= 1
