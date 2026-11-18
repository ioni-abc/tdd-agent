import random
import re


class TwentyFourPointGame:
    """
    This ia a game of twenty-four points, which provides to generate four numbers and check whether player's expression is equal to 24.
    """

    def __init__(self) -> None:
        self.nums = []


    def _generate_cards(self):
        """
        Generate random numbers between 1 and 9 for the cards.
        """
        self.nums = [random.randint(1, 9) for _ in range(4)]
        return self.nums


    def get_my_cards(self):
        """
        Get a list of four random numbers between 1 and 9 representing the player's cards.
        :return: list of integers, representing the player's cards
        >>> game = TwentyFourPointGame()
        >>> game.get_my_cards()

        """
        return self._generate_cards()


    def answer(self, expression):
        """
        Check if a given mathematical expression using the cards can evaluate to 24.
        :param expression: string, mathematical expression using the cards
        :return: bool, True if the expression evaluates to 24, False otherwise
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.answer(ans)
        True
        """
        if not isinstance(expression, str):
            return False

        # 'pass' means the player gives up: reveal the current cards.
        if expression.strip().lower() == 'pass':
            if not self.nums:
                self._generate_cards()
            return self.nums

        # If cards have been dealt, the expression must use exactly those cards.
        if self.nums:
            used = sorted(int(n) for n in re.findall(r'\d+', expression))
            if used != sorted(self.nums):
                return False

        return self.evaluate_expression(expression)


    def evaluate_expression(self, expression):
        """
        Evaluate a mathematical expression and check if the result is 24.
        :param expression: string, mathematical expression
        :return: bool, True if the expression evaluates to 24, False otherwise
        >>> game = TwentyFourPointGame()
        >>> nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.evaluate_expression(ans)
        True
        """
        if not isinstance(expression, str) or not expression.strip():
            return False

        # Only digits, whitespace, parentheses and basic arithmetic operators are allowed.
        if not re.fullmatch(r'[\d\s+\-*/().]+', expression):
            return False

        try:
            result = eval(expression, {"__builtins__": {}}, {})
        except Exception:
            return False

        if isinstance(result, bool) or not isinstance(result, (int, float)):
            return False

        return abs(result - 24) < 1e-6