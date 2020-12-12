import advent_tools

NORTH = (0, -1)
SOUTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)


def process_input(lines):
    return [(line[0], int(line[1:])) for line in lines]


def move(loc, direction, count):
    x, y = loc
    del_x, del_y = direction
    return x + count * del_x, y + count * del_y


def turn_right(cur_dir, count):
    next_dir = {NORTH: EAST, SOUTH: WEST, EAST: SOUTH, WEST: NORTH}
    for _ in range(count//90):
        cur_dir = next_dir[cur_dir]
    return cur_dir


def turn_left(cur_dir, count):
    next_dir = {NORTH: WEST, SOUTH: EAST, EAST: NORTH, WEST: SOUTH}
    for _ in range(count//90):
        cur_dir = next_dir[cur_dir]
    return cur_dir


def run_part_1(instructions):
    cur_dir = EAST
    cur_loc = (0, 0)
    for action, count in instructions:
        if action == 'N':
            cur_loc = move(cur_loc, NORTH, count)
        elif action == 'S':
            cur_loc = move(cur_loc, SOUTH, count)
        elif action == 'E':
            cur_loc = move(cur_loc, EAST, count)
        elif action == 'W':
            cur_loc = move(cur_loc, WEST, count)
        elif action == 'F':
            cur_loc = move(cur_loc, cur_dir, count)
        elif action == 'R':
            cur_dir = turn_right(cur_dir, count)
        elif action == 'L':
            cur_dir = turn_left(cur_dir, count)
    return sum(cur_loc)


def get_quadrant(point):
    x, y = point
    if y > 0:
        if x > 0:
            return 3
        else:
            return 2
    else:
        if x < 0:
            return 1
        else:
            return 0


def set_quadrant(point, quadrant):
    x, y = point
    x = abs(x)
    y = abs(y)
    if quadrant == 0:
        return x, -y
    elif quadrant == 1:
        return -x, -y
    elif quadrant == 2:
        return -x, y
    else:
        return x, y


def rotate_waypoint_right(waypoint, count):
    quadrant = get_quadrant(waypoint)
    x, y = waypoint
    for _ in range(count//90):
        quadrant = (quadrant - 1) % 4
        x, y = y, x
    return set_quadrant((x, y), quadrant)


def rotate_waypoint_left(waypoint, count):
    quadrant = get_quadrant(waypoint)
    x, y = waypoint
    for _ in range(count // 90):
        quadrant = (quadrant + 1) % 4
        x, y = y, x
    return set_quadrant((x, y), quadrant)


def run_part_2(instructions):
    waypoint = (10, -1)
    cur_loc = (0, 0)
    for action, count in instructions:
        if action == 'N':
            waypoint = move(waypoint, NORTH, count)
        elif action == 'S':
            waypoint = move(waypoint, SOUTH, count)
        elif action == 'E':
            waypoint = move(waypoint, EAST, count)
        elif action == 'W':
            waypoint = move(waypoint, WEST, count)
        elif action == 'F':
            cur_loc = move(cur_loc, waypoint, count)
        elif action == 'R':
            waypoint = rotate_waypoint_right(waypoint, count)
        elif action == 'L':
            waypoint = rotate_waypoint_left(waypoint, count)
    return sum(abs(m) for m in cur_loc)


if __name__ == '__main__':
    data = advent_tools.read_input_lines()
    data = process_input(data)
    print('Part 1:', run_part_1(data))
    print('Part 2:', run_part_2(data))