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
    groups = data.split('\n\n')
    result = []
    for group in groups:
        lines = group.splitlines()
        num_lines = len(lines)
        counts = collections.Counter(''.join(lines))
        result.append({'num': num_lines, 'counts': counts})
    return result


def run_part_1(groups):
    return sum(len(group['counts']) for group in groups)


def run_part_2(groups):
    return sum(count == group['num'] for group in groups
               for count in group['counts'].values())


if __name__ == '__main__':
    with open('input.txt') as in_file:
        data = in_file.read().strip()
    data = process_input(data)
    print(run_part_1(data))
    print(run_part_2(data))