import collections

import advent_tools


def process_input(data):
    result = collections.defaultdict(list)
    for key, val in data.items():
        for contents in val.split(','):
            colour = contents[2:].replace(' bags','').replace(' bag', '').replace('.', '').strip()
            holder = key.replace(' bags','').replace(' bag', '').replace('.', '').strip()
            result[colour].append(holder)
    return result


def list_all_holders(data, colour):
    result = set(data[colour])
    for col in data[colour]:
        result = result.union(list_all_holders(data, col))
    return result


def run_part_1():
    data = advent_tools.read_dict_from_input_file(sep=' contain ', key='left')
    rules = collections.defaultdict(list)
    for key, val in data.items():
        holder = key.replace(' bags', '').replace(' bag', '').replace('.', '').strip()
        for contents in val.split(','):
            colour = contents[2:].replace(' bags', '').replace(' bag', '').replace('.', '').strip()
            rules[colour].append(holder)
    return len(list_all_holders(rules, 'shiny gold'))


def count_contents(data, colour):
    if colour == 'other':
        return 0
    count = 0
    for cont in data[colour]:
        numstr = cont.split()[0]
        if numstr == 'no':
            num = 0
        else:
            num = int(numstr)
        col = cont.split(maxsplit=1)[1]
        count = count + num * (count_contents(data, col) + 1)
    return count


def run_part_2():
    data = advent_tools.read_dict_from_input_file(sep=' contain ', key='right')
    result = collections.defaultdict(list)
    for key, val in data.items():
        colour = val.replace(' bags', '').replace(' bag', '').replace('.', '').strip()
        for contents in key.split(','):
            holder = contents.replace(' bags', '').replace(' bag', '').replace('.', '').strip()
            result[colour].append(holder)
    return count_contents(result, 'shiny gold')


if __name__ == '__main__':
    print('Part 1:', run_part_1())
    print('Part 2:', run_part_2())