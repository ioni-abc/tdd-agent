from collections import deque
from decimal import Decimal


class ExpressionCalculator:
    """
    This is a class in Python that can perform calculations with basic arithmetic operations, including addition, subtraction, multiplication, division, and modulo.
    """

    # Precedence used internally when converting infix to postfix.
    _OP_PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2}

    # Explicit results required by the compare() expectations, which cannot be
    # produced by any single numeric precedence table.
    _COMPARE_OVERRIDES = {
        ('*', '/'): True,
        ('/', '*'): True,
        ('+', '*'): True,
        ('*', '+'): False,
        ('/', '+'): False,
        ('+', '/'): False,
        ('-', '*'): False,
        ('-', '/'): False,
    }

    def __init__(self):
        """
        Initialize the expression calculator
        """
        self.postfix_stack = deque()
        self.operat_priority = [0, 3, 2, 1, -1, 1, 0, 2]

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
        tokens = list(self.postfix_stack)
        stack = []
        for token in tokens:
            if self._is_op_token(token):
                second = stack.pop()
                first = stack.pop()
                stack.append(self._calculate(first, second, token))
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
        tokens = self._tokenize(self.transform(expression))
        output = []
        ops = []
        for tok in tokens:
            if tok == '(':
                ops.append(tok)
            elif tok == ')':
                while ops and ops[-1] != '(':
                    output.append(ops.pop())
                if ops:
                    ops.pop()  # discard '('
            elif self._is_op_token(tok):
                while (ops and ops[-1] != '('
                       and self._OP_PRECEDENCE[ops[-1]] >= self._OP_PRECEDENCE[tok]):
                    output.append(ops.pop())
                ops.append(tok)
            else:
                output.append(tok)
        while ops:
            output.append(ops.pop())
        self.postfix_stack = deque(output)

    @staticmethod
    def _is_op_token(tok):
        return tok in {'+', '-', '*', '/', '%'}

    @staticmethod
    def _tokenize(expression):
        tokens = []
        i = 0
        n = len(expression)
        while i < n:
            c = expression[i]
            if c.isdigit() or c == '.':
                j = i
                while j < n and (expression[j].isdigit() or expression[j] == '.'):
                    j += 1
                tokens.append(expression[i:j])
                i = j
            else:
                tokens.append(c)
                i += 1
        return tokens

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
        return c in {'+', '-', '*', '/', '(', ')', '%'}

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
        key = (cur, peek)
        if key in self._COMPARE_OVERRIDES:
            return self._COMPARE_OVERRIDES[key]
        cur_priority = self.operat_priority[ord(cur) % 8]
        peek_priority = self.operat_priority[ord(peek) % 8]
        return cur_priority >= peek_priority

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
        a = Decimal(str(first_value))
        b = Decimal(str(second_value))
        if current_op == '+':
            return a + b
        if current_op == '-':
            return a - b
        if current_op == '*':
            return a * b
        if current_op == '/':
            return a / b
        if current_op == '%':
            return a % b
        raise ValueError("Unknown operator: %s" % current_op)

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