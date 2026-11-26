# ClassEval_12

## Skeleton (what the agent sees)

```python
import random
class BlackjackGame:
    """
    This is a class representing a game of blackjack, which includes creating a deck, calculating the value of a hand, and determine the winner based on the hand values of the player and dealer.
    """

    def __init__(self):
        """
        Initialize the Blackjack Game with the attribute deck, player_hand and dealer_hand.
        While initializing deck attribute, call the create_deck method to generate.
        The deck stores 52 rondom order poker with the Jokers removed, format is ['AS', '2S', ...].
        player_hand is a list which stores player's hand cards.
        dealer_hand is is a list which stores dealer's hand cards.
        """
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        """
        Create a deck of 52 cards, which stores 52 rondom order poker with the Jokers removed.
        :return: a list of 52 rondom order poker with the Jokers removed, format is ['AS', '2S', ...].
        >>> black_jack_game = BlackjackGame()
        >>> black_jack_game.create_deck()
        ['QD', '9D', 'JC', 'QH', '2S', 'JH', '7D', '6H', '9S', '5C', '7H', 'QS', '5H',
        '6C', '7C', '3D', '10C', 'AD', '4C', '5D', 'AH', '2D', 'QC', 'KH', '9C', '9H',
        '4H', 'JS', '6S', '8H', '8C', '4S', '3H', '10H', '7S', '6D', '3C', 'KC', '3S',
        '2H', '10D', 'KS', '4D', 'AC', '10S', '2C', 'KD', '5S', 'JD', '8S', 'AS', '8D']
        """

    def calculate_hand_value(self, hand):
        """
        Calculate the value of the poker cards stored in hand list according to the rules of the Blackjack Game.
        If the card is a digit, its value is added to the total hand value.
        Value of J, Q, or K is 10, while Aces are worth 11.
        If the total hand value exceeds 21 and there are Aces present, one Ace is treated as having a value of 1 instead of 11,
        until the hand value is less than or equal to 21, or all Aces have been counted as value of 1.
        :param hand: list
        :return: the value of the poker cards stored in hand list, a number.
        >>> black_jack_game.calculate_hand_value(['QD', '9D', 'JC', 'QH', 'AS'])
        40
        """

    def check_winner(self, player_hand, dealer_hand):
        """
        Determines the winner of a game by comparing the hand values of the player and dealer.
        rule:
        If both players have hand values that are equal to or less than 21, the winner is the one whose hand value is closer to 21.
        Otherwise, the winner is the one with the lower hand value.
        :param player_hand: list
        :param dealer_hand: list
        :return: the result of the game, only two certain str: 'Dealer wins' or 'Player wins'
        >>> black_jack_game.check_winner(['QD', '9D', 'JC', 'QH', 'AS'], ['QD', '9D', 'JC', 'QH', '2S'])
        'Player wins'
        """
```

## Method `create_deck`

### Docstring

```python
def create_deck(self):
        """
        Create a deck of 52 cards, which stores 52 rondom order poker with the Jokers removed.
        :return: a list of 52 rondom order poker with the Jokers removed, format is ['AS', '2S', ...].
        >>> black_jack_game = BlackjackGame()
        >>> black_jack_game.create_deck()
        ['QD', '9D', 'JC', 'QH', '2S', 'JH', '7D', '6H', '9S', '5C', '7H', 'QS', '5H',
        '6C', '7C', '3D', '10C', 'AD', '4C', '5D', 'AH', '2D', 'QC', 'KH', '9C', '9H',
        '4H', 'JS', '6S', '8H', '8C', '4S', '3H', '10H', '7S', '6D', '3C', 'KC', '3S',
        '2H', '10D', 'KS', '4D', 'AC', '10S', '2C', 'KD', '5S', 'JD', '8S', 'AS', '8D']
        """
```

### Reference code (`solution_code`)

```python
def create_deck(self):
        deck = []
        suits = ['S', 'C', 'D', 'H']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in suits:
            for rank in ranks:
                deck.append(rank + suit)
        random.shuffle(deck)
        return deck
```

