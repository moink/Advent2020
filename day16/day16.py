import collections
import pandas as pd

import advent_tools


def main():
    data = advent_tools.read_input_line_groups()
    rules, my_ticket, other_tickets = parse_input(data)
    part1, valid_other_tickets = run_part_1(rules, other_tickets)
    print('Part 1:', part1)
    print('Part 2:', run_part_2(rules, valid_other_tickets, my_ticket))


def parse_input(data):
    rules = collections.defaultdict(list)
    for rule in data[0]:
        name, numbers = rule.split(':')
        for ran in numbers.split(' or '):
            low, high = ran.split('-')
            rules[name].append((int(low), int(high)))
    other_tickets = [parse_ticket(ticket)  for ticket in data[2][1:]]
    my_ticket = parse_ticket(data[1][1])
    return rules, my_ticket, other_tickets


def parse_ticket(ticket):
    return tuple(int(num) for num in ticket.split(','))


def run_part_1(rules, other_tickets):
    allowed_intervals = [interval for rule in rules.values()
                         for interval in rule]
    result = 0
    valid = set()
    for ticket in other_tickets:
        valid.add(ticket)
        for num in ticket:
            for low, high in allowed_intervals:
                if low <= int(num) <= high:
                    break
            else:
                result += int(num)
                valid.remove(ticket)
    return result, valid


def run_part_2(rules, valid_other_tickets, my_ticket):
    num_fields = len(rules)
    allowed = pd.DataFrame(columns=range(num_fields), index=rules.keys(),
                           data=True)
    for field_num in range(num_fields):
        for name, ((low1, high1), (low2, high2)) in rules.items():
            for ticket in valid_other_tickets:
                if (ticket[field_num] not in range(low1, high1 + 1)
                        and ticket[field_num] not in range(low2, high2 + 1)):
                    allowed.loc[name, field_num] = False
    result = 1
    while allowed.sum(axis=1).max() > 1:
        for name, row in allowed[allowed.sum(axis=1) == 1].iterrows():
            if name.startswith('departure'):
                result = result * my_ticket[row[row].index[0]]
            allowed.loc[:, row[row].index[0]] = False
    return result





if __name__ == '__main__':
    main()