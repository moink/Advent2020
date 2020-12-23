import advent_tools


def main():
    data = advent_tools.read_whole_input()
    print('Part 1:', run_part_1(data))
    print('Part 2:', run_part_2(data))


def run_part_1(data):
    cups = [int(char) for char in data]
    cll = run_game(cups, 100)
    result = []
    for _ in range(len(cups) - 1):
        cll.move_clockwise(1)
        result.append(str(cll.get_current()))
    return ''.join(result).replace('0', '9')


def run_part_2(data):
    moves = 10000000
    cups = [int(char) for char in data]
    cups = cups + list(range(10, 1000001))
    cll = run_game(cups, moves)
    cll.move_clockwise(1)
    result1 = cll.get_current()
    cll.move_clockwise(1)
    result2 = cll.get_current()
    return result1 * result2


def run_game(data, moves, verbose=False):
    cll = advent_tools.CircularLinkedList(data[0])
    for char in data[1:]:
        cll.add_node_after_current(int(char))
    cll.move_clockwise(1)
    for move in range(1, moves + 1):
        print_if_condition(f'\n-- move {move} --', move % 1000000 == 0 or verbose)
        print_if_condition('cups: {cll}', verbose)
        cc_label = cll.get_current()
        dest_cup = (cc_label - 1) % len(data)
        if dest_cup == 0:
            dest_cup = max(data)
        picked_up = []
        prev_current = cll.current
        cll.move_clockwise(1)
        for pick_up in range(3):
            picked_up.append(cll.get_current())
            cll.remove_current_node()
        print_if_condition(f'pick up: {picked_up}', verbose)
        while dest_cup in picked_up:
            dest_cup = (dest_cup - 1) % len(data)
            if dest_cup == 0:
                dest_cup = max(data)
        print_if_condition(f'destination {dest_cup}', verbose)
        cll.set_current_to_data(dest_cup)
        for p in picked_up:
            cll.add_node_after_current(p)
        cll.current = prev_current
        cll.move_clockwise(1)
    cll.set_current_to_data(1)
    return cll


def print_if_condition(message, verbose):
    if verbose:
        print(message)


if __name__ == '__main__':
    main()