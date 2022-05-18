from random import shuffle, choice, sample, random, randint
import numpy as np
from copy import deepcopy
from operator import attrgetter


class Individual:
    def __init__(
            self,
            sudoku,
    ):

        self.sudoku = sudoku
        self.fitness_score = 0
        self.fitness = self.calculate_fitness(self.sudoku)

    def calculate_fitness(self, sudoku):
        self.row_evaluation(sudoku)
        self.column_evaluation(sudoku)
        self.block_evaluation(sudoku)
        return self.fitness_score

    def row_evaluation(self, sudoku):
        min_current_index = 0
        max_current_index = 9

        while max_current_index <= len(sudoku):
            row = set(sudoku[min_current_index:max_current_index])
            self.fitness_score += 9 - len(row)

            min_current_index += 9
            max_current_index += 9

    def column_evaluation(self, sudoku):
        columns = [0, 9, 18, 27, 36, 45, 54, 63, 72]

        for i in range(9):
            column = set([sudoku[index] for index in columns])
            self.fitness_score += 9 - len(column)
            columns = [x + 1 for x in columns]

    def block_evaluation(self, sudoku):
        blocks = [0, 1, 2, 9, 10, 11, 54, 63, 72]

        for i in range(9):
            block = set([sudoku[index] for index in blocks])
            self.fitness_score += 9 - len(block)
            blocks = [x + 1 for x in blocks]

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
        return f"Population(size={len(self.individuals)}, individual_size={len(self.individuals[0])})"
