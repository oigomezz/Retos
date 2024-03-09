class Direction:
    POSITIVEY = "POSITIVEY"
    NEGATIVEX = "NEGATIVEX"
    NEGATIVEY = "NEGATIVEY"
    POSITIVEX = "POSITIVEX"

    def __init__(self, direction):
        self.direction_to = direction

    def turn(self):
        if self.direction_to == Direction.POSITIVEY:
            self.direction_to = Direction.NEGATIVEX
        elif self.direction_to == Direction.NEGATIVEX:
            self.direction_to = Direction.NEGATIVEY
        elif self.direction_to == Direction.NEGATIVEY:
            self.direction_to = Direction.POSITIVEX
        elif self.direction_to == Direction.POSITIVEX:
            self.direction_to = Direction.POSITIVEY


def where_is_the_robot(steps):
    x = 0
    y = 0
    direction = Direction(Direction.POSITIVEY)

    for step in steps:
        if direction.direction_to == Direction.POSITIVEY:
            y += step
        elif direction.direction_to == Direction.NEGATIVEX:
            x -= step
        elif direction.direction_to == Direction.NEGATIVEY:
            y -= step
        elif direction.direction_to == Direction.POSITIVEX:
            x += step

        direction.turn()

    return f"x: {x}, y: {y}, direction: {direction.direction_to}"


print(where_is_the_robot([10, 5, -2]))
print(where_is_the_robot([0, 0, 0]))
print(where_is_the_robot([]))
print(where_is_the_robot([-10, -5, 2]))
print(where_is_the_robot([-10, -5, 2, 4, -8]))
