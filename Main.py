from Crossover import Crossover
from Fitness import *
from Selection import Selection
from sudoku_data.SudokuProblems import sudoku1
from Population import Population
from Sudoku import Sudoku


if __name__ == '__main__':

    print(str(sudoku1))

    populate = Population(sudoku1, 100)
    sudokus = populate.fill()
    f = Fitness()
    i = 0
    for sudoku in sudokus:
        f.calculate_fitness(sudoku)
        print("Sudoku " + str(i) + " Fitness : " + str(sudoku.fitness_score))
        i += 1

    selec = Selection(sudokus)
    sudokus = selec.tournment(20)
    i = 0
    for sudoku in sudokus:
        print("Sudoku " + str(i) + " Fitness : " + str(sudoku.fitness_score) + " and Board : " + str(sudoku.board) )
        i += 1

    #c = Crossover()
    #c.apply_row_crossover(sudokuA,sudokuB)




