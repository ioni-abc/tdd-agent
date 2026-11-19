import unittest


import unittest

import random

class AgentTest_random_food_position(unittest.TestCase):

    def test_random_food_position_1(self):
        snake = Snake(100, 100, 1, (51, 51))
        result = snake.random_food_position()
        self.assertIsNone(result)

    def test_random_food_position_2(self):
        snake = Snake(100, 100, 1, (51, 51))
        snake.random_food_position()
        self.assertIsInstance(snake.food_position, tuple)
        self.assertEqual(len(snake.food_position), 2)
        self.assertIsInstance(snake.food_position[0], (int, float))
        self.assertIsInstance(snake.food_position[1], (int, float))

    def test_random_food_position_3(self):
        snake = Snake(100, 100, 1, (51, 51))
        for _ in range(100):
            snake.random_food_position()
            self.assertNotEqual(snake.food_position, snake.positions[0])

    def test_random_food_position_4(self):
        snake = Snake(100, 100, 1, (0, 0))
        snake.positions = [(10, 10), (11, 10), (12, 10), (13, 10), (13, 11), (13, 12)]
        for _ in range(200):
            snake.random_food_position()
            self.assertNotIn(snake.food_position, snake.positions)

    def test_random_food_position_5(self):
        snake = Snake(100, 100, 1, (51, 51))
        seen = set()
        for _ in range(50):
            snake.random_food_position()
            seen.add(snake.food_position)
        self.assertGreater(len(seen), 1)

import unittest

from unittest.mock import patch

class AgentTest_reset(unittest.TestCase):

    def test_reset_1(self):
        snake = Snake(100, 100, 1, (51, 51))
        result = snake.reset()
        self.assertIsNone(result)

    def test_reset_2(self):
        snake = Snake(100, 100, 1, (51, 51))
        snake.length = 5
        snake.positions = [(10, 10), (11, 10), (12, 10), (13, 10), (13, 11)]
        snake.reset()
        self.assertEqual(snake.length, 1)
        self.assertEqual(snake.positions, [(50, 50)])

    def test_reset_3(self):
        snake = Snake(100, 100, 1, (51, 51))
        snake.score = 300
        snake.reset()
        self.assertEqual(snake.score, 0)

    def test_reset_4(self):
        snake = Snake(100, 100, 1, (51, 51))
        with patch.object(Snake, 'random_food_position') as mock_rfp:
            snake.reset()
            mock_rfp.assert_called_once()

    def test_reset_5(self):
        snake = Snake(100, 100, 1, (0, 0))
        snake.positions = [(10, 10), (11, 10), (12, 10)]
        snake.length = 3
        for _ in range(100):
            snake.reset()
            self.assertIsInstance(snake.food_position, tuple)
            self.assertEqual(len(snake.food_position), 2)
            self.assertNotIn(snake.food_position, snake.positions)
            self.assertNotEqual(snake.food_position, snake.positions[0])

import unittest

import random

from unittest.mock import patch

class AgentTest_eat_food(unittest.TestCase):

    def test_eat_food_1(self):
        snake = Snake(100, 100, 1, (51, 51))
        result = snake.eat_food()
        self.assertIsNone(result)

    def test_eat_food_2(self):
        snake = Snake(100, 100, 1, (51, 51))
        self.assertEqual(snake.length, 1)
        snake.eat_food()
        self.assertEqual(snake.length, 2)

    def test_eat_food_3(self):
        snake = Snake(100, 100, 1, (51, 51))
        snake.length = 3
        snake.eat_food()
        self.assertEqual(snake.length, 4)

    def test_eat_food_4(self):
        snake = Snake(100, 100, 1, (51, 51))
        self.assertEqual(snake.score, 0)
        snake.eat_food()
        self.assertEqual(snake.score, 100)
        snake.score = 50
        snake.eat_food()
        self.assertEqual(snake.score, 150)

    def test_eat_food_5(self):
        snake = Snake(100, 100, 1, (0, 0))
        snake.positions = [(10, 10), (11, 10), (12, 10)]
        snake.length = 3
        for _ in range(100):
            snake.eat_food()
            self.assertIsInstance(snake.food_position, tuple)
            self.assertEqual(len(snake.food_position), 2)
            self.assertNotIn(snake.food_position, snake.positions)

import unittest

import random

from unittest.mock import patch

class AgentTest_move(unittest.TestCase):

    def test_move_1(self):
        snake = Snake(100, 100, 1, (0, 0))
        result = snake.move((1, 0))
        self.assertIsNone(result)

    def test_move_2(self):
        snake = Snake(100, 100, 1, (0, 0))
        snake.move((1, 0))
        self.assertEqual(snake.positions[0], (51, 50))

    def test_move_3(self):
        snake = Snake(100, 100, 1, (0, 0))
        snake.move((-2, 3))
        self.assertEqual(snake.positions[0], (48, 53))

    def test_move_4(self):
        snake = Snake(100, 100, 1, (51, 51))
        self.assertEqual(snake.length, 1)
        self.assertEqual(snake.score, 0)
        snake.move((1, 1))
        self.assertEqual(snake.length, 2)
        self.assertGreater(snake.score, 0)

    def test_move_5(self):
        snake = Snake(100, 100, 1, (0, 0))
        snake.length = 4
        snake.positions = [(50, 50), (50, 51), (51, 51), (51, 50)]
        snake.score = 300
        snake.move((1, 0))
        self.assertEqual(snake.length, 1)
        self.assertEqual(snake.score, 0)
        self.assertEqual(snake.positions, [(50, 50)])