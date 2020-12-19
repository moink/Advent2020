import collections

import advent_tools


def main():
    # advent_tools.TESTING = True
    data = advent_tools.read_input_line_groups()
    print('Part 1:', run_part_1(data[0], data[1]))
    print('Part 2:', run_part_2(data[0], data[1]))


def process_rules(data):
    rules = collections.defaultdict(list)
    for line in data:
        left, right = line.split(':')
        for sp in right.split('|'):
            try:
                rule = [int(num) for num in sp.split()]
            except ValueError:
                rule = sp.replace('"', '').strip()
            rules[int(left)].append(rule)
    return dict(rules)


def run_part_1(rules, messages):
    rules = process_rules(rules)
    return sum(check_rule(message, rules) for message in messages)


def run_part_2(rules, messages):
    rules = rules + ['8: 42 | 42 8', '11: 42 31 | 42 11 31']
    rules = process_rules(rules)
    return sum(check_rule(message, rules) for message in messages)


def check_rule(message, rules):
    return '' in calc_remainders(message, 0, rules)


def calc_remainders(message, rule_num, rules):
    cur_rule = rules[rule_num]
    if len(cur_rule) == 1 and isinstance(cur_rule[0], str):
        if message.startswith(cur_rule[0]):
            yield message[1:]
    else:
        for option in cur_rule:
            rems = [message]
            for num in option:
                next_rems = [r for rem in rems
                             for r in calc_remainders(rem, num, rules)]
                rems = next_rems
            for rem in rems:
                yield rem


if __name__ == '__main__':
    main()