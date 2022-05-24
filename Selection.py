import random


class Selection(object):

    def __init__(self):
        return

    def tournment(self, individuals , selection_rate):
        # Select 2 random individuals and make them compete
        c1 = individuals[random.randint(0, len(individuals)-1)]
        c2 = individuals[random.randint(0, len(individuals)-1)]

        # Find the strongest and the weakest.
        if(c1.fitness > c2.fitness):
            strongest = c1
            weakest = c2
        else:
            strongest = c2
            weakest = c1

        rand = random.uniform(0, 1)
        if(rand < selection_rate):
            return strongest
        else:
            return weakest