import advent_tools


def run_part_1(numbers):
    return find_invalid(numbers, 25)


def find_invalid(numbers, length):
    for i in range(length, len(numbers)):
        found = False
        a = numbers[i - length:i]
        for x in a:
            for y in a:
                if x + y == numbers[i]:
                    found = True
                    break
            if found:
                break
        if not found:
            return numbers[i]


def run_part_2(numbers, goal):
    n = len(numbers)
    for length in range(2, n):
        for start in range(n - length):
            candidates = numbers[start:start + length]
            if sum(candidates) == goal:
                return min(candidates) + max(candidates)


if __name__ == '__main__':
    data = advent_tools.read_one_int_per_line()
    part1_result = run_part_1(data)
    print('Part 1:', part1_result)
    print('Part 2:', run_part_2(data, part1_result))