class MarsRover:
    location = [0, 0]

    def move_forward_east(self) -> None:
        self.location[0] += 1

    def move_backwards(self) -> None:
        self.location[1] -= 1
