import unittest


import unittest

from collections import Counter

class AgentTest_create_deck(unittest.TestCase):

    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    SUITS = ['S', 'H', 'D', 'C']

    def test_create_deck_1(self):
        game = BlackjackGame()
        deck = game.create_deck()
        self.assertIsInstance(deck, list)
        self.assertEqual(len(deck), 52)

    def test_create_deck_2(self):
        game = BlackjackGame()
        deck = game.create_deck()
        expected = {rank + suit for rank in self.RANKS for suit in self.SUITS}
        self.assertEqual(len(set(deck)), 52)
        self.assertEqual(set(deck), expected)

    def test_create_deck_3(self):
        game = BlackjackGame()
        deck = game.create_deck()
        for card in deck:
            self.assertIsInstance(card, str)
            self.assertNotIn('JOKER', card.upper())
            suit = card[-1]
            rank = card[:-1]
            self.assertIn(suit, self.SUITS, f"Invalid suit in card {card!r}")
            self.assertIn(rank, self.RANKS, f"Invalid rank in card {card!r}")

    def test_create_deck_4(self):
        game = BlackjackGame()
        deck = game.create_deck()
        for card in ['AS', '2S', '10C', 'KD', 'JH', 'QC', '8D']:
            self.assertIn(card, deck)
        self.assertNotIn('10S10', deck)
        self.assertNotIn('1C', deck)
        self.assertEqual(Counter(deck)['AS'], 1)
        self.assertEqual(Counter(deck)['10C'], 1)

    def test_create_deck_5(self):
        game = BlackjackGame()
        deck_one = game.create_deck()
        deck_two = game.create_deck()
        self.assertEqual(len(deck_one), 52)
        self.assertEqual(len(deck_two), 52)
        self.assertNotEqual(deck_one, deck_two)
        self.assertNotEqual(deck_one, sorted(deck_one))

import unittest

class AgentTest_calculate_hand_value(unittest.TestCase):

    def test_calculate_hand_value_1(self):
        game = BlackjackGame()
        self.assertEqual(game.calculate_hand_value(['QD', '9D', 'JC', 'QH', 'AS']), 40)

    def test_calculate_hand_value_2(self):
        game = BlackjackGame()
        self.assertEqual(game.calculate_hand_value(['2H', '3D', '9C']), 14)
        self.assertEqual(game.calculate_hand_value(['2H', '3D', '10C']), 15)

    def test_calculate_hand_value_3(self):
        game = BlackjackGame()
        self.assertEqual(game.calculate_hand_value(['KS', 'QH', 'JD']), 30)
        self.assertEqual(game.calculate_hand_value(['KC']), 10)

    def test_calculate_hand_value_4(self):
        game = BlackjackGame()
        # Ace counted as 11 when the hand does not exceed 21
        self.assertEqual(game.calculate_hand_value(['AS', '9H']), 20)
        self.assertEqual(game.calculate_hand_value(['AS', 'KD']), 21)
        # Ace reduced to 1 when the hand would exceed 21
        self.assertEqual(game.calculate_hand_value(['AS', 'KD', '5C']), 16)

    def test_calculate_hand_value_5(self):
        game = BlackjackGame()
        # One ace reduced from 11 to 1 is enough to get to 21
        self.assertEqual(game.calculate_hand_value(['AS', 'AH', '9C']), 21)
        # Aces are reduced one at a time until the total is <= 21
        self.assertEqual(game.calculate_hand_value(['AS', 'AH', 'AD', 'AC']), 14)

class AgentTest_check_winner(unittest.TestCase):

    def test_check_winner_1(self):
        # Both hands are 21 or under; player's 20 is closer to 21 than dealer's 18
        game = BlackjackGame()
        self.assertEqual(game.check_winner(['KH', 'JD'], ['KS', '8C']), 'Player wins')

    def test_check_winner_2(self):
        # Both hands are 21 or under; dealer's 19 is closer to 21 than player's 17
        game = BlackjackGame()
        self.assertEqual(game.check_winner(['10H', '7D'], ['KS', '9C']), 'Dealer wins')

    def test_check_winner_3(self):
        # Player busts (25 > 21) while dealer stands at 17; the lower hand value wins
        game = BlackjackGame()
        self.assertEqual(game.check_winner(['KH', 'QD', '5S'], ['10C', '7H']), 'Dealer wins')

    def test_check_winner_4(self):
        # Dealer busts (25 > 21) while player stands at 18; the lower hand value wins
        game = BlackjackGame()
        self.assertEqual(game.check_winner(['10H', '8D'], ['KS', 'QC', '5D']), 'Player wins')

    def test_check_winner_5(self):
        # Both hands exceed 21; the lower hand value (player's 22 vs dealer's 25) wins
        game = BlackjackGame()
        self.assertEqual(game.check_winner(['KH', 'QD', '2S'], ['KC', 'QS', '5D']), 'Player wins')