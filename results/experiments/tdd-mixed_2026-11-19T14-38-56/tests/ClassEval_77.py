import unittest




class SnakeTestRandomFoodPosition(unittest.TestCase):
    def test_random_food_position_1(self):
        snake = Snake(100, 100, 1, (51, 51))
        self.assertEqual(snake.food_position, (51, 51))
        snake.random_food_position()
        self.assertNotIn(snake.food_position, snake.positions)
        self.assertGreaterEqual(snake.food_position[0], 0)
        self.assertGreaterEqual(snake.food_position[1], 0)
        self.assertLessEqual(snake.food_position[0], 100)
        self.assertLessEqual(snake.food_position[1], 100)

    def test_random_food_position_2(self):
        snake = Snake(100, 100, 1, (99, 99))
        self.assertEqual(snake.food_position, (99, 99))
        snake.random_food_position()
        self.assertNotIn(snake.food_position, snake.positions)
        self.assertGreaterEqual(snake.food_position[0], 0)
        self.assertGreaterEqual(snake.food_position[1], 0)
        self.assertLessEqual(snake.food_position[0], 100)
        self.assertLessEqual(snake.food_position[1], 100)

    def test_random_food_position_3(self):
        snake = Snake(100, 100, 1, (0, 0))
        self.assertEqual(snake.food_position, (0, 0))
        snake.random_food_position()
        self.assertNotIn(snake.food_position, snake.positions)
        self.assertGreaterEqual(snake.food_position[0], 0)
        self.assertGreaterEqual(snake.food_position[1], 0)
        self.assertLessEqual(snake.food_position[0], 100)
        self.assertLessEqual(snake.food_position[1], 100)

import unittest

class AgentTest_random_food_position(unittest.TestCase):
    def test_random_food_position_1(self):
        snake = Snake(100, 100, 1, (51, 51))
        result = snake.random_food_position()
        self.assertIsNone(result)
        self.assertIsInstance(snake.food_position, tuple)
        self.assertEqual(len(snake.food_position), 2)

    def test_random_food_position_2(self):
        snake = Snake(10, 10, 1, (0, 0))
        snake.positions = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0)]
        for _ in range(200):
            snake.random_food_position()
            self.assertNotIn(snake.food_position, snake.positions)
            self.assertGreaterEqual(snake.food_position[0], 0)
            self.assertGreaterEqual(snake.food_position[1], 0)
            self.assertLessEqual(snake.food_position[0], 10)
            self.assertLessEqual(snake.food_position[1], 10)

class SnakeTestReset(unittest.TestCase):
    def test_reset_1(self):
        snake = Snake(100, 100, 1, (51, 51))
        snake.move((1, 1))
        snake.reset()
        self.assertEqual(snake.length, 1)
        self.assertEqual(snake.positions[0], (50, 50))
        self.assertEqual(snake.score, 0)

    def test_reset_2(self):
        snake = Snake(100, 100, 1, (51, 51))
        snake.move((0, 1))
        snake.reset()
        self.assertEqual(snake.length, 1)
        self.assertEqual(snake.positions[0], (50, 50))
        self.assertEqual(snake.score, 0)

    def test_reset_3(self):
        snake = Snake(100, 100, 1, (51, 51))
        snake.move((0, -1))
        snake.reset()
        self.assertEqual(snake.length, 1)
        self.assertEqual(snake.positions[0], (50, 50))
        self.assertEqual(snake.score, 0)

import unittest

from unittest.mock import patch

