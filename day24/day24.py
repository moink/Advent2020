import collections

import numpy as np

import advent_tools

DIR_MAP = {'nw': (-1, -1),
           'ne': (1, -1),
           'w': (-2, 0),
           'e': (2, 0),
           'sw': (-1, 1),
           'se': (1, 1)}

DIRECTIONS = {key: np.asarray(val) for key, val in DIR_MAP.items()}


def main():
    flipped = [get_tile_flipped(line) for line in (advent_tools.read_input_lines())]
    floor = get_floor(flipped)
    print('Part 1:', sum(floor.values()))
    print('Part 2:', run_part_2(floor))


def get_tile_flipped(line):
    two_letter_dirs = [direc for direc in DIRECTIONS if len(direc) > 1]
    for direc in two_letter_dirs:
        if line == direc:
            return DIRECTIONS[direc]
        if line.startswith(direc):
            return DIRECTIONS[direc] + get_tile_flipped(line[2:])
    try:
        return DIRECTIONS[line[0]] + get_tile_flipped(line[1:])
    except IndexError:
        return DIRECTIONS[line[0]]


def get_floor(flipped):
    count_flips = collections.Counter(tuple(tile) for tile in flipped)
    floor = {tile: flip_count % 2 == 1 for tile, flip_count in count_flips.items()}
    return floor


def run_part_2(initial_black_tiles):
    floor = collections.defaultdict(bool)
    floor.update(initial_black_tiles)
    for day in range(100):
        counts = collections.defaultdict(int)
        for tile, black in floor.items():
            if black:
                for direction in DIRECTIONS.values():
                    counts[tuple(np.asarray(tile) + direction)] += 1
        all_tiles = set(floor.keys()).union(counts.keys())
        for tile in all_tiles:
            if floor[tile] and (counts[tile] == 0 or counts[tile] > 2):
                floor[tile] = False
            elif not(floor[tile]) and counts[tile] == 2:
                floor[tile] = True
    return sum(floor.values())


if __name__ == '__main__':
    main()