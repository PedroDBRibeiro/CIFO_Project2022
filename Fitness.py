import Sudoku


class Fitness():

    def __init__(self):
        self.fitness_score = 0;


    def calculate_fitness(self, sudoku : Sudoku) :
        self.fitness_score = 0;
        self.row_evaluation(sudoku)
        self.column_evaluation(sudoku)
        self.block_evaluation(sudoku)
        sudoku.fitness_score = self.fitness_score


    def row_evaluation(self, sudoku):
        min_current_index = 0
        max_current_index = 9

        while max_current_index<= len(sudoku.board):
            row = set(sudoku.board[min_current_index:max_current_index])
            self.fitness_score += 9-len(row)

            min_current_index += 9
            max_current_index += 9

    def column_evaluation(self, sudoku):
        columns = [0,9,18,27,36,45,54,63,72]

        for i in range(9):
            column = set([sudoku.board[index] for index in columns])
            self.fitness_score += 9-len(column)
            columns = [x + 1 for x in columns]

    def block_evaluation(self, sudoku):
        blocks = [0,1,2,9,10,11,54,63,72]

        for i in range(9):
            block = set([sudoku.board[index] for index in blocks])
            self.fitness_score += 9-len(block)
            blocks = [x + 1 for x in blocks]
