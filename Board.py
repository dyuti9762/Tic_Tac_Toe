from models.GameState import GameState
from models.Errors import PositionNotValidError


class Board:

    def __init__(self):
        self.game_board = None
        self.game_states = GameState
        self.set_game_board()

    def _check_diagonals_for_winner(self):
        return self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] or self.game_board[0][2] == \
               self.game_board[1][1] == self.game_board[2][0]

    def _check_rows_for_winner(self):
        for row in range(3):
            if self.game_board[row][0] == self.game_board[row][1] == self.game_board[row][2]:
                return True
        return False

    def _check_columns_for_winner(self):
        for col in range(3):
            if self.game_board[0][col] == self.game_board[1][col] == self.game_board[2][col]:
                return True
        return False

    def _check_if_no_moves_left(self):
        for row in range(3):
            for col in range(3):
                if self.game_board[row][col] != 'X' and self.game_board[row][col] != 'O':
                    return False
        return True

    def _get_row_and_column_indices_of_position(self, position): 
        for row in range(3):
            for col in range(3):
                if position == self.game_board[row][col]:
                    return row, col
        raise PositionNotValidError(position)

    def set_game_board(self, custom_board=None): 
        if custom_board:
            self.game_board = custom_board
            return

        self.game_board = []
        cell_number = 1
        for row in range(3):
            self.game_board.append([])
            for col in range(3):
                self.game_board[row].append(str(cell_number))
                cell_number += 1

    def get_game_board(self): #??
        return self.game_board

    def update_game_board(self, position, piece): #??
        row, column = self._get_row_and_column_indices_of_position(position)
        self.game_board[row][column] = piece

    def get_game_state(self): #encapsulation
        if self._check_rows_for_winner() or self._check_columns_for_winner() or self._check_diagonals_for_winner():
            return self.game_states.WINNER
        if self._check_if_no_moves_left():
            return self.game_states.DRAW
        return self.game_states.ONGOING

    def display(self):
        for row in range(3):
            for col in range(3):
                if self.game_board[row][col] != 'X' and self.game_board[row][col] != 'O':
                    print(' _ ', end="")
                else:
                    print(' {} '.format(self.game_board[row][col]), end="")
            print()
        print()
