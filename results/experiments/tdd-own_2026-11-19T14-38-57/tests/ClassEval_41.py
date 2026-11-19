import unittest


import unittest

class AgentTest_make_move(unittest.TestCase):

    def test_make_move_1(self):
        game = GomokuGame(10)
        self.assertIs(game.make_move(5, 5), True)

    def test_make_move_2(self):
        game = GomokuGame(10)
        game.make_move(5, 5)
        self.assertIs(game.make_move(5, 5), False)

    def test_make_move_3(self):
        game = GomokuGame(10)
        game.make_move(2, 7)
        self.assertEqual(game.board[2][7], 'X')
        game.make_move(4, 1)
        self.assertEqual(game.board[4][1], 'O')

    def test_make_move_4(self):
        game = GomokuGame(10)
        self.assertEqual(game.current_player, 'X')
        game.make_move(0, 0)
        self.assertEqual(game.current_player, 'O')
        game.make_move(0, 1)
        self.assertEqual(game.current_player, 'X')
        game.make_move(0, 2)
        self.assertEqual(game.current_player, 'O')

    def test_make_move_5(self):
        game = GomokuGame(10)
        board_before = [row[:] for row in game.board]
        player_before = game.current_player
        self.assertIs(game.make_move(10, 3), False)
        self.assertIs(game.make_move(-1, 4), False)
        self.assertIs(game.make_move(3, 10), False)
        self.assertEqual(game.board, board_before)
        self.assertEqual(game.current_player, player_before)

import unittest

class AgentTest__check_five_in_a_row(unittest.TestCase):

    def test__check_five_in_a_row_1(self):
        game = GomokuGame(10)
        moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1)]
        for move in moves:
            game.make_move(move[0], move[1])
        self.assertIs(game._check_five_in_a_row(5, 1, (0, 1)), True)

    def test__check_five_in_a_row_2(self):
        game = GomokuGame(10)
        moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1)]
        for move in moves:
            game.make_move(move[0], move[1])
        self.assertIs(game._check_five_in_a_row(5, 1, (1, 1)), False)

    def test__check_five_in_a_row_3(self):
        game = GomokuGame(10)
        moves = [(2, 2), (0, 0), (2, 3), (0, 1), (2, 4), (0, 2), (2, 5), (0, 3)]
        for move in moves:
            game.make_move(move[0], move[1])
        self.assertIs(game._check_five_in_a_row(2, 2, (0, 1)), False)

    def test__check_five_in_a_row_4(self):
        game = GomokuGame(10)
        moves = [(0, 0), (9, 9), (1, 0), (9, 8), (2, 0), (9, 7), (3, 0), (9, 6), (4, 0)]
        for move in moves:
            game.make_move(move[0], move[1])
        self.assertIs(game._check_five_in_a_row(0, 0, (1, 0)), True)

    def test__check_five_in_a_row_5(self):
        game = GomokuGame(10)
        moves = [(0, 0), (0, 9), (1, 1), (1, 9), (2, 2), (2, 9), (3, 3), (3, 9), (4, 4)]
        for move in moves:
            game.make_move(move[0], move[1])
        self.assertIs(game._check_five_in_a_row(0, 0, (1, 1)), True)

import unittest

class AgentTest_check_winner(unittest.TestCase):

    def test_check_winner_1(self):
        game = GomokuGame(10)
        moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1)]
        for move in moves:
            game.make_move(move[0], move[1])
        self.assertEqual(game.check_winner(), 'X')

    def test_check_winner_2(self):
        game = GomokuGame(10)
        self.assertIsNone(game.check_winner())

    def test_check_winner_3(self):
        game = GomokuGame(10)
        moves = [(0, 0), (1, 9), (0, 1), (2, 9), (0, 2), (3, 9), (0, 3), (4, 9), (9, 0), (5, 9)]
        for move in moves:
            game.make_move(move[0], move[1])
        self.assertEqual(game.check_winner(), 'O')

    def test_check_winner_4(self):
        game = GomokuGame(10)
        moves = [(0, 0), (0, 9), (1, 1), (9, 9), (2, 2), (9, 8), (3, 3), (9, 7), (4, 4)]
        for move in moves:
            game.make_move(move[0], move[1])
        self.assertEqual(game.check_winner(), 'X')

    def test_check_winner_5(self):
        game = GomokuGame(10)
        moves = [(5, 1), (0, 0), (5, 2), (0, 1), (5, 3), (0, 2), (5, 4), (0, 3)]
        for move in moves:
            game.make_move(move[0], move[1])
        self.assertIsNone(game.check_winner())