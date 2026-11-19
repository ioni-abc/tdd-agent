import unittest


class TicTacToe:
    """
    The class represents a game of Tic-Tac-Toe and its functions include making a move on the board, checking for a winner, and determining if the board is full.
    """

    def __init__(self, N=3):
        """
        Initialize a 3x3 game board with all empty spaces and current symble player, default is 'X'.
        """
        self.board = [[' ' for _ in range(N)] for _ in range(3)]
        self.current_player = 'X'

    def make_move(self, row, col):
        """
        Place the current player's mark at the specified position on the board and switch the mark.
        :param row: int, the row index of the position
        :param col: int, the column index of the position
        :return: bool, indicating whether the move was successful or not
        >>> ttt.current_player
        'X'
        >>> ttt.make_move(1, 1)
        >>> ttt.current_player
        'O'
        """
        if not (0 <= row < len(self.board)):
            return False
        if not (0 <= col < len(self.board[row])):
            return False
        if self.board[row][col] != ' ':
            return False

        self.board[row][col] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return True

    def check_winner(self):
        """
        Check if there is a winner on the board in rows, columns and diagonals three directions
        :return: str or None, the mark of the winner ('X' or 'O'), or None if there is no winner yet
        >>> moves = [(1, 0), (2, 0), (1, 1), (2, 1), (1, 2)]
        >>> for move in moves:
        ...     ttt.make_move(move[0], move[1])
        >>> ttt.check_winner()
        'X'
        """
        lines = []

        # Rows
        for r in range(len(self.board)):
            lines.append([self.board[r][c] for c in range(len(self.board[r]))])

        # Columns
        num_cols = len(self.board[0]) if self.board else 0
        for c in range(num_cols):
            lines.append([self.board[r][c] for r in range(len(self.board))])

        # Diagonals (only meaningful on a square board)
        if self.board and len(self.board) == num_cols:
            n = len(self.board)
            lines.append([self.board[i][i] for i in range(n)])
            lines.append([self.board[i][n - 1 - i] for i in range(n)])

        for line in lines:
            if line and line[0] != ' ' and all(cell == line[0] for cell in line):
                return line[0]

        return None

    def is_board_full(self):
        """
        Check if the game board is completely filled.
        :return: bool, indicating whether the game board is full or not
        >>> ttt.is_board_full()
        False
        """
        return all(cell != ' ' for row in self.board for cell in row)