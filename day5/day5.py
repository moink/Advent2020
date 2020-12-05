import itertools


def get_seat_id(line):
    char_map = {'B': '1', 'F': '0', 'L': '0', 'R': '1'}
    binary = ''.join(char_map[char] for char in line)
    return int(binary, 2)


def run_part_1(seats):
    return max(seats)


def run_part_2(seats):
    for seat_num in itertools.count(min(seats)):
        if seat_num not in seats:
            return seat_num


if __name__ == '__main__':
    with open('input.txt') as in_file:
        data = in_file.read().strip().splitlines()
    all_seats = {get_seat_id(line) for line in data}
    print(run_part_1(all_seats))
    print(run_part_2(all_seats))
