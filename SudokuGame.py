import numpy
import random

from Individual import Individual
from Crossover import Crossover
from Given import Given
from Population import Population
from Selection import pick_selection_algorithm
from Maximization import better
import Parameters


class SudokuGame(object):

    def __init__(self, population_size, generations, mutation_rate):
        self.given = None
        self.population_size = population_size  # Number of individuals
        # Number of better individuals to consider for crossover.
        self.number_best_individuals = int(0.05 * population_size)
        self.generations = generations
        self.mutation_rate = mutation_rate
        return

    def load(self, board):
        self.given = Given(numpy.reshape(board, (Parameters.board_length, Parameters.board_length)))
        return

    def print_solution(self,  solution):
        return print(str(solution))

    def play(self):

        # Create an initial population.
        self.population = Population()
        self.population.seed(self.population_size, self.given)

        # For up to 10000 generations...
        stale = 0
        for generation in range(0, self.generations):

            print("Generation %d" % generation)

            # Check for a solution.
            best_fitness = 0.0
            for c in range(0, self.population_size):
                fitness = self.population.individuals[c].fitness
                if Parameters.is_maximization and fitness == 1:
                    print("Solution found at generation %d!" % generation)
                    print(self.population.individuals[c].values)
                    return self.population.individuals[c]

                # Find the best fitness.
                if (fitness > best_fitness):
                    best_fitness = fitness

            print("Best fitness: %f" % best_fitness)

            # Create the next population.
            next_population = []

            # Select the individuals with better fitness
            self.population.sort()
            best_individuals = []
            for e in range(0, self.number_best_individuals):
                elite = Individual()
                elite.values = numpy.copy(
                    self.population.individuals[e].values)
                best_individuals.append(elite)

            # Create the rest of the candidates.
            for _ in range(self.number_best_individuals, self.population_size, 2):
                # Select parents from population via the picked selection algorithm.
                selection_algorithm = pick_selection_algorithm(Parameters.selection_algorithm)
                
                parent1 = selection_algorithm.select(self.population.individuals)
                parent2 = selection_algorithm.select(self.population.individuals)

                # Cross-over.
                c = Crossover()
                child1, child2 = c.crossover(
                    parent1, parent2, crossover_rate=1.0)

                child1.mutate(self.mutation_rate, self.given)
                child1.update_fitness()

                child2.mutate(self.mutation_rate, self.given)
                child2.update_fitness()

                # Add children to new population.
                next_population.append(child1)
                next_population.append(child2)

            # Append elites onto the end of the population. These will not have been affected by crossover or mutation.
            for e in range(0, self.number_best_individuals):
                next_population.append(best_individuals[e])

            # Select next generation.
            self.population.individuals = next_population
            self.population.update_fitness()

            # Check for stale population.
            self.population.sort()
            if (self.population.individuals[0].fitness != self.population.individuals[1].fitness):
                stale = 0
            else:
                stale += 1

            # Re-seed the population if 100 generations have passed with the fittest two candidates always having the same fitness.
            if (stale >= 100):
                print("The population has gone stale. Re-seeding...")
                self.population.seed(self.population_size, self.given)
                stale = 0
                self.mutation_rate = 0.06

        print("No solution found.")
        return None
