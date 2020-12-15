import advent_tools


def memory_game(starting_numbers, end):
    last_called = {n: i for i, n in enumerate(starting_numbers[:-1])}
    prev_number = starting_numbers[-1]
    for turn in range(len(starting_numbers), end):
        try:
            last_turn = last_called[prev_number]
        except KeyError:
            number = 0
        else:
            number = turn - last_turn - 1
        last_called[prev_number] = turn - 1
        prev_number = number
    return number


def run_part_1(starting_numbers):
    return memory_game(starting_numbers, 2020)


def run_part_2(starting_numbers):
    return memory_game(starting_numbers, 30000000)


if __name__ == '__main__':
    data = advent_tools.read_all_integers()[0]
    print('Part 1:', run_part_1(data))
    print('Part 2:', run_part_2(data))