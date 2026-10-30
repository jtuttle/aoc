from collections import namedtuple
#from typing import NamedTuple, Callable

with open("../input/day-06.in") as file:
    input = file.readlines()

class Grid:
    def __init__(self, width, height, value):
        self.grid = [ [value] * width for i in range(height)]

class BinaryGrid(Grid):
    def __init__(self, width, height):
        super().__init__(width, height, False)

    def on(self, x, y):
        self.grid[y][x] = True
    
    def off(self, x, y):
        self.grid[y][x] = False

    def toggle(self, x, y):
        self.grid[y][x] = not self.grid[y][x]

    def total_lights_on(self):
        count = 0

        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x]: count += 1

        return count

class ContinuousGrid(Grid):
    def __init__(self, width, height):
        super().__init__(width, height, 0)
    
    def on(self, x, y):
        self.grid[y][x] += 1
    
    def off(self, x, y):
        self.grid[y][x] = max(0, self.grid[y][x] - 1)

    def toggle(self, x, y):
        self.grid[y][x] += 2

    def total_brightness(self):
        brightness = 0

        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                brightness += self.grid[y][x]

        return brightness

def apply(action, x, y, grid):
    match action:
        case "on":
            grid.on(x, y)
        case "off":
            grid.off(x, y)
        case _:
            grid.toggle(x, y)

test_grid = BinaryGrid(2, 2)
for test in (
    [
        (
            "on", 1, 0,
            [
                [False, True ],
                [False, False],
            ]
        ),
        (
            "off", 1, 0,
            [
                [False, False],
                [False, False],
            ]
        ),
        (
            "toggle", 0, 1,
            [
                [False, False],
                [True,  False],
            ]
        ),
        (
            "toggle", 0, 1,
            [
                [False, False],
                [False, False],
            ]
        )
    ]
):
    apply(test[0], test[1], test[2], test_grid)
    assert test_grid.grid == test[3]

test_grid = ContinuousGrid(2, 2)
for test in (
    [
        (
            "on", 1, 1,
            [
                [0, 0],
                [0, 1],
            ]
        ),
        (
            "off", 1, 1,
            [
                [0, 0],
                [0, 0],
            ]
        ),
        (
            "off", 1, 1,
            [
                [0, 0],
                [0, 0],
            ]
        ),
        (
            "toggle", 0, 0,
            [
                [2, 0],
                [0, 0],
            ]
        )
    ]
):
    apply(test[0], test[1], test[2], test_grid)
    assert test_grid.grid == test[3]

binary_grid = BinaryGrid(1000, 1000)
continuous_grid = ContinuousGrid(1000, 1000)

for line in input:
    instruction_split = line.split()

    from_x, from_y = map(lambda x: int(x), instruction_split[-3].split(','))
    to_x, to_y = map(lambda x: int(x), instruction_split[-1].split(','))
    action = instruction_split[1]

    for x in range(from_x, to_x + 1):
        for y in range(from_y, to_y + 1):
            apply(action, x, y, binary_grid)
            apply(action, x, y, continuous_grid)

print("Part 1: " + str(binary_grid.total_lights_on()))
print("Part 2: " + str(continuous_grid.total_brightness()))