import collections

import advent_tools


def main():
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
    return sum('' in check_rule(message, 0, rules) for message in messages)


def run_part_2(rules, messages):
    rules = rules + ['8: 42 | 42 8', '11: 42 31 | 42 11 31']
    rules = process_rules(rules)
    return sum('' in check_rule(message, 0, rules) for message in messages)


def check_rule(message, rule_num, rules):
    for option in rules[rule_num]:
        if isinstance(option, str):
            if message.startswith(option):
                yield message[1:]
            continue
        rems = (message,)
        for num in option:
            all_rems = []
            for rem in rems:
                for r in check_rule(rem, num, rules):
                    all_rems.append(r)
            rems = tuple(all_rems)
        for rem in rems:
            yield rem


if __name__ == '__main__':
    main()