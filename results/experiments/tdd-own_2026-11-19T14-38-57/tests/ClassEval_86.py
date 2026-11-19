import unittest


import unittest

class AgentTest_make_move(unittest.TestCase):

    def test_make_move_1(self):
        ttt = TicTacToe()
        result = ttt.make_move(1, 1)
        self.assertIsInstance(result, bool)
        self.assertTrue(result)
        self.assertEqual(ttt.board[1][1], 'X')

    def test_make_move_2(self):
        ttt = TicTacToe()
        self.assertEqual(ttt.current_player, 'X')
        ttt.make_move(1, 1)
        self.assertEqual(ttt.current_player, 'O')

    def test_make_move_3(self):
        ttt = TicTacToe()
        self.assertTrue(ttt.make_move(0, 0))
        self.assertTrue(ttt.make_move(2, 2))
        self.assertEqual(ttt.board[0][0], 'X')
        self.assertEqual(ttt.board[2][2], 'O')
        self.assertEqual(ttt.current_player, 'X')

    def test_make_move_4(self):
        ttt = TicTacToe()
        ttt.make_move(1, 1)
        result = ttt.make_move(1, 1)
        self.assertFalse(result)
        self.assertEqual(ttt.board[1][1], 'X')

    def test_make_move_5(self):
        ttt = TicTacToe()
        self.assertTrue(ttt.make_move(0, 2))
        self.assertEqual(ttt.board[0][2], 'X')
        self.assertEqual(ttt.board[2][0], ' ')
        self.assertEqual(ttt.board[0][0], ' ')
        self.assertEqual(ttt.board[2][2], ' ')

import unittest

class AgentTest_check_winner(unittest.TestCase):

    def test_check_winner_1(self):
        ttt = TicTacToe()
        self.assertIsNone(ttt.check_winner())

    def test_check_winner_2(self):
        ttt = TicTacToe()
        moves = [(1, 0), (2, 0), (1, 1), (2, 1), (1, 2)]
        for move in moves:
            ttt.make_move(move[0], move[1])
        self.assertEqual(ttt.check_winner(), 'X')

    def test_check_winner_3(self):
        ttt = TicTacToe()
        # X(0,0) O(0,1) X(0,2) O(1,1) X(2,0) O(2,1)
        moves = [(0, 0), (0, 1), (0, 2), (1, 1), (2, 0), (2, 1)]
        for move in moves:
            ttt.make_move(move[0], move[1])
        self.assertEqual(ttt.check_winner(), 'O')

    def test_check_winner_4(self):
        ttt = TicTacToe()
        # X(0,0) O(0,1) X(1,1) O(0,2) X(2,2)
        moves = [(0, 0), (0, 1), (1, 1), (0, 2), (2, 2)]
        for move in moves:
            ttt.make_move(move[0], move[1])
        self.assertEqual(ttt.check_winner(), 'X')

    def test_check_winner_5(self):
        ttt = TicTacToe()
        # X(0,0) O(0,2) X(0,1) O(1,1) X(1,2) O(2,0)
        moves = [(0, 0), (0, 2), (0, 1), (1, 1), (1, 2), (2, 0)]
        for move in moves:
            ttt.make_move(move[0], move[1])
        self.assertEqual(ttt.check_winner(), 'O')

import unittest

class AgentTest_is_board_full(unittest.TestCase):

    def test_is_board_full_1(self):
        ttt = TicTacToe()
        result = ttt.is_board_full()
        self.assertIsInstance(result, bool)
        self.assertFalse(result)

    def test_is_board_full_2(self):
        ttt = TicTacToe()
        ttt.make_move(1, 1)
        self.assertFalse(ttt.is_board_full())

    def test_is_board_full_3(self):
        ttt = TicTacToe()
        cells = [(r, c) for r in range(3) for c in range(3)]
        for row, col in cells[:8]:
            ttt.make_move(row, col)
        self.assertFalse(ttt.is_board_full())

    def test_is_board_full_4(self):
        ttt = TicTacToe()
        for row in range(3):
            for col in range(3):
                ttt.make_move(row, col)
        result = ttt.is_board_full()
        self.assertIsInstance(result, bool)
        self.assertTrue(result)

    def test_is_board_full_5(self):
        ttt = TicTacToe()
        # Draw game: X O X / X O O / O X X, no winner, board completely filled
        moves = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 0),
                 (1, 2), (2, 1), (2, 0), (2, 2)]
        for move in moves:
            ttt.make_move(move[0], move[1])
        self.assertTrue(ttt.is_board_full())