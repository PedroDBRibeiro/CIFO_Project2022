from random import choice
import numpy as np


class Population:

    def __init__(self, sudoku):
        self.sudoku = sudoku

    def fill(self):
        min_current_index = 0;
        max_current_index = 9;

        while max_current_index <= len(self.sudoku):
            row = [value for value in self.sudoku[min_current_index:max_current_index] if value > 0]
            for index in range(min_current_index,max_current_index):
                if self.sudoku[index] == 0:
                    new_value =  choice( np.setdiff1d( range(1, 10) , row ))
                    self.sudoku[index] = new_value
                    row.append(new_value)

            min_current_index+=9
            max_current_index+=9
            print(self.sudoku)