class AgentTest_reset(unittest.TestCase):
    def test_reset_1(self):
        snake = Snake(100, 100, 1, (51, 51))
        with patch.object(Snake, 'random_food_position') as mock_random_food:
            result = snake.reset()
        mock_random_food.assert_called_once_with()
        self.assertIsNone(result)

    def test_reset_2(self):
        snake = Snake(100, 100, 1, (51, 51))
        snake.length = 4
        snake.score = 300
        snake.positions = [(10, 10), (11, 10), (12, 10), (13, 10)]
        snake.reset()
        self.assertEqual(len(snake.positions), 1)
        self.assertEqual(snake.positions, [(50, 50)])
        self.assertNotIn(snake.food_position, snake.positions)
        self.assertGreaterEqual(snake.food_position[0], 0)
        self.assertGreaterEqual(snake.food_position[1], 0)
        self.assertLessEqual(snake.food_position[0], 100)
        self.assertLessEqual(snake.food_position[1], 100)

class SnakeTestEatFood(unittest.TestCase):
    def test_eat_food_1(self):
        snake = Snake(100, 100, 1, (51, 51))
        self.assertEqual(snake.length, 1)
        self.assertEqual(snake.score, 0)
        snake.eat_food()
        self.assertEqual(snake.length, 2)
        self.assertEqual(snake.score, 100)

    def test_eat_food_2(self):
        snake = Snake(100, 100, 1, (51, 51))
        self.assertEqual(snake.length, 1)
        self.assertEqual(snake.score, 0)
        snake.eat_food()
        snake.eat_food()
        self.assertEqual(snake.length, 3)
        self.assertEqual(snake.score, 200)

    def test_eat_food_3(self):
        snake = Snake(100, 100, 1, (51, 51))
        self.assertEqual(snake.length, 1)
        self.assertEqual(snake.score, 0)
        snake.eat_food()
        snake.eat_food()
        snake.eat_food()
        self.assertEqual(snake.length, 4)
        self.assertEqual(snake.score, 300)

import unittest

from unittest.mock import patch

class AgentTest_eat_food(unittest.TestCase):
    def test_eat_food_1(self):
        snake = Snake(100, 100, 1, (51, 51))
        with patch.object(Snake, 'random_food_position') as mock_random_food:
            result = snake.eat_food()
        mock_random_food.assert_called_once_with()
        self.assertIsNone(result)

    def test_eat_food_2(self):
        snake = Snake(10, 10, 1, (0, 0))
        snake.positions = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0)]
        for _ in range(200):
            snake.eat_food()
            self.assertIsInstance(snake.food_position, tuple)
            self.assertEqual(len(snake.food_position), 2)
            self.assertNotIn(snake.food_position, snake.positions)

class SnakeTestMove(unittest.TestCase):
    def test_move_1(self):
        snake = Snake(100, 100, 1, (51, 51))
        snake.move((1, 1))
        self.assertEqual(snake.length, 2)
        self.assertEqual(snake.positions[0], (51, 51))
        self.assertEqual(snake.positions[1], (50, 50))
        self.assertEqual(snake.score, 100)

    def test_move_2(self):
        snake = Snake(100, 100, 1, (80, 80))
        snake.move((1, 1))
        self.assertEqual(snake.length, 1)
        self.assertEqual(snake.positions[0], (51, 51))
        self.assertEqual(snake.score, 0)

    def test_move_3(self):
        snake = Snake(100, 100, 1, (51, 51))
        snake.move((1, 0))
        self.assertEqual(snake.length, 1)
        self.assertEqual(snake.positions[0], (51, 50))
        self.assertEqual(snake.score, 0)

class AgentTest_move(unittest.TestCase):
    def test_move_1(self):
        snake = Snake(100, 100, 1, (99, 99))
        snake.length = 4
        snake.score = 200
        snake.positions = [(50, 50), (51, 50), (51, 51), (50, 51)]
        snake.move((1, 0))
        self.assertEqual(snake.length, 1)
        self.assertEqual(snake.positions, [(50, 50)])
        self.assertEqual(snake.score, 0)

    def test_move_2(self):
        snake = Snake(100, 100, 1, (99, 99))
        snake.move((-1, -1))
        self.assertEqual(snake.length, 1)
        self.assertEqual(snake.positions[0], (49, 49))
        self.assertEqual(snake.score, 0)