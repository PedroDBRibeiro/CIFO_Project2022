from charles.crossover import pmx_co, single_point_co, cycle_co, arithmetic_co
from charles.mutation import inversion_mutation, swap_mutation
from charles.selection import tournament
from sudoku_data.SudokuProblems import sudoku1
from charles.charles import *

if __name__ == '__main__':
    print(sudoku1)

pop = Population(
    size=800,
    optim="min",
    sudoku=sudoku1
)

pop.evolve(
    gens=300,
    select=tournament,
    crossover=single_point_co,
    mutate=swap_mutation,
    co_p=0.8,
    mu_p=0.2,
    elitism=True
)



