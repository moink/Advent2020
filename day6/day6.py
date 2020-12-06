import collections

import advent_tools


def process_input(groups):
    result = []
    for lines in groups:
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
    data = advent_tools.read_input_line_groups()
    data = process_input(data)
    print(run_part_1(data))
    print(run_part_2(data))