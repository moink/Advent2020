import math

import advent_tools


def is_tree(grid, x, y):
    h, w = grid.grid.shape
    i = x % w
    tree = grid.grid[y, i]
    return tree


def count_trees(grid, slope):
    max_y = grid.grid.shape[0]
    slope_x, slope_y = slope
    x = 0
    y = 0
    tree_count = 0
    for i in range(max_y // slope_y):
        tree_count = tree_count + is_tree(grid, x, y)
        x += slope_x
        y += slope_y
    return tree_count


def run_part_1(grid):
    return count_trees(grid, (3, 1))


def run_part_2(grid):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    results = [float(count_trees(grid, slope)) for slope in slopes]
    return int(math.prod(results))


if __name__ == '__main__':
    data = advent_tools.PlottingGrid((324, 31))
    data.read_input_file()
    print(run_part_1(data))
    print(run_part_2(data))