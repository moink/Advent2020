import advent_tools


def main():
    num_steps = 6
    for part in (1, 2):
        gol = advent_tools.GameOfLife.from_file({'.': 0, '#': 1},
                                                dimension=part + 2,
                                                padding=num_steps + 1)
        gol.simulate_n_steps(6)
        print(f'Part {part}: {gol.sum()}')


if __name__ == '__main__':
    main()