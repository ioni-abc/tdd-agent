import unittest



class BlackjackGameTestCreateDeck(unittest.TestCase):
    def setUp(self):
        self.blackjackGame = BlackjackGame()
        self.deck = self.blackjackGame.deck

    def test_create_deck_1(self):
        self.assertEqual(len(self.deck), 52)

    def test_create_deck_2(self):
        suits = ['S', 'C', 'D', 'H']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in suits:
            for rank in ranks:
                self.assertIn(rank + suit, self.deck)

    def test_create_deck_3(self):
        suits = ['S', 'C', 'D', 'H']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9']
        for suit in suits:
            for rank in ranks:
                self.assertIn(rank + suit, self.deck)

import unittest

class AgentTest_create_deck(unittest.TestCase):
    def test_create_deck_1(self):
        game = BlackjackGame()
        deck = game.create_deck()
        self.assertIsInstance(deck, list)
        self.assertEqual(len(set(deck)), 52)
        for card in deck:
            self.assertIsInstance(card, str)
            self.assertNotIn(card, ['JOKER', 'JK', 'BJ', 'RJ'])

    def test_create_deck_2(self):
        decks = [BlackjackGame().create_deck() for _ in range(5)]
        sorted_reference = sorted(decks[0])
        orders = {tuple(deck) for deck in decks}
        self.assertGreater(len(orders), 1)
        for deck in decks:
            self.assertEqual(sorted(deck), sorted_reference)

class BlackjackGameTestCalculateHandValue(unittest.TestCase):
    def test_calculate_hand_value_1(self):
        blackjackGame = BlackjackGame()
        hand = ['2S', '3S', '4S', '5S']
        self.assertEqual(blackjackGame.calculate_hand_value(hand), 14)

    def test_calculate_hand_value_2(self):
        blackjackGame = BlackjackGame()
        hand = ['2S', '3S', 'JS', 'QS']
        self.assertEqual(blackjackGame.calculate_hand_value(hand), 25)

    def test_calculate_hand_value_3(self):
        blackjackGame = BlackjackGame()
        hand = ['2S', '3S', '4S', 'AS']
        self.assertEqual(blackjackGame.calculate_hand_value(hand), 20)

    def test_calculate_hand_value_4(self):
        blackjackGame = BlackjackGame()
        hand = ['JS', 'QS', '4S', 'AS']
        self.assertEqual(blackjackGame.calculate_hand_value(hand), 25)

import unittest

class AgentTest_calculate_hand_value(unittest.TestCase):
    def test_calculate_hand_value_1(self):
        blackjackGame = BlackjackGame()
        hand = ['AS', 'AH', '9D']
        self.assertEqual(blackjackGame.calculate_hand_value(hand), 21)

    def test_calculate_hand_value_2(self):
        blackjackGame = BlackjackGame()
        hand = ['10S', 'JS', 'QS']
        self.assertEqual(blackjackGame.calculate_hand_value(hand), 30)

class BlackjackGameTestCheckWinner(unittest.TestCase):
    def setUp(self):
        self.blackjackGame = BlackjackGame()

    def test_check_winner_1(self):
        player_hand = ['2S', 'JS', 'QS']
        dealer_hand = ['7S', '9S']
        self.assertEqual(self.blackjackGame.check_winner(player_hand, dealer_hand), 'Dealer wins')

    def test_check_winner_2(self):
        player_hand = ['2S', '4S', '5S']
        dealer_hand = ['2S', 'JS', 'QS']
        self.assertEqual(self.blackjackGame.check_winner(player_hand, dealer_hand), 'Player wins')

    def test_check_winner_3(self):
        player_hand = ['3S', 'JS', 'QS']
        dealer_hand = ['2S', 'JS', 'QS']
        self.assertEqual(self.blackjackGame.check_winner(player_hand, dealer_hand), 'Dealer wins')

    def test_check_winner_4(self):
        player_hand = ['2S', 'JS', 'QS']
        dealer_hand = ['3S', 'JS', 'QS']
        self.assertEqual(self.blackjackGame.check_winner(player_hand, dealer_hand), 'Player wins')

import unittest

class AgentTest_check_winner(unittest.TestCase):
    def test_check_winner_1(self):
        # Both hands are 21 or under: the hand closer to 21 wins.
        # Player = 10 + 7 = 17, dealer = 10 + 9 = 19, so the dealer is closer.
        game = BlackjackGame()
        player_hand = ['10S', '7S']
        dealer_hand = ['10H', '9H']
        self.assertEqual(game.check_winner(player_hand, dealer_hand), 'Dealer wins')

    def test_check_winner_2(self):
        # Both hands exceed 21: the one with the lower hand value wins.
        # Player = 10 + J + 5 = 25, dealer = 10 + Q + 9 = 29, so the player is lower.
        game = BlackjackGame()
        player_hand = ['10S', 'JS', '5S']
        dealer_hand = ['10H', 'QH', '9H']
        self.assertEqual(game.check_winner(player_hand, dealer_hand), 'Player wins')