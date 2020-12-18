import itertools

import advent_tools


def main():
    data = advent_tools.read_input_lines()
    print('Part 1:', sum(evaluate_expression(line, rules_part1)
                         for line in data))
    print('Part 2:', sum(evaluate_expression(line, rules_part2)
                         for line in data))


def evaluate_expression(line, rule_set):
    if '(' not in line:
        return rule_set(line)
    inside, outside = advent_tools.get_inside_outside_brackets(line, '(', ')')
    inside_vals = [str(evaluate_expression(inside_expr, rule_set))
                   for inside_expr in inside]
    if line.startswith('('):
        terms = itertools.zip_longest(inside_vals, outside)
    else:
        terms = itertools.zip_longest(outside, inside_vals)
    expr = ''.join(term for term in (itertools.chain.from_iterable(terms))
                   if term is not None)
    return evaluate_expression(expr, rule_set)


def rules_part1(expr):
    tokens = iter(expr.split())
    val = int(next(tokens))
    while True:
        try:
            symbol = next(tokens)
        except StopIteration:
            break
        right = int(next(tokens))
        if symbol == '+':
            val = val + right
        elif symbol == '*':
            val = val * right
        else:
            raise RuntimeError(f'Bad operator "{symbol}"')
    return val


def rules_part2(expr):
    if '+' not in expr:
        return eval(expr)
    if '+' in expr and '*' not in expr:
        return eval(expr)
    left, right = expr.split('*', 1)
    return rules_part2(left) * rules_part2(right)


if __name__ == '__main__':
    main()