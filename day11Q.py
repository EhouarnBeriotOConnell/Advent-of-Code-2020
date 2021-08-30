import numpy as np
import itertools

with open("data/d11") as f:
    raw = f.readlines()

width, height = len(raw[0]), len(raw)
start = np.zeros((height, width), dtype=bool)
mask = np.zeros((height, width), dtype=bool)

for h, line in enumerate(raw):
    for w, seat in enumerate(line):
        if seat == "L":
            mask[h, w] = 1


def step(grid, mask):
    new_grid = grid.copy()
    for w, h in itertools.product(range(width), range(height)):
        if mask[h, w]:
            neighbors = (
                grid[max(0, h - 1):h + 1, max(0, w - 1):w + 1].sum()
                - grid[h, w] # do not count local seat as neighbor
            )
            if grid[h, w] and neighbors > 3:
                new_grid[h, w] = 0
            elif not grid[h, w] and neighbors < 1:
                new_grid[h, w] = 1
    return new_grid, np.any(new_grid != grid)


grid, changed = start, True
#while changed:
#    grid, changed = step(grid, mask)

grid[1,1] = 1#
grid[1, 2] = 1#
grid[2, 1] = 1#
#grid[1, 2] = 1
#grid[2, 1] = 1
#grid[2, 2] = 1
#grid[1, 2] = 1
#grid[2, 1] = 1

h = 2
w = 2
neighbors = (
                grid[max(0, h - 1):h + 1, max(0, w - 1):w + 1].sum()
                - grid[h, w] # do not count local seat as neighbor
            )
print(neighbors)
print("Part 1:", grid.sum())