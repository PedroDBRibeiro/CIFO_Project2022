from random import shuffle, choice, sample, random, randint
from sudoku_data.SudokuProblems import sudoku1
import numpy
from sudoku_data.sudokuHelper import *
from copy import deepcopy
from operator import attrgetter


def calculate_fitness(sudoku):
    row_idx, col_idx, box_idx = get_indices(base=3)

    repres = sudoku
    n_error = 0
    # count errors in rows
    for row in row_idx:
        n_error += count_duplicates([repres[r] for r in row])
    # count errors in cols
    for col in col_idx:
        n_error += count_duplicates([repres[c] for c in col])
    # count errors in box
    for box in box_idx:
        n_error += count_duplicates([repres[b] for b in box])

    # penalize deviation from initial puzzle
    if True:
        for pos, v in enumerate(sudoku):
            if repres[pos] != v and v != 0:
                n_error += 12

    # penalize sudokus that still have zeros
    # if True:
    # for pos, v in enumerate(sudoku):
    #  if v == 0:
    #   n_error += 5

    return n_error


def fill(sudoku):
    sudoku = sudoku
    for count, value in enumerate(sudoku):
        if value == 0:
            sudoku[count] = numpy.random.randint(1, 10)

    return sudoku


board_length = 9


class Individual:
    def __init__(
            self,
            sudoku
    ):
        self.sudoku = fill(sudoku)
        self.fitness = calculate_fitness(self.sudoku)

    def index(self, value):
        return self.sudoku.index(value)

    def __len__(self):
        return len(self.sudoku)

    def __getitem__(self, position):
        return self.sudoku[position]

    def __setitem__(self, position, value):
        self.sudoku[position] = value

    def __repr__(self):
        return f"Individual(Sudoku: {self.sudoku}, Fitness: {self.fitness})"


class Population:

    def __init__(self, size, optim, sudoku, **kwargs):
        self.individuals = []
        self.size = size
        self.optim = optim

        for _ in range(size):
            self.individuals.append(
                Individual(
                    sudoku=sudoku
                )
            )

    def evolve(self, gens, select, crossover, mutate, co_p, mu_p, elitism):
        for gen in range(gens):
            new_pop = []

            if elitism:
                if self.optim == "max":
                    elite = deepcopy(max(self.individuals, key=attrgetter("fitness")))
                elif self.optim == "min":
                    elite = deepcopy(min(self.individuals, key=attrgetter("fitness")))

            while len(new_pop) < self.size:
                parent1, parent2 = select(self), select(self)
                # Crossover
                if random() < co_p:
                    offspring1, offspring2 = crossover(parent1, parent2)
                else:
                    offspring1, offspring2 = parent1, parent2
                # Mutation
                if random() < mu_p:
                    offspring1 = mutate(offspring1)
                if random() < mu_p:
                    offspring2 = mutate(offspring2)

                new_pop.append(Individual(sudoku=offspring1))
                if len(new_pop) < self.size:
                    new_pop.append(Individual(sudoku=offspring2))

            if elitism:
                if self.optim == "max":
                    least = min(new_pop, key=attrgetter("fitness"))
                elif self.optim == "min":
                    least = max(new_pop, key=attrgetter("fitness"))
                new_pop.pop(new_pop.index(least))
                new_pop.append(elite)

            self.individuals = new_pop

            if self.optim == "max":
                print(f'Best Individual: {max(self, key=attrgetter("fitness"))}')
            elif self.optim == "min":
                print(f'Best Individual: {min(self, key=attrgetter("fitness"))}')

    def __len__(self):
        return len(self.individuals)

    def __getitem__(self, position):
        return self.individuals[position]

    def __repr__(self):
        return  # f"Population(size={len(self.individuals)}, individual_size={len(self.individuals[0])})"
