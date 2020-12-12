import copy
import numpy as np
from scipy import signal

import advent_tools


class SeatingSystem(advent_tools.PlottingGrid):
    convolve_matrix = np.asarray([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    walls_treated_as = 0

    @classmethod
    def seating_from_file(cls, char_map, part, plotting):

        new_grid = super().from_file(char_map)
        if part == 1:
            new_grid.count_fun = cls.count_neighbours_part_one
            new_grid.limit = 4
        else:
            new_grid.count_fun = cls.count_neighbours_part_two
            new_grid.limit = 5
        new_grid.plotting = plotting
        return new_grid

    def count_neighbours_part_one(self):
        """Count the number of neighbours each grid point has for part 1"""
        count = signal.convolve2d(self.grid == 1, self.convolve_matrix,
                                  mode='same', boundary='fill',
                                  fillvalue=self.walls_treated_as)
        return count

    def count_neighbours_part_two(self):
        """Count the number of neighbours each grid point has for part 2"""
        directions = [(0, 1), (-1, 1), (-1, 0), (-1, -1),
                      (0, -1), (1, -1), (1, 0), (1, 1)]
        count = np.zeros(self.grid.shape)
        for (y, x), _ in np.ndenumerate(self.grid):
            for direction in directions:
                count[y, x] += self.next_neighbour(y, x, direction)
        return count

    def next_neighbour(self, y, x, direction):
        del_y, del_x = direction
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
        counts = self.count_fun(self)
        self.evaluate_where_on(counts)
        if self.plotting:
            self.draw()

    def evaluate_where_on(self, counts):
        self.grid = np.where(np.logical_and(self.grid == 1,
                                            counts >= self.limit),
                             0, self.grid)
        self.grid = np.where(np.logical_and(self.grid == 0, counts == 0), 1,
                             self.grid)

    def run_until_stable(self):
        while True:
            old_grid = copy.deepcopy(self.grid)
            self.one_step()
            if (old_grid == self.grid).all().all():
                break
        if self.plotting:
            self.show()

    def count_ones(self):
        return sum(sum(self.grid == 1))


def run_part(part_num):
    seating = SeatingSystem.seating_from_file({'L': 0, '#': 1, '.': 2},
                                              part_num, True)
    seating.run_until_stable()
    return seating.count_ones()


if __name__ == '__main__':
    print('Part 1:', run_part(1))
    print('Part 2:', run_part(2))