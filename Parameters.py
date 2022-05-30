# Problem parameters
from sudoku_data import SudokuProblems

board_length = 9
runs = 1
currentSudoku = SudokuProblems.medium
sudokuName = "Medium"
verbose = True
timePath = "Results/time_analysis_random.xlsx"
resultsPath = "Results/results_random.xlsx"
reseeding = False

# GA parameters
elitism = True
population_size = 1000
generations = 125
mutation_rate = 0.15

# Selection Parameters
is_maximization = True
selection_algorithm = 'tournament'  # tournament or proportional
selection_mutation = 'scramble' #swap or inversion or scramble
number_of_mutations = 1
tournament_size = 10
selection_rate = 0.90
crossover_rate = 0.90
