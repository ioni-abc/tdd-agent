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
        self.expr = "".join(
            ch for ch in self.expr
            if ch in self.left_brackets or ch in self.right_brackets
        )

    def check_balanced_brackets(self):
        """
        Checks if the expression has balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets()
        True

        """
        pairs = {")": "(", "}": "{", "]": "["}
        self.stack = []
        for ch in self.expr:
            if ch in self.left_brackets:
                self.stack.append(ch)
            elif ch in self.right_brackets:
                if not self.stack or self.stack[-1] != pairs[ch]:
                    return False
                self.stack.pop()
        return len(self.stack) == 0