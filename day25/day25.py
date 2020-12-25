import itertools

import advent_tools


def main():
    door_key, card_key = (int(line) for line in advent_tools.read_input_lines())
    print('Part 1:', run_part_1(door_key, card_key))


def run_part_1(door_key, card_key):
    initial_subject = 7
    modulus_base = 20201227
    for exponent in itertools.count():
        if pow(initial_subject, exponent, modulus_base) == door_key:
            return pow(card_key, exponent, modulus_base)


if __name__ == '__main__':
    main()