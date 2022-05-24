import numpy
from sudoku_data.SudokuProblems import sudoku1
from charles.charles import fill

if __name__ == '__main__':
    print(fill(sudoku1))


def matrix(sudoku):
    matrix = numpy.zeros((9, 9))
    i = 0
    j = 0
    for array in sudoku:
        matrix[i][j] = array
        j += 1
        if j % 9 == 0:
            j = 0
            i += 1
    return matrix


"""
    def update_fitness(self):
        row_count = numpy.zeros(Nd)
        column_count = numpy.zeros(Nd)
        block_count = numpy.zeros(Nd)
        row_sum = 0
        column_sum = 0
        block_sum = 0

        for i in range(0, Nd):  # For each row...
            for j in range(0, Nd):  # For each number within it...
                row_count[self.values[i][j] - 1] += 1  # ...Update list with occurrence of a particular number.

            row_sum += (1.0 / len(set(row_count))) / Nd
            row_count = numpy.zeros(Nd)

        for i in range(0, Nd):  # For each column...
            for j in range(0, Nd):  # For each number within it...
                column_count[self.values[j][i] - 1] += 1  # ...Update list with occurrence of a particular number.

            column_sum += (1.0 / len(set(column_count))) / Nd
            column_count = numpy.zeros(Nd)

        # For each block...
        for i in range(0, Nd, 3):
            for j in range(0, Nd, 3):
                block_count[self.values[i][j] - 1] += 1
                block_count[self.values[i][j + 1] - 1] += 1
                block_count[self.values[i][j + 2] - 1] += 1

                block_count[self.values[i + 1][j] - 1] += 1
                block_count[self.values[i + 1][j + 1] - 1] += 1
                block_count[self.values[i + 1][j + 2] - 1] += 1

                block_count[self.values[i + 2][j] - 1] += 1
                block_count[self.values[i + 2][j + 1] - 1] += 1
                block_count[self.values[i + 2][j + 2] - 1] += 1

                block_sum += (1.0 / len(set(block_count))) / Nd
                block_count = numpy.zeros(Nd)

        # Calculate overall fitness.
        if (int(row_sum) == 1 and int(column_sum) == 1 and int(block_sum) == 1):
            fitness = 1.0
        else:
            fitness = column_sum * block_sum

        self.fitness = fitness
        return
"""
"""
    def calculate_fitness(self, sudoku):
        self.row_evaluation(sudoku)
        self.column_evaluation(sudoku)
        self.block_evaluation(sudoku)
        return self.fitness_score

    def row_evaluation(self, sudoku):
        min_current_index = 0
        max_current_index = 9

        while max_current_index <= len(sudoku):
            row = set(sudoku[min_current_index:max_current_index])
            self.fitness_score += 9 - len(row)

            min_current_index += 9
            max_current_index += 9

    def column_evaluation(self, sudoku):
        columns = [0, 9, 18, 27, 36, 45, 54, 63, 72]

        for i in range(9):
            column = set([sudoku[index] for index in columns])
            self.fitness_score += 9 - len(column)
            columns = [x + 1 for x in columns]

    def block_evaluation(self, sudoku):
        blocks = [0, 1, 2, 9, 10, 11, 54, 63, 72]

        for i in range(9):
            block = set([sudoku[index] for index in blocks])
            self.fitness_score += 9 - len(block)
            blocks = [x + 1 for x in blocks]
    """