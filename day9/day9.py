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


def process_input(data):
    print(data)
    return data

def run_part_1(data):
    length = 25
    for i in range(length, len(data) - 2):
        found = False
        a = data[i-length:i]
        for x in a:
            for y in a:
                if x + y == data[i]:
                    found = True
        if not found:
            return data[i]


def run_part_2(data):
    goal = 177777905
    # goal = 127
    n = len(data)
    for length in range(2, n):
        for start in range(n - length):
            p = data[start:start+length]
            if sum(p) == goal:
                return min(p) + max(p)


if __name__ == '__main__':
    # advent_tools.TESTING = True
    # data = advent_tools.read_all_integers()
    # data = advent_tools.read_whole_input()
    # data = advent_tools.read_input_lines()
    # data = advent_tools.read_input_no_strip()
    # data = advent_tools.read_dict_from_input_file(sep=' => ', key='left')
    # data = advent_tools.read_dict_of_list_from_file(sep=' => ', key='left')
    data = advent_tools.read_one_int_per_line()
    # data = advent_tools.PlottingGrid.from_file({'.' : 0, '#' : 1})
    # data = advent_tools.read_input_line_groups()
    data = process_input(data)
    # print('Part 1:', run_part_1(data))
    print('Part 2:', run_part_2(data))