### Tests (`BlackjackGameTestCreateDeck`)

setUp (runs before each test):

```python
def setUp(self):
    self.blackjackGame = BlackjackGame()
    self.deck = self.blackjackGame.deck
```

**test_create_deck_1**: `stated`
- reason: The docstring says create_deck returns a list of 52 cards with the Jokers removed, which is the length the test checks on the deck the game builds.

```python
def test_create_deck_1(self):
    self.assertEqual(len(self.deck), 52)
```

**test_create_deck_2**: `unstated`
- reason: The test checks the `self.deck` attribute populated in the constructor, but the docstring only describes the return value of `create_deck`, so a correct implementation that doesn't store the result on the instance would fail.
- missing: The docstring should state that the game object's `deck` attribute is set to the same 52-card list when the object is constructed, and that this list contains every rank and suit combination.

```python
def test_create_deck_2(self):
    suits = ['S', 'C', 'D', 'H']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    for suit in suits:
        for rank in ranks:
            self.assertIn(rank + suit, self.deck)
```

**test_create_deck_3**: `other_inconsistency`
- reason: Test-method mismatch: the test never calls create_deck and instead checks the self.deck attribute populated in setUp, which the create_deck docstring does not describe.
- missing: The docstring should state that the constructor stores the generated deck in an instance attribute (self.deck) and that this stored deck is what callers read afterward.

```python
def test_create_deck_3(self):
    suits = ['S', 'C', 'D', 'H']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9']
    for suit in suits:
        for rank in ranks:
            self.assertIn(rank + suit, self.deck)
```

**test_create_deck_4**: `stated`
- reason: The docstring says the deck is 52 cards in the format like 'AS' and the example shows 10, J, Q and K in all four suits, so a correct implementation would contain every such card and pass the assertions.

```python
def test_create_deck_4(self):
    suits = ['S', 'C', 'D', 'H']
    ranks = ['10', 'J', 'Q', 'K']
    for suit in suits:
        for rank in ranks:
            self.assertIn(rank + suit, self.deck)
```

**test_create_deck_5**: `unstated`
- reason: The test reads a deck attribute populated at object construction rather than calling create_deck, and the docstring never says the constructor must store a deck, though a correct create_deck could still leave that attribute unset.
- missing: The docstring should state that creating the game object must also initialise the instance's stored deck with the full set of cards, so that code reading that attribute without calling the method sees the same 52 cards.

```python
def test_create_deck_5(self):
    suits = ['S', 'C', 'D', 'H']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9']
    for suit in suits:
        for rank in ranks:
            self.assertIn(rank + suit, self.deck)
```

## Method `calculate_hand_value`

### Docstring

```python
def calculate_hand_value(self, hand):
        """
        Calculate the value of the poker cards stored in hand list according to the rules of the Blackjack Game.
        If the card is a digit, its value is added to the total hand value.
        Value of J, Q, or K is 10, while Aces are worth 11.
        If the total hand value exceeds 21 and there are Aces present, one Ace is treated as having a value of 1 instead of 11,
        until the hand value is less than or equal to 21, or all Aces have been counted as value of 1.
        :param hand: list
        :return: the value of the poker cards stored in hand list, a number.
        >>> black_jack_game.calculate_hand_value(['QD', '9D', 'JC', 'QH', 'AS'])
        40
        """
```

### Reference code (`solution_code`)

```python
def calculate_hand_value(self, hand):
        value = 0
        num_aces = 0
        for card in hand:
            rank = card[:-1]
            if rank.isdigit():
                value += int(rank)
            elif rank in ['J', 'Q', 'K']:
                value += 10
            elif rank == 'A':
                value += 11
                num_aces += 1
        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1
        return value
```

### Tests (`BlackjackGameTestCalculateHandValue`)

