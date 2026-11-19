import unittest


import unittest

import random

class AgentTest__generate_cards(unittest.TestCase):

    def test__generate_cards_1(self):
        game = TwentyFourPointGame()
        game._generate_cards()
        self.assertEqual(len(game.nums), 4)

    def test__generate_cards_2(self):
        game = TwentyFourPointGame()
        game._generate_cards()
        for card in game.nums:
            self.assertIsInstance(card, int)

    def test__generate_cards_3(self):
        game = TwentyFourPointGame()
        for _ in range(100):
            game._generate_cards()
            for card in game.nums:
                self.assertGreaterEqual(card, 1)
                self.assertLessEqual(card, 9)

    def test__generate_cards_4(self):
        game = TwentyFourPointGame()
        seen_hands = set()
        for _ in range(50):
            game._generate_cards()
            seen_hands.add(tuple(game.nums))
        self.assertGreater(len(seen_hands), 1)

    def test__generate_cards_5(self):
        game = TwentyFourPointGame()
        game._generate_cards()
        game._generate_cards()
        self.assertEqual(len(game.nums), 4)

import unittest

import random

class AgentTest_get_my_cards(unittest.TestCase):

    def test_get_my_cards_1(self):
        game = TwentyFourPointGame()
        cards = game.get_my_cards()
        self.assertIsInstance(cards, list)
        self.assertEqual(len(cards), 4)

    def test_get_my_cards_2(self):
        game = TwentyFourPointGame()
        cards = game.get_my_cards()
        for card in cards:
            self.assertIsInstance(card, int)

    def test_get_my_cards_3(self):
        game = TwentyFourPointGame()
        for _ in range(100):
            cards = game.get_my_cards()
            self.assertEqual(len(cards), 4)
            for card in cards:
                self.assertGreaterEqual(card, 1)
                self.assertLessEqual(card, 9)

    def test_get_my_cards_4(self):
        game = TwentyFourPointGame()
        seen_hands = set()
        for _ in range(50):
            seen_hands.add(tuple(game.get_my_cards()))
        self.assertGreater(len(seen_hands), 1)

    def test_get_my_cards_5(self):
        game = TwentyFourPointGame()
        first = game.get_my_cards()
        second = game.get_my_cards()
        self.assertIsNot(first, second)
        self.assertEqual(len(first), 4)
        self.assertEqual(len(second), 4)

import unittest

class AgentTest_evaluate_expression(unittest.TestCase):

    def test_evaluate_expression_1(self):
        game = TwentyFourPointGame()
        self.assertIs(game.evaluate_expression("4*3+6+6"), True)

    def test_evaluate_expression_2(self):
        game = TwentyFourPointGame()
        self.assertIs(game.evaluate_expression("4*3+6+5"), False)

    def test_evaluate_expression_3(self):
        game = TwentyFourPointGame()
        self.assertIs(game.evaluate_expression("6*(2+2)"), True)

    def test_evaluate_expression_4(self):
        game = TwentyFourPointGame()
        self.assertIs(game.evaluate_expression("2*2*2"), False)

    def test_evaluate_expression_5(self):
        game = TwentyFourPointGame()
        self.assertIs(game.evaluate_expression("(1+2+3)*4"), True)

import unittest

import random

class AgentTest_answer(unittest.TestCase):

    def test_answer_1(self):
        game = TwentyFourPointGame()
        game.nums = [4, 3, 6, 6]
        self.assertIs(game.answer("4*3+6+6"), True)

    def test_answer_2(self):
        game = TwentyFourPointGame()
        game.nums = [1, 2, 3, 4]
        self.assertIs(game.answer("(1+2+3)*4"), True)

    def test_answer_3(self):
        game = TwentyFourPointGame()
        game.nums = [4, 3, 6, 6]
        self.assertIs(game.answer("4*3*6+6"), False)

    def test_answer_4(self):
        game = TwentyFourPointGame()
        game.nums = [1, 2, 3, 4]
        result = game.answer("1+2+3+4")
        self.assertIsInstance(result, bool)
        self.assertIs(result, False)

    def test_answer_5(self):
        game = TwentyFourPointGame()
        game.nums = [6, 6, 6, 6]
        self.assertIs(game.answer("6+6+6+6"), True)