from operator import attrgetter

from Crossover import Crossover
from Fitness import *
from Selection import Selection
from SudokuGame import SudokuGame
from sudoku_data.SudokuProblems import sudoku1
from Population import Population
from Sudoku import Sudoku


if __name__ == '__main__':

    s = SudokuGame()
    s.load(sudoku1)
    solution = s.solve()
    if (solution):
        s.save("solution.txt", solution)

    """print(str(sudoku1))

    #populate = Population(sudoku1, 100)
    #sudokus = populate.fill()

    #generation = 0
    #while generation < 100:
    #    f = Fitness()
    #    i = 0
    #    for sudoku in sudokus:
    #        f.calculate_fitness(sudoku)
    #        print("Sudoku " + str(i) + " Fitness : " + str(sudoku.fitness_score))
    #        i += 1

    #    selec = Selection(sudokus)
        sudokus = selec.tournment(20)

        #i = 0
        #for sudoku in sudokus:
         #   print("Sudoku " + str(i) + " Fitness : " + str(sudoku.fitness_score) + " and Board : " + str(sudoku.board) )
        #    i += 1

        if generation < 50:
            moreChildren = True
        else:
            moreChildren = False

        c = Crossover()
        sudokus = c.apply_row_crossover(sudokus, moreChildren)

        best_sudoku = min(sudokus, key=attrgetter('fitness_score'))
        print("BEST SUDOKU ON ITERATION " + str(generation) + " HAS FITNESS " + str(best_sudoku.fitness_score) )
        generation += 1"""




