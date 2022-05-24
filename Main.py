from SudokuGame import SudokuGame
from sudoku_data.SudokuProblems import sudoku1


if __name__ == '__main__':

    s = SudokuGame()
    s.load(sudoku1)
    solution = s.play()
    if (solution):
        s.print_solution(solution)
    else:
        print("NO SOLUTION WAS FOUND")



