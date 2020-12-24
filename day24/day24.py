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
    data = [process_line(line) for line in (advent_tools.read_input_lines())]
    floor = get_initial_map(data)
    print('Part 1:', run_part_1(floor))
    print('Part 2:', run_part_2(floor))


def process_line(line):
    two_letter_dirs = [direc for direc in DIRECTIONS if len(direc) > 1]
    for direc in two_letter_dirs:
        if line == direc:
            return [direc]
        if line.startswith(direc):
            return [direc] + process_line(line[2:])
    try:
        return [line[0]] + process_line(line[1:])
    except IndexError:
        return [line[0]]


def get_initial_map(data):
    floor = collections.defaultdict(bool)
    for line in data:
        tile = np.asarray((0, 0))
        for direc in line:
            tile = tile + DIRECTIONS[direc]
        floor[tuple(tile)] = not floor[tuple(tile)]
    return floor


def run_part_1(floor):
    return sum(floor.values())


def run_part_2(floor):
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