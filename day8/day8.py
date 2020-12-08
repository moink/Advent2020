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


class MyComputer(advent_tools.Computer):
    operation = advent_tools.Computer.operation
    return_register = 'a'

    def __init__(self):
        self.instruction_pointer = 0
        self.acc = 0
        self.have_run = set()

    @operation('nop')
    def no_op(self, arg):
        pass

    @operation('acc')
    def accum(self, arg):
        self.acc += int(arg)

    @operation('jmp')
    def jump(self, arg):
        self.instruction_pointer += int(arg) - 1

    def run_program(self, program):
        """Run a list of instructions through the virtual machine

        The program terminates when the instruction pointer moves past the
        end of the program

        Args:
            program: [str]
                Instructions, each of which starts with a valid operation
                identifier
        Returns:
            int
                Contents of the return register when the program terminates
        """
        while True:
            try:
                line = program[self.instruction_pointer]
            except IndexError:
                return self.registers[self.return_register]
            if self.instruction_pointer in self.have_run:
                return self.acc
            self.have_run.add(self.instruction_pointer)
            self.run_instruction(line)
            self.instruction_pointer = self.instruction_pointer + 1

def run_part_1(data):
    computer = MyComputer()
    return computer.run_program(data)

def run_part_2(data):
    pass


if __name__ == '__main__':
    # advent_tools.TESTING = True
    # data = advent_tools.read_all_integers()
    # data = advent_tools.read_whole_input()
    data = advent_tools.read_input_lines()
    # data = advent_tools.read_input_no_strip()
    # data = advent_tools.read_dict_from_input_file(sep=' => ', key='left')
    # data = advent_tools.read_dict_of_list_from_file(sep=' => ', key='left')
    # data = advent_tools.read_one_int_per_line()
    # data = advent_tools.PlottingGrid.from_file({'.' : 0, '#' : 1})
    # data = advent_tools.read_input_line_groups()
    # data = process_input(data)
    print('Part 1:', run_part_1(data))
    # print('Part 2:', run_part_2(data))