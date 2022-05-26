from Individual import Individual

board_size = 9  #

class Given(Individual):
    # Grid containing the values of a sudoku

    def __init__(self, values):
        self.values = values
        return

    def duplicates_in_row(self, row, value):
        # Check if row has duplicates
        for column in range(0, board_size):
            if(self.values[row][column] == value):
               return True
        return False

    def duplicates_in_column(self, column, value):
        # Check if column has duplicates
        for row in range(0, board_size):
            if(self.values[row][column] == value):
               return True
        return False

    def duplicates_in_block(self, row, column, value):
        # Check if 3 x 3 block has duplicates
        i = 3*(int(row/3))
        j = 3*(int(column/3))

        if((self.values[i][j] == value)
           or (self.values[i][j+1] == value)
           or (self.values[i][j+2] == value)
           or (self.values[i+1][j] == value)
           or (self.values[i+1][j+1] == value)
           or (self.values[i+1][j+2] == value)
           or (self.values[i+2][j] == value)
           or (self.values[i+2][j+1] == value)
           or (self.values[i+2][j+2] == value)):
            return True
        else:
            return False
