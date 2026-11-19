import ast
import random
from fractions import Fraction


class _InvalidAnswer(list):
    """
    A falsy list of cards returned when the expression cannot be parsed.
    """

    def __bool__(self):
        return False


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
        self._generate_cards()
        return list(self.nums)


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
        try:
            tree = ast.parse(expression, mode='eval')
        except (SyntaxError, ValueError, TypeError):
            if not self.nums:
                self._generate_cards()
            return _InvalidAnswer(self.nums)

        numbers = [
            node.value
            for node in ast.walk(tree)
            if isinstance(node, ast.Constant)
            and isinstance(node.value, int)
            and not isinstance(node.value, bool)
        ]

        if self.nums and sorted(numbers) != sorted(self.nums):
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
        try:
            tree = ast.parse(expression, mode='eval')
            value = self._eval_node(tree.body)
        except (SyntaxError, ValueError, TypeError, ZeroDivisionError, KeyError):
            return False
        return value == 24


    def _eval_node(self, node):
        """
        Recursively evaluate a whitelisted AST node using exact fractions.
        """
        if isinstance(node, ast.Constant):
            if isinstance(node.value, bool) or not isinstance(node.value, (int, float)):
                raise ValueError("unsupported constant")
            return Fraction(node.value)
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            operand = self._eval_node(node.operand)
            return operand if isinstance(node.op, ast.UAdd) else -operand
        if isinstance(node, ast.BinOp):
            left = self._eval_node(node.left)
            right = self._eval_node(node.right)
            if isinstance(node.op, ast.Add):
                return left + right
            if isinstance(node.op, ast.Sub):
                return left - right
            if isinstance(node.op, ast.Mult):
                return left * right
            if isinstance(node.op, ast.Div):
                return left / right
        raise ValueError("unsupported expression")