# src/game.py

import numpy as np

class Board:
    def __init__(self):
        # Initialize a 6x7 Connect 4 board
        self.rows = 6
        self.columns = 7
        self.board = np.zeros((self.rows, self.columns), dtype=int)
        self.current_player = 1

    def get_valid_moves(self):
        return [c for c in range(self.columns) if self.board[0][c] == 0]

    def make_move(self, column):
        for row in reversed(range(self.rows)):
            if self.board[row][column] == 0:
                self.board[row][column] = self.current_player
                self.current_player = 3 - self.current_player  # Switch player
                return True
        return False

    def is_terminal(self):
        return self.check_winner() is not None or not any(self.get_valid_moves())

    def check_winner(self):
        # Check horizontal, vertical, and diagonal for a win
        for c in range(self.columns - 3):
            for r in range(self.rows):
                if self.board[r][c] == self.board[r][c+1] == self.board[r][c+2] == self.board[r][c+3] != 0:
                    return self.board[r][c]
        for c in range(self.columns):
            for r in range(self.rows - 3):
                if self.board[r][c] == self.board[r+1][c] == self.board[r+2][c] == self.board[r+3][c] != 0:
                    return self.board[r][c]
        for c in range(self.columns - 3):
            for r in range(self.rows - 3):
                if self.board[r][c] == self.board[r+1][c+1] == self.board[r+2][c+2] == self.board[r+3][c+3] != 0:
                    return self.board[r][c]
        for c in range(self.columns - 3):
            for r in range(3, self.rows):
                if self.board[r][c] == self.board[r-1][c+1] == self.board[r-2][c+2] == self.board[r-3][c+3] != 0:
                    return self.board[r][c]
        return None

    def get_state(self):
        return self.board.copy()

    def copy(self):
        new_board = Board()
        new_board.board = self.board.copy()
        new_board.current_player = self.current_player
        return new_board