from SudokuGame import SudokuGame
from sudoku_data.SudokuProblems import sudoku1
import Parameters

if __name__ == '__main__':

    s = SudokuGame(Parameters.population_size, Parameters.generations, Parameters.mutation_rate)
    s.load(sudoku1)
    solution = s.play()
    if (solution):
        s.print_solution(solution)
    else:
        print("NO SOLUTION WAS FOUND")



