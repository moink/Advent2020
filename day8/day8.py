import copy

import advent_tools


class HandheldComputer(advent_tools.Computer):
    operation = advent_tools.Computer.operation
    return_register = 'a'  # Needed for inheritance but not actually used

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
        while True:
            try:
                line = program[self.instruction_pointer]
            except IndexError:
                return ('Finished', self.acc)
            if self.instruction_pointer in self.have_run:
                return ('Infinite', self.acc)
            self.have_run.add(self.instruction_pointer)
            self.run_instruction(line)
            self.instruction_pointer = self.instruction_pointer + 1


def run_part_1(data):
    computer = HandheldComputer()
    return computer.run_program(data)[1]


def run_part_2(data):
    nop_lines = [i for i, line in enumerate(data) if line.startswith('nop')]
    jmp_lines = [i for i, line in enumerate(data) if line.startswith('jmp')]
    for line_num in nop_lines:
        prog = copy.deepcopy(data)
        prog[line_num] = prog[line_num].replace('nop', 'jmp')
        comp = HandheldComputer()
        fin, val = comp.run_program(prog)
        if fin == 'Finished':
            return val
    for line_num in jmp_lines:
        prog = copy.deepcopy(data)
        prog[line_num] = prog[line_num].replace('jmp', 'nop')
        comp = HandheldComputer()
        fin, val = comp.run_program(prog)
        if fin == 'Finished':
            return val
    return 'Failed'

if __name__ == '__main__':
    data = advent_tools.read_input_lines()
    print('Part 1:', run_part_1(data))
    print('Part 2:', run_part_2(data))