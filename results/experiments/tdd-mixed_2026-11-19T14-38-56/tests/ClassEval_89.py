import unittest




class TwentyFourPointGameTestGetMyCards(unittest.TestCase):
    def test_get_my_cards_1(self):
        game = TwentyFourPointGame()
        cards = game.get_my_cards()
        self.assertEqual(len(cards), 4)
        for card in cards:
            self.assertIn(card, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_get_my_cards_2(self):
        game = TwentyFourPointGame()
        cards = game.get_my_cards()
        self.assertEqual(len(cards), 4)
        for card in cards:
            self.assertIn(card, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_get_my_cards_3(self):
        game = TwentyFourPointGame()
        cards = game.get_my_cards()
        self.assertEqual(len(cards), 4)
        for card in cards:
            self.assertIn(card, [1, 2, 3, 4, 5, 6, 7, 8, 9])

import random

import unittest

class AgentTest__generate_cards(unittest.TestCase):
    def _run_generate(self, game):
        result = game._generate_cards()
        if result is None:
            return list(game.nums)
        return list(result)

    def test__generate_cards_1(self):
        game = TwentyFourPointGame()
        cards = self._run_generate(game)
        self.assertEqual(len(cards), 4)
        for card in cards:
            self.assertIsInstance(card, int)
            self.assertNotIsInstance(card, bool)

    def test__generate_cards_2(self):
        game = TwentyFourPointGame()
        hands = set()
        for _ in range(50):
            cards = self._run_generate(game)
            self.assertEqual(len(cards), 4)
            hands.add(tuple(cards))
        self.assertGreater(len(hands), 1)

class TwentyFourPointGameTestAnswer(unittest.TestCase):
    def test_answer_1(self):
        game = TwentyFourPointGame()
        cards = game.answer('pass')
        self.assertEqual(len(cards), 4)

    def test_answer_2(self):
        game = TwentyFourPointGame()
        result = game.answer('4*3+6+6')
        self.assertTrue(result)

    def test_answer_3(self):
        game = TwentyFourPointGame()
        result = game.answer('1+1+1+1')
        self.assertFalse(result)

    def test_answer_4(self):
        game = TwentyFourPointGame()
        result = game.answer('1+')
        self.assertFalse(result)

    def test_answer_5(self):
        game = TwentyFourPointGame()
        result = game.answer('abc')
        self.assertFalse(result)

class AgentTest_get_my_cards(unittest.TestCase):
    def test_get_my_cards_1(self):
        game = TwentyFourPointGame()
        cards = game.get_my_cards()
        self.assertIsInstance(cards, list)
        for card in cards:
            self.assertIsInstance(card, int)
            self.assertNotIsInstance(card, bool)

    def test_get_my_cards_2(self):
        game = TwentyFourPointGame()
        hands = set()
        for _ in range(50):
            cards = game.get_my_cards()
            self.assertEqual(len(cards), 4)
            hands.add(tuple(cards))
        self.assertGreater(len(hands), 1)

class TwentyFourPointGameTest(unittest.TestCase):
    def test_TwentyFourPointGame(self):
        game = TwentyFourPointGame()
        cards = game.get_my_cards()
        self.assertEqual(len(cards), 4)
        for card in cards:
            self.assertIn(card, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        game.nums = [4, 3, 6, 6]
        result = game.answer('4*3+6+6')
        self.assertTrue(result)
        result = game.evaluate_expression('4*3+6+6')
        self.assertTrue(result)

class TwentyFourPointGameTestEvaluateExpression(unittest.TestCase):
    def test_evaluate_expression_1(self):
        game = TwentyFourPointGame()
        result = game.evaluate_expression('4+3+6+6')
        self.assertFalse(result)

    def test_evaluate_expression_2(self):
        game = TwentyFourPointGame()
        result = game.evaluate_expression('4*3+6+6')
        self.assertTrue(result)

    def test_evaluate_expression_3(self):
        game = TwentyFourPointGame()
        result = game.evaluate_expression('1+1+1+1')
        self.assertFalse(result)

import unittest

class AgentTest_answer(unittest.TestCase):
    def test_answer_1(self):
        game = TwentyFourPointGame()
        game.nums = [2, 3, 4, 5]
        result = game.answer('2*(3+4+5)')
        self.assertTrue(result)

    def test_answer_2(self):
        game = TwentyFourPointGame()
        game.nums = [1, 2, 3, 4]
        result = game.answer('6*4')
        self.assertFalse(result)