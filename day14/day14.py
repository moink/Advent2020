import collections
import itertools

import advent_tools


def parse_instructions(lines):
    result = []
    for line in lines:
        left, right = line.split(' = ')
        if left == 'mask':
            result.append(('mask', right))
        else:
            num = int(advent_tools.get_inside_outside_brackets(left, '[', ']',
                                                               False)[0][0])
            result.append(('mem', num, int(right)))
    return result


def run_part_1(instructions):
    memory = collections.defaultdict(int)
    for inst in instructions:
        if inst[0] == 'mask':
            bitmask = {}
            for i, char in enumerate(inst[1]):
                if char != 'X':
                    bitmask[i] = char
        else:
            num_str = "{0:b}".format(inst[2]).zfill(36)
            to_write = ''
            for i, char in enumerate(num_str):
                try:
                    to_write = to_write + bitmask[i]
                except KeyError:
                    to_write = to_write + char
            memory[inst[1]] = int(to_write, 2)
    return sum(memory.values())


def run_part_2(instructions):
    memory = collections.defaultdict(int)
    ones = []
    floating = []
    for inst in instructions:
        if inst[0] == 'mask':
            ones = [i for i, char in enumerate(inst[1]) if char == '1']
            floating = [i for i, char in enumerate(inst[1]) if char == 'X']
        else:
            bits = list("{0:b}".format(inst[1]).zfill(36))
            memory_locations = set()
            for pos in ones:
                bits[pos] = '1'
            for bit_vals in itertools.product(('0', '1'), repeat=len(floating)):
                for pos, bit_val in zip(floating, bit_vals):
                    bits[pos] = bit_val
                    memory_locations.add(int(''.join(bits), 2))
            for mem_loc in memory_locations:
                memory[mem_loc] = inst[2]
    return sum(memory.values())


if __name__ == '__main__':
    data = advent_tools.read_input_lines()
    data = parse_instructions(data)
    print('Part 1:', run_part_1(data))
    print('Part 2:', run_part_2(data))