
import numpy
import random

import Parameters
from Individual import Individual

random.seed()

# Number of digits (in the case of standard Sudoku puzzles, this is 9).
board_size = 9


class Crossover(object):
    def __init__(self):
        return

    def crossover(self, parent1, parent2, crossover_rate, number_of_cutoff_points=2):
        """ Create two new child candidates by crossing over parent genes. """
        cutoff_points = []

        child1 = Individual()
        child2 = Individual()

        # Make a copy of the parent genes.
        child1.values = numpy.copy(parent1.values)
        child2.values = numpy.copy(parent2.values)

        r = random.uniform(0, 1.1)
        while(r > 1):  # Outside [0, 1] boundary. Choose another.
            r = random.uniform(0, 1.1)

        # Perform crossover.
        if r < Parameters.crossover_rate:
            # Pick a crossover point. Crossover must have at least 1 row (and at most Nd-1) rows.
            for i in range(number_of_cutoff_points):
                cutoff_points.append(random.randint(0, 8))

            # retry if  crossover poits are equal
            while(len(set(cutoff_points)) != len(cutoff_points)):
                for i in range(number_of_cutoff_points):
                    cutoff_points[i] = random.randint(0, 8)

            for i in cutoff_points:
                child1.values[i], child2.values[i] = self.crossover_rows(
                    child1.values[i], child2.values[i])

        return child1, child2

    def crossover_rows(self, row1, row2):
        child_row1 = numpy.zeros(board_size)
        child_row2 = numpy.zeros(board_size)

        remaining = list(range(1, board_size+1))
        cycle = 0

        # While child rows not complete...
        while((0 in child_row1) and (0 in child_row2)):
            if(cycle % 2 == 0):  # Even cycles.
                # Assign next unused value.
                index = self.find_unused(row1, remaining)
                start = row1[index]
                remaining.remove(row1[index])
                child_row1[index] = row1[index]
                child_row2[index] = row2[index]
                next = row2[index]

                while(next != start):  # While cycle not done...
                    index = self.find_value(row1, next)
                    child_row1[index] = row1[index]
                    remaining.remove(row1[index])
                    child_row2[index] = row2[index]
                    next = row2[index]

                cycle += 1

            else:  # Odd cycle - flip values.
                index = self.find_unused(row1, remaining)
                start = row1[index]
                remaining.remove(row1[index])
                child_row1[index] = row2[index]
                child_row2[index] = row1[index]
                next = row2[index]

                while(next != start):  # While cycle not done...
                    index = self.find_value(row1, next)
                    child_row1[index] = row2[index]
                    remaining.remove(row1[index])
                    child_row2[index] = row1[index]
                    next = row2[index]

                cycle += 1

        return child_row1, child_row2

    def find_unused(self, parent_row, remaining):
        for i in range(0, len(parent_row)):
            if(parent_row[i] in remaining):
                return i

    def find_value(self, parent_row, value):
        for i in range(0, len(parent_row)):
            if(parent_row[i] == value):
                return i
