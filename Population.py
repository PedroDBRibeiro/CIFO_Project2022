from random import choice
import numpy as np

from Sudoku import Sudoku


class Population:

    def __init__(self, board , number_of_sudokus ):
        self.board = board
        self.number_of_sudokus = number_of_sudokus
        pass

    def fill(self):
        sudokus_filled = []
        for i in range(self.number_of_sudokus):

            sudoku = Sudoku(list(self.board))

            min_current_index = 0
            max_current_index = 9

            while max_current_index <= len(sudoku.board):
                row = [value for value in sudoku.board[min_current_index:max_current_index] if value > 0]
                for index in range(min_current_index,max_current_index):
                    if sudoku.board[index] == 0:
                        new_value =  choice( np.setdiff1d( range(1, 10) , row ))
                        sudoku.board[index] = new_value
                        row.append(new_value)

                min_current_index+=9
                max_current_index+=9
            sudokus_filled.append(sudoku)

        print(sudoku.board)
        return sudokus_filled
