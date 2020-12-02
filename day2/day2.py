import collections

import advent_tools


def is_valid_part_one(line):
    min_count, max_count, letter, password = process_line(line)
    c = collections.Counter(password)
    return min_count <= c[letter] <= max_count


def is_valid_part_two(line):
    first, last, letter, password = process_line(line)
    return (password[first - 1] == letter) + (password[last - 1] == letter) == 1


def process_line(line):
    numbers, letter_colon, password = line.split(' ')
    first, last = (int(num) for num in numbers.split('-'))
    letter = letter_colon[0]
    return first, last, letter, password


def run_part_1():
    return advent_tools.count_times_true(is_valid_part_one)


def run_part_2():
    return advent_tools.count_times_true(is_valid_part_two)


if __name__ == '__main__':
    print(run_part_1())
    print(run_part_2())
    # rank today: 719