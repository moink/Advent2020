import collections
import functools

import advent_tools


def run_part_1(data):
    diffs = [a - b for a, b in zip(data[1:], data[:-1])]
    count = collections.Counter(diffs)
    return (count[1] + 1) * (count[3] + 1)


def run_part_2(data):
    end = max(data) + 3
    numbers = data + [end]

    @functools.lru_cache
    def count_ways(start):
        if start == end:
            return 1
        count = sum(count_ways(num) for num in numbers if 1 <= num - start <= 3)
        return count

    return count_ways(0)


if __name__ == '__main__':
    input_data = sorted(advent_tools.read_one_int_per_line())
    print('Part 1:', run_part_1(input_data))
    print('Part 2:', run_part_2(input_data))