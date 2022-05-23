
class Sudoku:

    def __init__(self, board):
        self.board = board
        self.untouchableIndexes = [idx for idx, val in enumerate(board) if val > 0]
        self.fitness_score = 0




    def get_board_until_row(self, row : int):
        board_until_row = self.board[0: 9*row]
        #print("BOARD UNTIL : " + str(board_until_row))
        return board_until_row


    def get_board_from_row(self , row: int):
        board_from_row = self.board[9 * row: 81]
        #print("BOARD FROM : " + str(board_from_row))
        return board_from_row