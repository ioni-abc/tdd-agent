import unittest


class BalancedBrackets:
    """
    This is a class that checks for bracket matching
    """

    def __init__(self, expr):
        """
        Initializes the class with an expression.
        :param expr: The expression to check for balanced brackets,str.
        """
        self.stack = []
        self.left_brackets = ["(", "{", "["]
        self.right_brackets = [")", "}", "]"]
        self.expr = expr

    def clear_expr(self):
        """
        Clears the expression of all characters that are not brackets.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.clear_expr()
        >>> b.expr
        '()'

        """
        brackets = self.left_brackets + self.right_brackets
        self.expr = "".join(ch for ch in self.expr if ch in brackets)

    def check_balanced_brackets(self):
        """
        Checks if the expression has balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets()
        True

        """
        pairs = {")": "(", "}": "{", "]": "["}
        stack = []
        for ch in self.expr:
            if ch in self.left_brackets:
                stack.append(ch)
            elif ch in self.right_brackets:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
        return not stack


class AgentTest_clear_expr(unittest.TestCase):

    def test_clear_expr_1(self):
        b = BalancedBrackets("a(b)c")
        b.clear_expr()
        self.assertEqual(b.expr, '()')

    def test_clear_expr_2(self):
        b = BalancedBrackets("([{}])")
        b.clear_expr()
        self.assertEqual(b.expr, "([{}])")

    def test_clear_expr_3(self):
        b = BalancedBrackets("abc 123 xyz")
        b.clear_expr()
        self.assertEqual(b.expr, "")

    def test_clear_expr_4(self):
        b = BalancedBrackets("x{ y [z] } w")
        b.clear_expr()
        self.assertEqual(b.expr, "{[]}")

    def test_clear_expr_5(self):
        b = BalancedBrackets("")
        result = b.clear_expr()
        self.assertEqual(b.expr, "")
        self.assertIsNone(result)