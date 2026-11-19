import unittest



class TicTacToeTestMakeMove(unittest.TestCase):
    def test_make_move_1(self):
        ttt = TicTacToe()
        self.assertEqual(ttt.current_player, 'X')
        self.assertTrue(ttt.make_move(0, 0))
        self.assertEqual(ttt.current_player, 'O')

    def test_make_move_2(self):
        ttt = TicTacToe()
        self.assertEqual(ttt.current_player, 'X')
        self.assertTrue(ttt.make_move(0, 0))
        self.assertTrue(ttt.make_move(0, 1))
        self.assertFalse(ttt.make_move(0, 0))
        self.assertEqual(ttt.current_player, 'X')

    def test_make_move_3(self):
        ttt = TicTacToe()
        self.assertEqual(ttt.current_player, 'X')
        self.assertTrue(ttt.make_move(0, 0))
        self.assertTrue(ttt.make_move(0, 1))
        self.assertTrue(ttt.make_move(1, 1))
        self.assertEqual(ttt.current_player, 'O')

import unittest

class AgentTest_make_move(unittest.TestCase):
    def test_make_move_1(self):
        ttt = TicTacToe()
        self.assertTrue(ttt.make_move(1, 1))
        self.assertEqual(ttt.board[1][1], 'X')
        self.assertTrue(ttt.make_move(0, 2))
        self.assertEqual(ttt.board[0][2], 'O')
        self.assertEqual(ttt.board[1][1], 'X')
        for r in range(3):
            for c in range(3):
                if (r, c) not in [(1, 1), (0, 2)]:
                    self.assertEqual(ttt.board[r][c], ' ')

    def test_make_move_2(self):
        ttt = TicTacToe()
        self.assertTrue(ttt.make_move(0, 0))
        self.assertEqual(ttt.board[0][0], 'X')
        self.assertFalse(ttt.make_move(0, 0))
        self.assertEqual(ttt.board[0][0], 'X')
        self.assertEqual(ttt.current_player, 'O')

class TicTacToeTestCheckWinner(unittest.TestCase):
    # rows
    def test_check_winner_1(self):
        ttt = TicTacToe()
        moves = [(1, 0), (2, 0), (1, 1), (2, 1), (1, 2)]
        for move in moves:
            ttt.make_move(move[0], move[1])
        self.assertEqual(ttt.check_winner(), 'X')

    def test_check_winner_2(self):
        ttt = TicTacToe()
        moves = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0)]
        for move in moves:
            ttt.make_move(move[0], move[1])
        self.assertEqual(ttt.check_winner(), 'X')

    def test_check_winner_3(self):
        ttt = TicTacToe()
        moves = [(0, 0), (0, 1), (1, 1), (0, 2), (2, 2)]
        for move in moves:
            ttt.make_move(move[0], move[1])
        self.assertEqual(ttt.check_winner(), 'X')

import unittest

class AgentTest_check_winner(unittest.TestCase):
    def test_check_winner_1(self):
        # column win for X in the rightmost column
        ttt = TicTacToe()
        moves = [(0, 2), (0, 0), (1, 2), (1, 0), (2, 2)]
        for move in moves:
            ttt.make_move(move[0], move[1])
        self.assertEqual(ttt.check_winner(), 'X')

    def test_check_winner_2(self):
        # anti-diagonal win for O
        ttt = TicTacToe()
        moves = [(0, 0), (0, 2), (0, 1), (1, 1), (2, 2), (2, 0)]
        for move in moves:
            ttt.make_move(move[0], move[1])
        self.assertEqual(ttt.check_winner(), 'O')

class TicTacToeTestIsBoardFull(unittest.TestCase):
    # not full
    def test_is_board_full_1(self):
        ttt = TicTacToe()
        self.assertFalse(ttt.is_board_full())

    def test_is_board_full_2(self):
        ttt = TicTacToe()
        moves = [(1, 1), (0, 2), (2, 2), (0, 0), (0, 1), (2, 1), (1, 0), (1, 2), (2, 0)]
        for move in moves:
            ttt.make_move(move[0], move[1])
        self.assertTrue(ttt.is_board_full())

    def test_is_board_full_3(self):
        ttt = TicTacToe()
        moves = [(0, 0), (0, 1), (1, 1), (1, 0), (2, 0)]
        for move in moves:
            ttt.make_move(move[0], move[1])
        self.assertFalse(ttt.is_board_full())

import unittest

class AgentTest_is_board_full(unittest.TestCase):
    def test_is_board_full_1(self):
        # Only one empty cell remains, so the board is not yet full
        ttt = TicTacToe()
        moves = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1)]
        for move in moves:
            ttt.make_move(move[0], move[1])
        self.assertFalse(ttt.is_board_full())

    def test_is_board_full_2(self):
        # Board is completely filled even though both players have a complete row
        ttt = TicTacToe()
        moves = [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2), (2, 0), (2, 1), (2, 2)]
        for move in moves:
            ttt.make_move(move[0], move[1])
        self.assertTrue(ttt.is_board_full())