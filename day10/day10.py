import collections
import functools

import advent_tools


def process_input(data):
    return sorted(data)


def run_part_1(data):
    diffs = [a - b for a, b in zip(data[1:], data[:-1])]
    count = collections.Counter(diffs)
    return (count[1] + 1) * (count[3] + 1)


@functools.lru_cache
def count_ways(data, start, end):
    if start == end:
        return 1
    next_nums = [num for num in data if 1 <= num - start <=3]
    count = 0
    for next_num in next_nums:
        count = count + count_ways(data, next_num, end)
    return count


def run_part_2(data):
    builtin = max(data) + 3
    return count_ways(tuple(data + [builtin]), 0, builtin)


if __name__ == '__main__':
    data = advent_tools.read_one_int_per_line()
    data = process_input(data)
    print('Part 1:', run_part_1(data))
    print('Part 2:', run_part_2(data))