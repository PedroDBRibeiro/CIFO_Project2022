from numpy import random

import Sudoku
class Crossover:

    def __init__(self ):
        pass


    def apply_crossover(self , dad : Sudoku, mother : Sudoku):
        strategy = random.randint(1,2)

        if(strategy == 1):
            self.apply_row_crossover(dad , mother )
        else:
            self.apply_column_crossover()


    def apply_row_crossover(self, dad : Sudoku, mother : Sudoku):
        row_to_apply = random.randint(1, 9)
        print("CROSSOVER ON ROW " + str(row_to_apply))
        dadGenes = dad.get_board_until_row(row_to_apply)
        motherGenes = mother.get_board_from_row(row_to_apply)
        child = dadGenes + motherGenes
        return child

    def apply_column_crossover(self, dad : Sudoku, mother : Sudoku):
        pass

    def apply_mixed_crossover(self):
        pass


