import numpy
import random

from Individual import Individual
from Crossover import Crossover
from Given import Given
from Population import Population
from Selection import  Selection

board_length = 9


class SudokuGame(object):

    def __init__(self):
        self.given = None
        return


    def load(self, board):
        self.given = Given(numpy.reshape(board, (board_length, board_length)))
        return


    def print_solution(self,  solution):
        return print( str(solution) )

    def play(self):
        population_size = 1000  # Number of individuals
        number_best_individuals = int(0.05 * population_size)  # Number of better individuals to consider for crossover.
        generations = 1000
        mutations = 2

        # Mutation parameters.
        phi = 0
        sigma = 1
        mutation_rate = 0.09

        # Create an initial population.
        self.population = Population()
        self.population.seed(population_size, self.given)

        # For up to 10000 generations...
        stale = 0
        for generation in range(0, generations):

            print("Generation %d" % generation)

            # Check for a solution.
            best_fitness = 0.0
            for c in range(0, population_size):
                fitness = self.population.candidates[c].fitness
                if (fitness == 1):
                    print("Solution found at generation %d!" % generation)
                    print(self.population.candidates[c].values)
                    return self.population.candidates[c]

                # Find the best fitness.
                if (fitness > best_fitness):
                    best_fitness = fitness

            print("Best fitness: %f" % best_fitness)

            # Create the next population.
            next_population = []

            # Select the individuals with better fitness
            self.population.sort()
            best_individuals = []
            for e in range(0, number_best_individuals):
                elite = Individual()
                elite.values = numpy.copy(self.population.candidates[e].values)
                best_individuals.append(elite)

            # Create the rest of the candidates.
            for count in range(number_best_individuals, population_size, 2):
                # Select parents from population via a tournament.
                t = Selection()
                parent1 = t.compete(self.population.candidates , 0.85)
                parent2 = t.compete(self.population.candidates, 0.85)

                ## Cross-over.
                c = Crossover()
                child1, child2 = c.crossover(parent1, parent2, crossover_rate=1.0)

                # Mutate child1.
                old_fitness = child1.fitness
                success = child1.mutate(mutation_rate, self.given)
                child1.update_fitness()
                if (success):
                    mutations += 1
                    if (old_fitness is not None and child1.fitness > old_fitness):  # Used to calculate the relative success rate of mutations.
                        phi = phi + 1

                # Mutate child2.
                old_fitness = child2.fitness
                success = child2.mutate(mutation_rate, self.given)
                child2.update_fitness()
                if (success):
                    mutations += 1
                    if (old_fitness is not None and child2.fitness > old_fitness):  # Used to calculate the relative success rate of mutations.
                        phi = phi + 1

                # Add children to new population.
                next_population.append(child1)
                next_population.append(child2)

            # Append elites onto the end of the population. These will not have been affected by crossover or mutation.
            for e in range(0, number_best_individuals):
                next_population.append(best_individuals[e])

            # Select next generation.
            self.population.candidates = next_population
            self.population.update_fitness()

            # Calculate new adaptive mutation rate (based on Rechenberg's 1/5 success rule). This is to stop too much mutation as the fitness progresses towards unity.
            if (mutations == 0):
                phi = 0  # Avoid divide by zero.
            else:
                phi = phi / mutations

            if (phi > 0.2):
                sigma = sigma / 0.998
            elif (phi < 0.2):
                sigma = sigma * 0.998

            mutation_rate = abs(numpy.random.normal(loc=0.0, scale=sigma, size=None))
            mutations = 0
            phi = 0

            # Check for stale population.
            self.population.sort()
            if (self.population.candidates[0].fitness != self.population.candidates[1].fitness):
                stale = 0
            else:
                stale += 1

            # Re-seed the population if 100 generations have passed with the fittest two candidates always having the same fitness.
            if (stale >= 100):
                print("The population has gone stale. Re-seeding...")
                self.population.seed(population_size, self.given)
                stale = 0
                sigma = 1
                phi = 0
                mutations = 0
                mutation_rate = 0.06

        print("No solution found.")
        return None