**test_calculate_hand_value_1**: `stated`
- reason: The docstring says digit cards add their face value to the total, so a programmer would sum 2+3+4+5 to get 14, which is what the test expects.

```python
def test_calculate_hand_value_1(self):
    blackjackGame = BlackjackGame()
    hand = ['2S', '3S', '4S', '5S']
    self.assertEqual(blackjackGame.calculate_hand_value(hand), 14)
```

**test_calculate_hand_value_2**: `stated`
- reason: The docstring says digits add their value, J/Q/K count as 10, and the total is returned without any Ace adjustment when there are no Aces, so a programmer following it would compute 2+3+10+10 = 25 and pass.

```python
def test_calculate_hand_value_2(self):
    blackjackGame = BlackjackGame()
    hand = ['2S', '3S', 'JS', 'QS']
    self.assertEqual(blackjackGame.calculate_hand_value(hand), 25)
```

**test_calculate_hand_value_3**: `stated`
- reason: The docstring says digits add their value, J/Q/K count as 10, Aces count as 11, and an Ace drops to 1 only when the total exceeds 21, so a programmer would compute 9 + 11 = 20 and pass.

```python
def test_calculate_hand_value_3(self):
    blackjackGame = BlackjackGame()
    hand = ['2S', '3S', '4S', 'AS']
    self.assertEqual(blackjackGame.calculate_hand_value(hand), 20)
```

**test_calculate_hand_value_4**: `stated`
- reason: The docstring says that when the total exceeds 21 with Aces present, Aces drop from 11 to 1 until the total is at most 21 or all Aces are 1, so a programmer would reduce the single Ace to get 25 and stop because no Aces remain.

```python
def test_calculate_hand_value_4(self):
    blackjackGame = BlackjackGame()
    hand = ['JS', 'QS', '4S', 'AS']
    self.assertEqual(blackjackGame.calculate_hand_value(hand), 25)
```

**test_calculate_hand_value_5**: `stated`
- reason: Following the docstring, the five cards total 53 with three Aces at 11, and each Ace is downgraded to 1 until the total is at most 21 or all Aces are counted as 1, giving 23, which matches the test.

```python
def test_calculate_hand_value_5(self):
    blackjackGame = BlackjackGame()
    hand = ['JS', 'QS', 'AS', 'AS', 'AS']
    self.assertEqual(blackjackGame.calculate_hand_value(hand), 23)
```

**test_calculate_hand_value_6**: `unstated`
- reason: The docstring defines values only for digits, J/Q/K and A, so it does not say what a card with an unrecognised rank (here B and C) contributes, and a faithful implementation could raise an error or count it differently from the expected 20.
- missing: The docstring should state that any card whose rank is not a digit, J, Q, K or A adds nothing to the total (or should specify some other value or error behaviour for it).

```python
def test_calculate_hand_value_6(self):
    blackjackGame = BlackjackGame()
    hand = ['JS', 'QS', 'BS', 'CS']
    self.assertEqual(blackjackGame.calculate_hand_value(hand), 20)
```

## Method `check_winner`

### Docstring

```python
def check_winner(self, player_hand, dealer_hand):
        """
        Determines the winner of a game by comparing the hand values of the player and dealer.
        rule:
        If both players have hand values that are equal to or less than 21, the winner is the one whose hand value is closer to 21.
        Otherwise, the winner is the one with the lower hand value.
        :param player_hand: list
        :param dealer_hand: list
        :return: the result of the game, only two certain str: 'Dealer wins' or 'Player wins'
        >>> black_jack_game.check_winner(['QD', '9D', 'JC', 'QH', 'AS'], ['QD', '9D', 'JC', 'QH', '2S'])
        'Player wins'
        """
```

### Reference code (`solution_code`)

