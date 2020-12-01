import itertools

import advent_tools


def run_part_1(data):
    for a, b in itertools.combinations(data, 2):
        if a + b == 2020:
            return a * b


def run_part_2(data):
    for a, b, c in itertools.combinations(data, 3):
        if a + b + c == 2020:
            return a * b * c


if __name__ == '__main__':
    data = [row[0] for row in advent_tools.read_all_integers()]
    print(run_part_1(data))
    print(run_part_2(data))