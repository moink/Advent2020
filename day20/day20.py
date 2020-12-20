import collections
import math
import numpy as np
import matplotlib.pyplot as plt

import advent_tools


SEA_MONSTER = (
"""                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
)


def main():
    # advent_tools.TESTING = True
    data = advent_tools.read_input_line_groups()
    tiles = create_tiles(data)
    matches = get_matches(tiles)
    print('Part 1:', run_part_1(matches))
    print('Part 2:', run_part_2(tiles, matches))


def create_tiles(data):
    tiles = {}
    shape = (10, 10)
    for group in data:
        group_num = int(group[0].split()[1][:-1])
        tiles[group_num] = read_grid(group[1:], shape)
    return tiles


def get_matches(data):
    sides = collections.defaultdict(dict)
    for tile_num, grid in data.items():
        sides[tile_num]["top"] = grid[0, :]
        sides[tile_num]["top_reversed"] = np.flip(grid[0, :])
        sides[tile_num]["bottom"] = grid[-1, :]
        sides[tile_num]["bottom_reversed"] = np.flip(grid[-1, :])
        sides[tile_num]["left"] = grid[:, 0]
        sides[tile_num]["left_reversed"] = np.flip(grid[:, 0])
        sides[tile_num]["right"] = grid[:, -1]
        sides[tile_num]["right_reversed"] = np.flip(grid[:, -1])
    sides = dict(sides)
    matches = collections.defaultdict(lambda: collections.defaultdict(list))
    for tile_num, tile_sides in sides.items():
        for side_name, array in tile_sides.items():
            for tile_num2, tile_sides2 in sides.items():
                for side_name2, array2 in tile_sides2.items():
                    if (array == array2).all() and tile_num != tile_num2:
                        matches[tile_num][side_name].append((tile_num2, side_name2))
                        break
    matches = {key: dict(val) for key, val in matches.items()}
    return matches


def run_part_1(matches):
    corners = [key for key, val in matches.items() if len(val) == 4]
    return math.prod(corners)


def run_part_2(data, matches):
    big_grid = assemble_grid(data, matches)
    sea_monster = read_grid(SEA_MONSTER.splitlines(), big_grid.shape).astype(bool)
    found = False
    for orient in generate_orientations(big_grid):
        for top_edge in range(big_grid.shape[0]- 2):
            for left_edge in range(big_grid.shape[1] - 19):
                window = np.roll(np.roll(sea_monster, left_edge, axis=1), top_edge, axis=0)
                if orient[window].all():
                    orient[window] = 2
                    found = True
        if found:
            good_orient = orient
            break
    plt.imshow(good_orient)
    plt.show()
    return (good_orient == 1).sum()


def assemble_grid(data, matches):
    side_len = int(math.sqrt(len(data)))
    grid = solve_grid(data, matches)
    data = rotate_pieces(data, grid)
    big_grid = np.concatenate([np.concatenate([data[g][1:-1, 1:-1]
                                               for g in grid[i]], axis=1)
                               for i in range(side_len)], axis=0)
    return big_grid


def rotate_pieces(data, grid):
    side_len = int(math.sqrt(len(data)))
    row = 0
    for col in range(1, side_len):
        left_tile = grid[row, col - 1]
        next_tile = grid[row, col]
        for orientation in generate_orientations(data[next_tile]):
            if (orientation[:, 0] == data[left_tile][:, -1]).all():
                data[next_tile] = orientation
                break
        else:
            grid = grid.transpose()
            left_tile = grid[row, col - 1]
            next_tile = grid[row, col]
            for orientation in generate_orientations(data[next_tile]):
                if (orientation[:, 0] == data[left_tile][:, -1]).all():
                    data[next_tile] = orientation
                    break
    for col in range(side_len):
        for row in range(1, side_len):
            top_tile = grid[row - 1, col]
            next_tile = grid[row, col]
            for orientation in generate_orientations(data[next_tile]):
                if (orientation[0, :] == data[top_tile][-1, :]).all():
                    data[next_tile] = orientation
                    break
            else:
                raise RuntimeError('No fitting orientation')
    return data

def generate_orientations(grid):
    for k in range(4):
        yield np.rot90(grid, k=k)
        yield np.rot90(np.flip(grid, axis=0), k=k)


def solve_grid(tiles, matches):
    side_len = int(math.sqrt(len(tiles)))
    corners = [key for key, val in matches.items() if len(val) == 4]
    tile_matches = collections.defaultdict(set)
    for tile1, sides in matches.items():
        for sidename, side in sides.items():
            tile_matches[tile1].add(side[0][0])
    first_tile = corners[0]
    inner_sides = matches[first_tile].keys()
    if 'right' in inner_sides and 'bottom' in inner_sides:
        k = 0
    elif 'top' in inner_sides and 'right' in inner_sides:
        k = 3
    elif 'top' in inner_sides and 'left' in inner_sides:
        k = 2
    else:
        k = 1
    tiles[first_tile] = np.rot90(tiles[first_tile], k).transpose()
    grid = np.zeros((side_len, side_len), dtype=int)
    grid[0, 0] = first_tile
    for col_num in range(side_len - 1):
        found = False
        for next_tile in tile_matches[grid[0, col_num]]:
            for orient in generate_orientations(tiles[next_tile]):
                if (orient[:, 0] == tiles[grid[0, col_num]][:, -1]).all():
                    found = True
                    tiles[next_tile] = orient
                    grid[0, col_num + 1] = next_tile
                    tile_matches[grid[0, col_num]].remove(grid[0, col_num + 1])
                    tile_matches[grid[0, col_num + 1]].remove(grid[0, col_num])
                    break
            if found:
                break
    while grid.min() == 0:
        for i in range(side_len):
            for j in range(side_len):
                if grid[j, i] == 0:
                    neighbours = []
                    if i > 0:
                        neighbour = grid[j, i-1]
                        if neighbour:
                            neighbours.append(neighbour)
                    if j > 0:
                        neighbour = grid[j-1, i]
                        if neighbour:
                            neighbours.append(neighbour)
                    if neighbours:
                        available = set.intersection(*[tile_matches[n] for n in neighbours])
                        if len(available) == 1:
                            next_tile = sorted(available)[0]
                            grid[j, i] = next_tile
                            for first_tile in neighbours:
                                tile_matches[first_tile].remove(next_tile)
                                tile_matches[next_tile].remove(first_tile)
    return grid





def read_grid(lines, shape):
    char_map = {'.': 0, '#': 1, ' ': 0}
    grid = np.zeros(shape)
    for y_pos, line in enumerate(lines):
        for x_pos, char in enumerate(line):
            grid[(y_pos, x_pos)] = char_map[char]
    return grid




if __name__ == '__main__':
    main()