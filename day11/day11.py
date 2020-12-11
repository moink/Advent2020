import contextlib
import collections
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
    """Implementation of Conway's Game Of Life

    Works as is - you are most likely to want to change
    self.convolve_matrix, or walls_treated_as, or to overwrite
    evaluate_where_on

    In 2015 day 18 part 2 I also had to change read_input_file (inherited
    from PlottingGrid) to turn the corner lights on initially (they were
    stuck on in the problem description).
    """
    # This is all eight neighbours
    convolve_matrix = np.asarray([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    # If you wanted just four neighbours, do instead:
    # convolve_matrix = np.asarray([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    walls_treated_as = 0

    def count_neighbours_part_one(self):
        """Count the number of neighbours each grid point has"""
        count = signal.convolve2d(self.grid == 1, self.convolve_matrix,
                                  mode='same', boundary='fill',
                                  fillvalue=self.walls_treated_as)
        return count

    def count_neighbours_part_two(self):
        """Count the number of neighbours each grid point has"""
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



    def one_step(self):
        """Take one game of life step"""
        counts = self.count_neighbours_part_two()
        self.evaluate_where_on(counts)
        self.draw()

    def evaluate_where_on(self, counts):
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
                                            counts >= 5), 0, self.grid)
        # For grid points that are off, if count is 3, turn on
        # Otherwise keep the same as grid calculated in previous step
        self.grid = np.where(np.logical_and(self.grid == 0, counts == 0), 1,
                             self.grid)
        # print('')

    def simulate_n_steps(self):
        """Take a defined number of steps of the Game of Life

        Args:
            num_steps: int
                Number of steps to take

        Returns:
            None
        """
        while True:
            old_grid = copy.deepcopy(self.grid)
            self.one_step()
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
    # g.show()
    g.simulate_n_steps()
    return g.count_ones()


def run_part_2():
    g = GameOfLife.from_file({'L': 0, '#': 1, '.': 2})
    g.simulate_n_steps()
    return g.count_ones()


if __name__ == '__main__':
    print('Part 1:', run_part_1())
    print('Part 2:', run_part_2())