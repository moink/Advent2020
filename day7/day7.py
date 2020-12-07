import collections


def run_part_1(lines):
    rules = collections.defaultdict(list)
    for line in lines:
        left, right = line.split(' contain ')
        holder = clean_colour(left)
        for contents in right.split(','):
            contained = clean_colour(contents[2:])
            rules[contained].append(holder)
    return len(list_all_holders(rules, 'shiny gold'))


def clean_colour(colour):
    return colour.replace(' bags', '').replace(' bag', '').replace('.', '').strip()


def list_all_holders(data, colour):
    result = set(data[colour])
    for col in data[colour]:
        result = result.union(list_all_holders(data, col))
    return result


def run_part_2(lines):
    rules = collections.defaultdict(list)
    for line in lines:
        left, right = line.split(' contain ')
        holder = clean_colour(left)
        for contents in right.split(','):
            contained = clean_colour(contents)
            rules[holder].append(contained)
    return count_contents(rules, 'shiny gold')


def count_contents(data, colour):
    if colour == 'other':
        return 0
    count = 0
    for cont in data[colour]:
        num_str = cont.split()[0]
        if num_str == 'no':
            num = 0
        else:
            num = int(num_str)
        col = cont.split(maxsplit=1)[1]
        count = count + num * (count_contents(data, col) + 1)
    return count


if __name__ == '__main__':
    with open('input.txt') as in_file:
        input_lines = in_file.read().strip().splitlines()
    print('Part 1:', run_part_1(input_lines))
    print('Part 2:', run_part_2(input_lines))
