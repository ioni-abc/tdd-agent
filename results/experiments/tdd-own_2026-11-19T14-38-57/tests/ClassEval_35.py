import unittest


import unittest

class AgentTest_find_blank(unittest.TestCase):

    def test_find_blank_1(self):
        # Example from the find_blank docstring
        eightPuzzle = EightPuzzle([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        result = eightPuzzle.find_blank([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        self.assertEqual(result, (2, 1))

    def test_find_blank_2(self):
        # Blank in the top-left corner
        eightPuzzle = EightPuzzle([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        result = eightPuzzle.find_blank([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        self.assertEqual(result, (0, 0))

    def test_find_blank_3(self):
        # Blank in the top-right corner
        eightPuzzle = EightPuzzle([[1, 2, 0], [3, 4, 5], [6, 7, 8]])
        result = eightPuzzle.find_blank([[1, 2, 0], [3, 4, 5], [6, 7, 8]])
        self.assertEqual(result, (0, 2))

    def test_find_blank_4(self):
        # Blank in the centre of the board
        eightPuzzle = EightPuzzle([[1, 2, 3], [4, 0, 6], [7, 8, 5]])
        result = eightPuzzle.find_blank([[1, 2, 3], [4, 0, 6], [7, 8, 5]])
        self.assertEqual(result, (1, 1))

    def test_find_blank_5(self):
        # find_blank must inspect the state passed as argument,
        # not the state stored as initial_state
        eightPuzzle = EightPuzzle([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        result = eightPuzzle.find_blank([[0, 2, 3], [1, 4, 5], [6, 7, 8]])
        self.assertEqual(result, (0, 0))

import unittest

class AgentTest_move(unittest.TestCase):

    def test_move_1(self):
        # Example from the move docstring: blank at (2, 1) moves left
        eightPuzzle = EightPuzzle([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        result = eightPuzzle.move([[2, 3, 4], [5, 8, 1], [6, 0, 7]], 'left')
        self.assertEqual(result, [[2, 3, 4], [5, 8, 1], [0, 6, 7]])

    def test_move_2(self):
        # Blank at (2, 1) moves right, swapping with the 8 at (2, 2)
        eightPuzzle = EightPuzzle([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
        result = eightPuzzle.move([[1, 2, 3], [4, 5, 6], [7, 0, 8]], 'right')
        self.assertEqual(result, [[1, 2, 3], [4, 5, 6], [7, 8, 0]])

    def test_move_3(self):
        # Blank at (2, 1) moves up, swapping with the 8 at (1, 1)
        eightPuzzle = EightPuzzle([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        result = eightPuzzle.move([[2, 3, 4], [5, 8, 1], [6, 0, 7]], 'up')
        self.assertEqual(result, [[2, 3, 4], [5, 0, 1], [6, 8, 7]])

    def test_move_4(self):
        # Blank at (0, 0) moves down, swapping with the 3 at (1, 0)
        eightPuzzle = EightPuzzle([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        result = eightPuzzle.move([[0, 1, 2], [3, 4, 5], [6, 7, 8]], 'down')
        self.assertEqual(result, [[3, 1, 2], [0, 4, 5], [6, 7, 8]])

    def test_move_5(self):
        # move must act on the state passed as argument,
        # not on the state stored as initial_state
        eightPuzzle = EightPuzzle([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        result = eightPuzzle.move([[1, 2, 0], [3, 4, 5], [6, 7, 8]], 'left')
        self.assertEqual(result, [[1, 0, 2], [3, 4, 5], [6, 7, 8]])

class AgentTest_get_possible_moves(unittest.TestCase):

    def test_get_possible_moves_1(self):
        # Example from the get_possible_moves docstring: blank at (2, 1)
        # can move up, left or right, but not down (off the board)
        eightPuzzle = EightPuzzle([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        result = eightPuzzle.get_possible_moves([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        self.assertIsInstance(result, list)
        self.assertCountEqual(result, ['up', 'left', 'right'])

    def test_get_possible_moves_2(self):
        # Blank in the top-left corner: only down and right are possible
        eightPuzzle = EightPuzzle([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        result = eightPuzzle.get_possible_moves([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        self.assertIsInstance(result, list)
        self.assertCountEqual(result, ['down', 'right'])

    def test_get_possible_moves_3(self):
        # Blank in the top-right corner: only down and left are possible
        eightPuzzle = EightPuzzle([[1, 2, 0], [3, 4, 5], [6, 7, 8]])
        result = eightPuzzle.get_possible_moves([[1, 2, 0], [3, 4, 5], [6, 7, 8]])
        self.assertIsInstance(result, list)
        self.assertCountEqual(result, ['down', 'left'])

    def test_get_possible_moves_4(self):
        # Blank in the centre of the board: all four directions are possible
        eightPuzzle = EightPuzzle([[1, 2, 3], [4, 0, 6], [7, 8, 5]])
        result = eightPuzzle.get_possible_moves([[1, 2, 3], [4, 0, 6], [7, 8, 5]])
        self.assertIsInstance(result, list)
        self.assertCountEqual(result, ['up', 'down', 'left', 'right'])

    def test_get_possible_moves_5(self):
        # get_possible_moves must inspect the state passed as argument,
        # not the state stored as initial_state (blank at the centre there)
        eightPuzzle = EightPuzzle([[1, 2, 3], [4, 0, 6], [7, 8, 5]])
        result = eightPuzzle.get_possible_moves([[0, 2, 3], [1, 4, 5], [6, 7, 8]])
        self.assertIsInstance(result, list)
        self.assertCountEqual(result, ['down', 'right'])

import unittest

class AgentTest_solve(unittest.TestCase):

    def test_solve_1(self):
        # Example from the solve docstring: one move to the right reaches the goal
        eightPuzzle = EightPuzzle([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
        result = eightPuzzle.solve()
        self.assertEqual(result, ['right'])

    def test_solve_2(self):
        # Blank at (1, 2) needs a single move down to reach the goal state
        eightPuzzle = EightPuzzle([[1, 2, 3], [4, 5, 0], [7, 8, 6]])
        result = eightPuzzle.solve()
        self.assertEqual(result, ['down'])

    def test_solve_3(self):
        # BFS must return the shortest path: two moves (right, down) is the only
        # two-move solution from this state
        eightPuzzle = EightPuzzle([[1, 2, 3], [4, 0, 5], [7, 8, 6]])
        result = eightPuzzle.solve()
        self.assertEqual(result, ['right', 'down'])

    def test_solve_4(self):
        # BFS must return the shortest path: blank at (2, 0) must move right twice
        eightPuzzle = EightPuzzle([[1, 2, 3], [4, 5, 6], [0, 7, 8]])
        result = eightPuzzle.solve()
        self.assertEqual(result, ['right', 'right'])

    def test_solve_5(self):
        # The returned path is a list of direction strings which, applied in order
        # from the initial state using move, leads to the goal state.
        # This state is four moves away from the goal, which is the minimum possible.
        start = [[0, 1, 3], [4, 2, 5], [7, 8, 6]]
        eightPuzzle = EightPuzzle(start)
        result = eightPuzzle.solve()

        self.assertIsInstance(result, list)
        for direction in result:
            self.assertIsInstance(direction, str)
            self.assertIn(direction, ['up', 'down', 'left', 'right'])
        self.assertEqual(len(result), 4)

        state = start
        for direction in result:
            self.assertIn(direction, eightPuzzle.get_possible_moves(state))
            state = eightPuzzle.move(state, direction)
        self.assertEqual(state, eightPuzzle.goal_state)