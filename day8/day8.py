import advent_tools


class HandheldComputer(advent_tools.Computer):
    operation = advent_tools.Computer.operation
    return_register = 'a'  # Needed for inheritance but not actually used

    def __init__(self):
        super().__init__()
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
                return True, self.acc
            if self.instruction_pointer in self.have_run:
                return False, self.acc
            self.have_run.add(self.instruction_pointer)
            self.run_instruction(line)
            self.instruction_pointer = self.instruction_pointer + 1


def run_part_1(program):
    computer = HandheldComputer()
    return computer.run_program(program)[1]


def run_part_2(program):
    for line_num, line in enumerate(program):
        if line.startswith('acc'):
            continue
        old_line = line
        if line.startswith('nop'):
            program[line_num] = old_line.replace('nop', 'jmp')
        if line.startswith('jmp'):
            program[line_num] = old_line.replace('jmp', 'nop')
        comp = HandheldComputer()
        finished, val = comp.run_program(program)
        if finished:
            return val
        program[line_num] = old_line
    return 'Failed'


if __name__ == '__main__':
    data = advent_tools.read_input_lines()
    print('Part 1:', run_part_1(data))
    print('Part 2:', run_part_2(data))