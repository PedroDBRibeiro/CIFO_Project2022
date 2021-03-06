import numpy
import random
import itertools

board_length = 9


class Individual(object):
    # A possible solution for the Sudoku puzzle.
    def __init__(self):
        self.values = numpy.zeros((board_length, board_length), dtype=int)
        self.fitness = None
        return

    def update_fitness(self):
        """ The fitness of a candidate solution is determined by how close it is to being the actual solution to the puzzle. The actual solution (i.e. the 'fittest') is defined as a 9x9 grid of numbers in the range [1, 9] where each row, column and 3x3 block contains the numbers [1, 9] without any duplicates (see e.g. http://www.sudoku.com/); if there are any duplicates then the fitness will be lower. """

        row_count = numpy.zeros(board_length)
        column_count = numpy.zeros(board_length)
        block_count = numpy.zeros(board_length)
        row_sum = 0
        column_sum = 0
        block_sum = 0

        for i in range(0, board_length):  # For each row...
            for j in range(0, board_length):  # For each number within it...
                row_count[self.values[i][j] - 1] += 1  # ...Update list with occurrence of a particular number.

            row_sum += (1.0 / len(set(row_count))) / board_length
            row_count = numpy.zeros(board_length)

        for i in range(0, board_length):  # For each column...
            for j in range(0, board_length):  # For each number within it...
                column_count[self.values[j][i] - 1] += 1  # ...Update list with occurrence of a particular number.

            column_sum += (1.0 / len(set(column_count))) / board_length
            column_count = numpy.zeros(board_length)

        # For each block...
        for i in range(0, board_length, 3):
            for j in range(0, board_length, 3):
                block_count[self.values[i][j] - 1] += 1
                block_count[self.values[i][j + 1] - 1] += 1
                block_count[self.values[i][j + 2] - 1] += 1

                block_count[self.values[i + 1][j] - 1] += 1
                block_count[self.values[i + 1][j + 1] - 1] += 1
                block_count[self.values[i + 1][j + 2] - 1] += 1

                block_count[self.values[i + 2][j] - 1] += 1
                block_count[self.values[i + 2][j + 1] - 1] += 1
                block_count[self.values[i + 2][j + 2] - 1] += 1

                block_sum += (1.0 / len(set(block_count))) / board_length
                block_count = numpy.zeros(board_length)

        # Calculate overall fitness.
        if (int(row_sum) == 1 and int(column_sum) == 1 and int(block_sum) == 1):
            fitness = 1.0
        else:
            fitness = column_sum * block_sum

        self.fitness = fitness
        return

    def mutate(self, mutation_rate, given , number_of_mutations = 1):
        """ Mutate a candidate by picking a row, and then picking two values within that row to swap. """

        r = random.uniform(0, 1.1)
        while (r > 1):  # Outside [0, 1] boundary - choose another
            r = random.uniform(0, 1.1)

        done_mutations = 0
        #success = False
        if (r < mutation_rate):  # Mutate.
            while ( number_of_mutations > done_mutations ): #not success
                row1 = random.randint(0, 8)
                row2 = row1

                from_column = random.randint(0, 8)
                to_column = random.randint(0, 8)
                while (from_column == to_column):
                    from_column = random.randint(0, 8)
                    to_column = random.randint(0, 8)

                # Check if the two places are free...
                if (given.values[row1][from_column] == 0 and given.values[row1][to_column] == 0):
                    # ...and that we are not causing a duplicate in the rows' columns.
                    if (  (not given.duplicates_in_column(to_column, self.values[row1][from_column])
                            and not given.duplicates_in_column(from_column, self.values[row2][to_column])
                            and not given.duplicates_in_block(row2, to_column, self.values[row1][from_column])
                            and not given.duplicates_in_block(row1, from_column, self.values[row2][to_column]))):
                        # Swap values.
                        temp = self.values[row2][to_column]
                        self.values[row2][to_column] = self.values[row1][from_column]
                        self.values[row1][from_column] = temp
                        done_mutations += 1
                        #success = True


    def mutate_inversion(self, mutation_rate, given ):

        r = random.uniform(0, 1.1)
        while (r > 1):  # Outside [0, 1] boundary - choose another
            r = random.uniform(0, 1.1)

        if (r < mutation_rate):  # Mutate.
            row1 = random.randint(0, 8)

            startMutation = 0
            finishMutation = 0
            while (startMutation >= finishMutation):
                startMutation = random.randint(0, 8)
                finishMutation = random.randint(0, 8)

            initial = self.values[row1][:startMutation]
            to_invert = numpy.copy(self.values[row1][startMutation:finishMutation])
            to_invert = to_invert[::-1]
            final = self.values[row1][finishMutation:]
            join = list(itertools.chain(initial, to_invert, final))
            self.values[row1] = join


    def mutate_scramble(self, mutation_rate, given ):

        r = random.uniform(0, 1.1)
        while (r > 1):  # Outside [0, 1] boundary - choose another
            r = random.uniform(0, 1.1)

        if (r < mutation_rate):  # Mutate.
            row1 = random.randint(0, 8)
            startMutation = 0
            finishMutation = 0
            while( startMutation >= finishMutation):
                startMutation = random.randint(0, 8)
                finishMutation = random.randint(0, 8)


            initial = self.values[row1][:startMutation]
            to_shuffle = numpy.copy(self.values[row1][startMutation:finishMutation])
            random.shuffle(to_shuffle)
            final = self.values[row1][finishMutation:]
            join = list(itertools.chain(initial, to_shuffle, final))
            self.values[row1] =  join


