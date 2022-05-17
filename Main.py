
from Fitness import *
from sudoku_data.SudokuProblems import sudoku1
from Population import Population


if __name__ == '__main__':
    print(sudoku1)
    a = Population(sudoku1)
    a.fill()
    f = Fitness()
    fit = f.calculate_fitness(sudoku1)
    print("FITNESS SCORE : " + str(fit) )




