from operator import attrgetter


class Sudokus(object):
    pass


class Selection:

    def __init__(self , sudokus ):
        self.sudokus = sudokus


    def tournment(self, number_to_consider):
        print(":: THE TOURNMENT STARTS NOW ::")
        scores = [o.fitness_score for o in self.sudokus]
        scores.sort()
        return [x for x in self.sudokus if x.fitness_score <= scores[number_to_consider]][:number_to_consider]
