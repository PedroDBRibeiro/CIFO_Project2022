# Problem parameters
from sudoku_data import SudokuProblems

board_length = 9
runs = 1
currentSudoku = SudokuProblems.sudoku1
sudokuName = "Easy"
verbose = True

# GA parameters
elitism = False
population_size = 1000
generations = 125
mutation_rate = 0.15

# Selection Parameters
is_maximization = True
selection_algorithm = 'tournament'  # tournament or proportional
tournament_size = 10
selection_rate = 0.90
