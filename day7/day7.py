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
    result = collections.defaultdict(list)
    for key, val in data.items():
        for contents in val.split(','):
            colour = contents[2:].replace(' bags','').replace(' bag', '').replace('.', '').strip()
            holder = key.replace(' bags','').replace(' bag', '').replace('.', '').strip()
            result[colour].append(holder)
    print(result)
    return result

def list_all_holders(data, colour):
    result = set(data[colour])
    for col in data[colour]:
        result = result.union(list_all_holders(data, col))
    return result

def run_part_1(data):
    return len(list_all_holders(data, 'shiny gold'))


def run_part_2(data):
    pass


if __name__ == '__main__':
    # advent_tools.TESTING = True
    # data = advent_tools.read_all_integers()
    # data = advent_tools.read_whole_input()
    # data = advent_tools.read_input_lines()
    # data = advent_tools.read_input_no_strip()
    data = advent_tools.read_dict_from_input_file(sep=' contain ', key='left')
    # data = advent_tools.read_dict_of_list_from_file(sep=' => ', key='left')
    # data = advent_tools.read_one_int_per_line()
    # data = advent_tools.PlottingGrid.from_file({'.' : 0, '#' : 1})
    # data = advent_tools.read_input_line_groups()
    data = process_input(data)
    print('Part 1:', run_part_1(data))
    print('Part 2:', run_part_2(data))