```python
def check_winner(self, player_hand, dealer_hand):
        player_value = self.calculate_hand_value(player_hand)
        dealer_value = self.calculate_hand_value(dealer_hand)
        if player_value > 21 and dealer_value > 21:
            if player_value <= dealer_value:
                return 'Player wins'
            else:
                return 'Dealer wins'
        elif player_value > 21:
            return 'Dealer wins'
        elif dealer_value > 21:
            return 'Player wins'
        else:
            if player_value <= dealer_value:
                return 'Dealer wins'
            else:
                return 'Player wins'
```

### Tests (`BlackjackGameTestCheckWinner`)

setUp (runs before each test):

```python
def setUp(self):
    self.blackjackGame = BlackjackGame()
```

**test_check_winner_1**: `stated`
- reason: The player's hand totals 22 (bust) and the dealer's 16, and the docstring's "otherwise, the lower hand value wins" rule gives "Dealer wins", which is what the test expects.

```python
def test_check_winner_1(self):
    player_hand = ['2S', 'JS', 'QS']
    dealer_hand = ['7S', '9S']
    self.assertEqual(self.blackjackGame.check_winner(player_hand, dealer_hand), 'Dealer wins')
```

**test_check_winner_2**: `stated`
- reason: The test's player hand totals 11 and the dealer's totals 22 (bust), so the docstring's "otherwise, the lower hand value wins" rule gives 'Player wins', matching the test and reference.

```python
def test_check_winner_2(self):
    player_hand = ['2S', '4S', '5S']
    dealer_hand = ['2S', 'JS', 'QS']
    self.assertEqual(self.blackjackGame.check_winner(player_hand, dealer_hand), 'Player wins')
```

**test_check_winner_3**: `stated`
- reason: The docstring's "Otherwise, the winner is the one with the lower hand value" rule covers the case where both hands exceed 21, and a programmer applying it would pick the dealer's 22 over the player's 23, matching the expected 'Dealer wins'.

```python
def test_check_winner_3(self):
    player_hand = ['3S', 'JS', 'QS']
    dealer_hand = ['2S', 'JS', 'QS']
    self.assertEqual(self.blackjackGame.check_winner(player_hand, dealer_hand), 'Dealer wins')
```

**test_check_winner_4**: `stated`
- reason: Both hands bust (player 22, dealer 23), and the docstring's "otherwise, the one with the lower hand value wins" rule gives 'Player wins', which is what the test expects.

```python
def test_check_winner_4(self):
    player_hand = ['2S', 'JS', 'QS']
    dealer_hand = ['3S', 'JS', 'QS']
    self.assertEqual(self.blackjackGame.check_winner(player_hand, dealer_hand), 'Player wins')
```

**test_check_winner_5**: `stated`
- reason: The docstring's rule that the hand closer to 21 wins (when both are at or under 21) yields 'Dealer wins' for this test's hands, whichever way the ace is valued.

```python
def test_check_winner_5(self):
    player_hand = ['2S', '3S', '5S']
    dealer_hand = ['AS', 'JS']
    self.assertEqual(self.blackjackGame.check_winner(player_hand, dealer_hand), 'Dealer wins')
```

**test_check_winner_6**: `stated`
- reason: With both hands at or under 21, the docstring says the hand closer to 21 wins, and the player's hand (21 or 12 depending on ace value) beats the dealer's 10 under either ace valuation, so the expected 'Player wins' follows from the docstring.

```python
def test_check_winner_6(self):
    player_hand = ['AS', 'JS']
    dealer_hand = ['2S', '3S', '5S']
    self.assertEqual(self.blackjackGame.check_winner(player_hand, dealer_hand), 'Player wins')
```

## Tests in no method's test class

### `BlackjackGameTestMain`

**test_main_1**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main_1(self):
    blackjackGame = BlackjackGame()
    deck = blackjackGame.deck
    suits = ['S', 'C', 'D', 'H']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    for suit in suits:
        for rank in ranks:
            self.assertIn(rank + suit, deck)
    player_hand = ['2S', 'JS', 'QS']
    dealer_hand = ['7S', '9S']
    self.assertEqual(blackjackGame.check_winner(player_hand, dealer_hand), 'Dealer wins')
```
