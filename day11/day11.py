import copy
import functools
import itertools
import math
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import re
from scipy import signal

import advent_tools


class GameOfLife(advent_tools.PlottingGrid):
    convolve_matrix = np.asarray([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    walls_treated_as = 0

    def count_neighbours_part_one(self):
        """Count the number of neighbours each grid point has for part 1"""
        count = signal.convolve2d(self.grid == 1, self.convolve_matrix,
                                  mode='same', boundary='fill',
                                  fillvalue=self.walls_treated_as)
        return count

    def count_neighbours_part_two(self):
        """Count the number of neighbours each grid point has for part 2"""
        directions = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
        count = np.zeros(self.grid.shape)
        for (y, x), _ in np.ndenumerate(self.grid):
            for dir in directions:
                count[y, x] = count[y, x] + self.next_neighbour(y, x, dir)
        return count

    def next_neighbour(self, y, x, dir):
        del_y, del_x = dir
        while True:
            y = y + del_y
            x = x + del_x
            if y >= 0 and x >= 0:
                try:
                    val = self.grid[y, x]
                except IndexError:
                    return 0
                if val < 2:
                    return val
            else:
                return 0

    def one_step(self, count_fun, limit):
        """Take one game of life step"""
        counts = count_fun()
        self.evaluate_where_on(counts, limit)
        self.draw()

    def evaluate_where_on(self, counts, limit):
        """Set the grid to the right setting based on the neighbour count

        Args:
            counts: np.ndarray
                Number of neighbours of each node that are on

        Returns:
            None
        """
        # For grid points that are on, if count is 2 or 3, keep on
        # Otherwise turn off
        # old_grid = copy.deepcopy(self.grid)
        self.grid = np.where(np.logical_and(self.grid == 1,
                                            counts >= limit), 0, self.grid)
        # For grid points that are off, if count is 3, turn on
        # Otherwise keep the same as grid calculated in previous step
        self.grid = np.where(np.logical_and(self.grid == 0, counts == 0), 1,
                             self.grid)
        # print('')

    def simulate_n_steps(self, count_fun, limit):
        """Take a defined number of steps of the Game of Life

        Args:
            num_steps: int
                Number of steps to take

        Returns:
            None
        """
        while True:
            old_grid = copy.deepcopy(self.grid)
            self.one_step(count_fun, limit)
            if (old_grid == self.grid).all().all():
                break
        self.draw()

    def count_ones(self):
        return sum(sum(self.grid == 1))




def process_input(data):
    print(data)
    return data

def run_part_1():
    g = GameOfLife.from_file({'L': 0, '#': 1, '.':2})
    g.simulate_n_steps(g.count_neighbours_part_one, 4)
    return g.count_ones()


def run_part_2():
    g = GameOfLife.from_file({'L': 0, '#': 1, '.': 2})
    g.simulate_n_steps(g.count_neighbours_part_two, 5)
    return g.count_ones()


if __name__ == '__main__':
    print('Part 1:', run_part_1())
    print('Part 2:', run_part_2())