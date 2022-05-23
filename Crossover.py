from numpy import random

import Sudoku
from Selection import Sudokus


class Crossover:

    def __init__(self ):
        pass


    def apply_crossover(self , sudokus , moreChildren):
        strategy = random.randint(1,2)

        if(strategy == 1):
            self.apply_row_crossover( sudokus , moreChildren )
        else:
            self.apply_column_crossover()


    def apply_row_crossover(self, sudokus: [], moreChildren):

        new_sudokus = []

        for i in range(50):
            dad = sudokus[random.randint(0, len(sudokus) - 1)]
            mother = sudokus[random.randint(0, len(sudokus) - 1)]

            runs = 1
            if moreChildren:
                runs = 2

            for i in range(runs):
                row_to_apply = random.randint(1, 9)
                #print("CROSSOVER ON ROW " + str(row_to_apply))
                dadGenes = dad.get_board_until_row(row_to_apply)
                motherGenes = mother.get_board_from_row(row_to_apply)
                child = dadGenes + motherGenes
                new_sudokus.append(child)
                motherGenes2 = mother.get_board_until_row(row_to_apply)
                dadGenes2 = dad.get_board_from_row(row_to_apply)
                child2 = motherGenes2 + dadGenes2
                new_sudokus.append(child2)

        sudokus = new_sudokus
        return sudokus

    def apply_column_crossover(self, dad : Sudoku, mother : Sudoku):
        pass

    def apply_mixed_crossover(self):
        pass




