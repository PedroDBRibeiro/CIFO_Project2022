import random
from abc import ABC, abstractmethod
from enum import Enum
from Util import better
import Parameters


class ISelection(ABC):

    @abstractmethod
    def select(self, individuals):
        pass


class TournamentSelection(ISelection):

    def __init__(self):
        return

    def select(self, individuals):
        i = 0
        c1 = individuals[random.randint(0, len(individuals)-1)]
        best = c1
        while i < Parameters.tournament_size:
            # Select 2 random individuals and make them compete

            c2 = individuals[random.randint(0, len(individuals)-1)]

            # Find the strongest and the weakest.
            if better(Parameters.is_maximization, c1.fitness, c2.fitness):
                strongest = c1
                weakest = c2
            else:
                strongest = c2
                weakest = c1

            i = i + 1

            rand = random.uniform(0, 1)
            if(rand < Parameters.selection_rate):
                best = strongest
            else:
                best = weakest

        return best


class ProportionalSelection(ISelection):
    def __init__(self):
        return

    def select(self, individuals):
        if Parameters.is_maximization:
            max = sum([i.fitness for i in individuals])

            while True:
                current = 0
                pick = random.uniform(0, max)
                for individual in individuals:
                    current = current + individual.fitness
                    if current > pick:
                        return individual
        else:
            max = sum([1 / i.fitness for i in individuals])
            while True:
                current = 0
                pick = random.uniform(0, max)
                for individual in individuals:
                    current = current + (1 / individual.fitness)
                    if current > pick:
                        return individual



def pick_selection_algorithm(algorithm):
    return{
        'tournament': TournamentSelection(),
        'proportional': ProportionalSelection()
    }.get(algorithm, 'tournament')
