import unittest


import unittest

class AgentTest_init_game(unittest.TestCase):

    def test_init_game_1(self):
        # Example from the init_game docstring
        game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"])
        self.assertEqual(game.targets, [(3, 3)])
        self.assertEqual(game.boxes, [(2, 2)])
        self.assertEqual(game.player_row, 1)
        self.assertEqual(game.player_col, 1)

    def test_init_game_2(self):
        # Player, box and target placed in different positions
        game = PushBoxGame(["#####", "#   #", "#OX #", "#G  #", "#####"])
        self.assertEqual(game.player_row, 2)
        self.assertEqual(game.player_col, 1)
        self.assertEqual(game.boxes, [(2, 2)])
        self.assertEqual(game.targets, [(3, 1)])

    def test_init_game_3(self):
        # Multiple boxes and multiple targets are all collected
        game = PushBoxGame(["######", "#O   #", "# X G#", "# X G#", "######"])
        self.assertCountEqual(game.boxes, [(2, 2), (3, 2)])
        self.assertCountEqual(game.targets, [(2, 4), (3, 4)])
        self.assertEqual(len(game.boxes), 2)
        self.assertEqual(len(game.targets), 2)

    def test_init_game_4(self):
        # Calling init_game again sets the same positions without duplicating entries
        game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"])
        game.init_game()
        self.assertEqual(game.targets, [(3, 3)])
        self.assertEqual(game.boxes, [(2, 2)])
        self.assertEqual(game.player_row, 1)
        self.assertEqual(game.player_col, 1)

    def test_init_game_5(self):
        # Single-row map: positions are reported as (row, col) tuples at the edge
        game = PushBoxGame(["OXG"])
        self.assertEqual(game.player_row, 0)
        self.assertEqual(game.player_col, 0)
        self.assertEqual(game.boxes, [(0, 1)])
        self.assertEqual(game.targets, [(0, 2)])

import unittest

class AgentTest_check_win(unittest.TestCase):

    def test_check_win_1(self):
        # Initial state from the class docstring: the box is not on its target
        game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"])
        self.assertFalse(game.check_win())
        self.assertFalse(game.is_game_over)

    def test_check_win_2(self):
        # Single box placed on the single target wins the game
        game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"])
        game.boxes = [(3, 3)]
        self.assertTrue(game.check_win())
        self.assertTrue(game.is_game_over)

    def test_check_win_3(self):
        # Two boxes, only one of them on a target: not won
        game = PushBoxGame(["######", "#O   #", "# X G#", "# X G#", "######"])
        game.boxes = [(2, 4), (2, 2)]
        self.assertFalse(game.check_win())
        self.assertFalse(game.is_game_over)

    def test_check_win_4(self):
        # Two boxes, both placed on targets: won
        game = PushBoxGame(["######", "#O   #", "# X G#", "# X G#", "######"])
        game.boxes = [(2, 4), (3, 4)]
        self.assertTrue(game.check_win())
        self.assertTrue(game.is_game_over)

    def test_check_win_5(self):
        # is_game_over is updated on every call: won first, then a box leaves its target
        game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"])
        game.boxes = [(3, 3)]
        self.assertTrue(game.check_win())
        self.assertTrue(game.is_game_over)
        game.boxes = [(2, 2)]
        self.assertFalse(game.check_win())
        self.assertFalse(game.is_game_over)

import unittest

class AgentTest_move(unittest.TestCase):

    def test_move_1(self):
        # Moving onto an empty floor cell changes the player position and does not win
        game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"])
        result = game.move('d')
        self.assertFalse(result)
        self.assertEqual(game.player_row, 1)
        self.assertEqual(game.player_col, 2)
        self.assertEqual(game.boxes, [(2, 2)])

    def test_move_2(self):
        # Moving into a wall leaves the player where it was
        game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"])
        result = game.move('a')
        self.assertFalse(result)
        self.assertEqual(game.player_row, 1)
        self.assertEqual(game.player_col, 1)
        self.assertEqual(game.boxes, [(2, 2)])

    def test_move_3(self):
        # Moving into a box pushes the box one cell further in the same direction
        game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"])
        game.move('d')
        result = game.move('s')
        self.assertFalse(result)
        self.assertEqual(game.player_row, 2)
        self.assertEqual(game.player_col, 2)
        self.assertEqual(game.boxes, [(3, 2)])

    def test_move_4(self):
        # The sequence from the move docstring: the last push places the box on the target and wins
        game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"])
        self.assertFalse(game.move('d'))
        self.assertFalse(game.move('s'))
        self.assertFalse(game.move('a'))
        self.assertFalse(game.move('s'))
        result = game.move('d')
        self.assertTrue(result)
        self.assertTrue(game.is_game_over)
        self.assertEqual(game.player_row, 3)
        self.assertEqual(game.player_col, 2)
        self.assertEqual(game.boxes, [(3, 3)])

    def test_move_5(self):
        # A box cannot be pushed into a wall: neither the box nor the player moves
        game = PushBoxGame(["#####", "#OX##", "#  G#", "#####"])
        result = game.move('d')
        self.assertFalse(result)
        self.assertEqual(game.player_row, 1)
        self.assertEqual(game.player_col, 1)
        self.assertEqual(game.boxes, [(1, 2)])