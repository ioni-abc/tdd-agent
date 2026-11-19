import unittest



class GomokuGameTestMakeMove(unittest.TestCase):
    def setUp(self) -> None:
        self.board_size = 10
        self.gomokuGame = GomokuGame(self.board_size)

    def test_make_move_1(self):
        board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.assertEqual(True, self.gomokuGame.make_move(0, 0))
        board[0][0] = 'X'
        self.assertEqual(board, self.gomokuGame.board)

    def test_make_move_2(self):
        board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.assertEqual(True, self.gomokuGame.make_move(0, 0))
        self.assertEqual(False, self.gomokuGame.make_move(0, 0))
        board[0][0] = 'X'
        self.assertEqual(board, self.gomokuGame.board)

    def test_make_move_3(self):
        board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.assertEqual(True, self.gomokuGame.make_move(0, 0))
        self.assertEqual(True, self.gomokuGame.make_move(0, 1))
        board[0][0] = 'X'
        board[0][1] = 'O'
        self.assertEqual(board, self.gomokuGame.board)

import unittest

class AgentTest_make_move(unittest.TestCase):
    def setUp(self) -> None:
        self.board_size = 10
        self.gomokuGame = GomokuGame(self.board_size)

    def test_make_move_1(self):
        self.assertEqual('X', self.gomokuGame.current_player)
        self.assertEqual(True, self.gomokuGame.make_move(0, 0))
        self.assertEqual('O', self.gomokuGame.current_player)
        self.assertEqual(True, self.gomokuGame.make_move(0, 1))
        self.assertEqual('X', self.gomokuGame.current_player)

    def test_make_move_2(self):
        board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.assertEqual(True, self.gomokuGame.make_move(4, 4))
        board[4][4] = 'X'
        self.assertEqual('O', self.gomokuGame.current_player)
        self.assertEqual(False, self.gomokuGame.make_move(4, 4))
        self.assertEqual('O', self.gomokuGame.current_player)
        self.assertEqual(board, self.gomokuGame.board)

class GomokuGameTestCheckFiveInARow(unittest.TestCase):
    def setUp(self) -> None:
        self.gomokuGame = GomokuGame(10)
        moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1)]
        for move in moves:
            self.gomokuGame.make_move(move[0], move[1])

    def test_check_five_in_a_row_1(self):
        self.assertEqual(True, self.gomokuGame._check_five_in_a_row(5, 5, (0, -1)))

    def test_check_five_in_a_row_2(self):
        self.assertEqual(True, self.gomokuGame._check_five_in_a_row(5, 1, (0, 1)))

    def test_check_five_in_a_row_3(self):
        self.assertEqual(False, self.gomokuGame._check_five_in_a_row(0, 0, (0, 1)))

import unittest

class AgentTest__check_five_in_a_row(unittest.TestCase):
    def setUp(self) -> None:
        self.gomokuGame = GomokuGame(10)

    def test__check_five_in_a_row_1(self):
        # X builds a vertical line in column 0 at rows 0-4; O plays elsewhere.
        moves = [(0, 0), (9, 9), (1, 0), (9, 8), (2, 0), (9, 7), (3, 0), (9, 6), (4, 0)]
        for move in moves:
            self.gomokuGame.make_move(move[0], move[1])
        self.assertEqual(True, self.gomokuGame._check_five_in_a_row(0, 0, (1, 0)))

    def test__check_five_in_a_row_2(self):
        # X builds only four cells on a diagonal; the fifth cell is empty.
        moves = [(0, 0), (9, 9), (1, 1), (9, 8), (2, 2), (9, 7), (3, 3), (9, 6)]
        for move in moves:
            self.gomokuGame.make_move(move[0], move[1])
        self.assertEqual(False, self.gomokuGame._check_five_in_a_row(0, 0, (1, 1)))

class GomokuGameTestCheckWinner(unittest.TestCase):
    def test_check_winner_1(self):
        gomokuGame = GomokuGame(10)
        self.assertEqual(None, gomokuGame.check_winner())

    def test_check_winner_2(self):
        gomokuGame = GomokuGame(10)
        moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1)]
        for move in moves:
            gomokuGame.make_move(move[0], move[1])
        self.assertEqual('X', gomokuGame.check_winner())

    def test_check_winner_3(self):
        gomokuGame = GomokuGame(10)
        moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 0), (0, 4)]
        for move in moves:
            gomokuGame.make_move(move[0], move[1])
        self.assertEqual('O', gomokuGame.check_winner())

import unittest

class AgentTest_check_winner(unittest.TestCase):
    def test_check_winner_1(self):
        # X builds a vertical line in column 3 at rows 0-4; O plays four cells in row 9.
        gomokuGame = GomokuGame(10)
        moves = [(0, 3), (9, 0), (1, 3), (9, 1), (2, 3), (9, 2), (3, 3), (9, 3), (4, 3)]
        for move in moves:
            gomokuGame.make_move(move[0], move[1])
        self.assertEqual('X', gomokuGame.check_winner())

    def test_check_winner_2(self):
        # O builds an anti-diagonal line (row + col == 4) from (0, 4) to (4, 0);
        # X plays four cells in row 8 and one isolated cell, never reaching five.
        gomokuGame = GomokuGame(10)
        moves = [(8, 8), (0, 4), (8, 7), (1, 3), (8, 6), (2, 2),
                 (8, 5), (3, 1), (6, 9), (4, 0)]
        for move in moves:
            gomokuGame.make_move(move[0], move[1])
        self.assertEqual('O', gomokuGame.check_winner())