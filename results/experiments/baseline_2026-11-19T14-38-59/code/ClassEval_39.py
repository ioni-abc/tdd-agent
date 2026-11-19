from collections import deque


class ExpressionCalculator:
    """
    This is a class in Python that can perform calculations with basic arithmetic operations, including addition, subtraction, multiplication, division, and modulo.
    """

    def __init__(self):
        """
        Initialize the expression calculator
        """
        self.postfix_stack = deque()
        self.operat_priority = [0, 3, 2, 1, -1, 1, 0, 2]

    # Priority table used for comparing operators.
    _PRIORITY = {
        '(': 0,
        ')': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '%': 2,
    }

    def calculate(self, expression):
        """
        Calculate the result of the given postfix expression
        :param expression: string, the postfix expression to be calculated
        :return: float, the calculated result
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.calculate("2 + 3 * 4")
        14.0

        """
        self.prepare(expression)
        stack = []
        while self.postfix_stack:
            token = self.postfix_stack.popleft()
            if self.is_operator(token) and token not in '()':
                second = stack.pop()
                first = stack.pop()
                stack.append(float(self._calculate(first, second, token)))
            else:
                stack.append(float(token))
        return float(stack[-1])

    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
        s = self.transform(expression)
        tokens = []
        i = 0
        n = len(s)
        while i < n:
            c = s[i]
            if c.isdigit() or c == '.':
                j = i + 1
                while j < n and (s[j].isdigit() or s[j] == '.'):
                    j += 1
                tokens.append(s[i:j])
                i = j
            elif (c == '-' and (i == 0 or s[i - 1] in '(+-*/%')
                  and i + 1 < n and (s[i + 1].isdigit() or s[i + 1] == '.')):
                j = i + 1
                while j < n and (s[j].isdigit() or s[j] == '.'):
                    j += 1
                tokens.append(s[i:j])
                i = j
            else:
                tokens.append(c)
                i += 1

        self.postfix_stack = deque()
        ops = []
        for tok in tokens:
            if not self.is_operator(tok):
                self.postfix_stack.append(tok)
            elif tok == '(':
                ops.append(tok)
            elif tok == ')':
                while ops and ops[-1] != '(':
                    self.postfix_stack.append(ops.pop())
                if ops:
                    ops.pop()
            else:
                while ops and ops[-1] != '(' and self.compare(ops[-1], tok):
                    self.postfix_stack.append(ops.pop())
                ops.append(tok)
        while ops:
            op = ops.pop()
            if op != '(':
                self.postfix_stack.append(op)

    @staticmethod
    def is_operator(c):
        """
        Check if a character is an operator in {'+', '-', '*', '/', '(', ')', '%'}
        :param c: string, the character to be checked
        :return: bool, True if the character is an operator, False otherwise
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.is_operator("+")
        True

        """
        return c in ('+', '-', '*', '/', '(', ')', '%')

    def compare(self, cur, peek):
        """
        Compare the precedence of two operators
        :param cur: string, the current operator
        :param peek: string, the operator at the top of the operator stack
        :return: bool, True if the current operator has higher or equal precedence, False otherwise
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.compare("+", "-")
        True

        """
        return self._PRIORITY.get(cur, 0) >= self._PRIORITY.get(peek, 0)

    @staticmethod
    def _calculate(first_value, second_value, current_op):
        """
        Perform the mathematical calculation based on the given operands and operator
        :param first_value: string, the first operand
        :param second_value: string, the second operand
        :param current_op: string, the operator
        :return: decimal.Decimal, the calculated result
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator._calculate("2", "3", "+")
        5.0

        """
        a = float(first_value)
        b = float(second_value)
        if current_op == '+':
            return float(a + b)
        if current_op == '-':
            return float(a - b)
        if current_op == '*':
            return float(a * b)
        if current_op == '/':
            return float(a / b)
        if current_op == '%':
            return float(a % b)
        raise ValueError("Unsupported operator: %s" % current_op)

    @staticmethod
    def transform(expression):
        """
        Transform the infix expression to a format suitable for conversion
        :param expression: string, the infix expression to be transformed
        :return: string, the transformed expression
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.transform("2 + 3 * 4")
        "2+3*4"

        """
        return "".join(expression.split())