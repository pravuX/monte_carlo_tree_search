import numpy as np


class GameState:
    piece = {
        -1: "O", 0: ' ', 1: "X"
    }

    def __init__(self, board, board_dim, turn=1):
        self.board = board
        self.board_dim = board_dim
        self.turn = turn

    def get_result(self):
        # this only works for 3x3 grids
        # Rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != 0:
                return self.board[i]
        # Columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != 0:
                return self.board[i]
        # Diagonals
        if self.board[0] == self.board[4] == self.board[8] != 0:
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != 0:
            return self.board[2]

        if self.is_board_full():
            return 0

        return None

    def is_board_full(self):
        return 0 not in self.board

    def is_game_over(self):
        return self.get_result() is not None

    def get_legal_moves(self):
        """Return all legal moves possible from current board state"""
        if self.is_game_over():
            return []
        return [i for i, cell in enumerate(self.board) if cell == 0]

    def make_move(self, move):
        """Place a piece in the given cell and change turn, return the new game state"""
        new_board = np.copy(self.board)
        turn = self.turn
        if new_board[move] == 0:
            new_board[move] = self.turn
            turn *= -1
        return GameState(new_board, board_dim=self.board_dim, turn=turn)

    def display_board(self):
        print("-"*13)
        for i, cell in enumerate(self.board):
            if i % 3 == 0:
                print("|", end=" ")
            print(self.piece[cell], end=" | ")
            if (i+1) % 3 == 0:
                print()
                print("-"*13)
