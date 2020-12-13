import contextlib
import itertools

import advent_tools


def run_part_1(bus_data):
    start_time = int(bus_data[0])
    buses = []
    for bus_info in bus_data[1].split(','):
        with contextlib.suppress(ValueError):
            buses.append(int(bus_info))
    for cur_time in itertools.count(start_time):
        for bus_id in buses:
            if cur_time % bus_id == 0:
                return bus_id * (cur_time - start_time)


def calc_moduli(bus_times):
    buses = bus_times.split(',')
    moduli = {int(buses[0]): 0}
    for time_delta, bus_id_str in enumerate(buses[1:], 1):
        with contextlib.suppress(ValueError):
            bus_id = int(bus_id_str)
            moduli[bus_id] = (bus_id - time_delta) % bus_id
    return moduli


def run_part_2(bus_data):
    moduli = calc_moduli(bus_data[1])
    divisors = sorted(moduli.keys(), reverse=True)
    to_check = moduli[divisors[0]]
    step_size = divisors[0]
    for divisor in divisors[1:]:
        while to_check % divisor != moduli[divisor]:
            to_check = to_check + step_size
        step_size = step_size * divisor
    return to_check


if __name__ == '__main__':
    data = advent_tools.read_input_lines()
    print('Part 1:', run_part_1(data))
    print('Part 2:', run_part_2(data))
