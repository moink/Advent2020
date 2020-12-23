import contextlib
import collections
import copy
import functools
import itertools
import math
import numpy as np
import pandas as pd
import re

import advent_tools


def main():
    advent_tools.TESTING = True
    # data = advent_tools.read_all_integers()
    # data = advent_tools.read_whole_input()
    # data = advent_tools.read_input_lines()
    # data = advent_tools.read_input_no_strip()
    # data = advent_tools.read_dict_from_input_file(sep=' => ', key='left')
    # data = advent_tools.read_dict_of_list_from_file(sep=' => ', key='left')
    # data = advent_tools.read_one_int_per_line()
    # data = advent_tools.PlottingGrid.from_file({'.' : 0, '#' : 1})
    # data = advent_tools.read_input_line_groups()
    # data = process_input(data)
    print('Part 1:', run_part_1())
    # print('Part 2:', run_part_2(data))


def process_input(data):
    print(data)
    return data


def run_part_1():
    data = '219748365'
    moves = 100
    # data = '389125467'
    # moves = 10
    data = data.replace('9', '0')
    cll = advent_tools.CircularLinkedList()
    cll.head.data = int(data[0])
    for char in data[1:]:
        cll.add_node_after_current(int(char))
    cll.move_clockwise(1)
    for move in range(1, moves + 1):
        # print(f'\n-- move {move} --')
        # print('cups: ', cll)
        cc_label = cll.get_current()
        dest_cup = (cc_label - 1) % 9
        picked_up = []
        prev_current = cll.current
        cll.move_clockwise(1)
        for pick_up in range(3):
            picked_up.append(cll.get_current())
            cll.remove_current_node()
        # print('pick up: ', picked_up)
        # print('k', cll)
        while dest_cup in picked_up:
            dest_cup = (dest_cup - 1) % 9
        # print('m', cll)
        # print('destination', dest_cup)
        while cc_label!= dest_cup:
            cll.move_clockwise(1)
            cc_label = cll.get_current()
        for p in picked_up:
            cll.add_node_after_current(p)
        while cll.current != prev_current:
            cll.move_clockwise(1)
        # print('x', cll)
        cll.move_clockwise(1)
        # print('z', cll)
    while cll.get_current() != 1:
        cll.move_clockwise(1)
    result = []
    for _ in range(len(data) - 1):
        cll.move_clockwise(1)
        result.append(str(cll.get_current()))
    return ''.join(result).replace('0', '9')


def run_part_2(data):
    pass


if __name__ == '__main__':
    main()