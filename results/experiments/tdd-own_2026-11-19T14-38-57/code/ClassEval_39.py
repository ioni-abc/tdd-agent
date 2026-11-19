from collections import deque
from decimal import Decimal
import unittest


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
        value_stack = []
        for token in list(self.postfix_stack):
            if self.is_operator(token):
                second_value = value_stack.pop()
                first_value = value_stack.pop()
                value_stack.append(self._calculate(first_value, second_value, token))
            else:
                value_stack.append(Decimal(token))
        return float(value_stack[-1])


    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
        # Tokenize: numbers (digits and decimal points) and operators, ignoring whitespace
        tokens = []
        number = ''
        for ch in expression:
            if ch.isspace():
                if number:
                    tokens.append(number)
                    number = ''
            elif ch.isdigit() or ch == '.':
                number += ch
            elif self.is_operator(ch):
                if number:
                    tokens.append(number)
                    number = ''
                tokens.append(ch)
            else:
                if number:
                    tokens.append(number)
                    number = ''
                # unknown characters are treated as part of a token
                tokens.append(ch)
        if number:
            tokens.append(number)

        # Shunting-yard conversion to postfix
        self.postfix_stack = deque()
        op_stack = []
        for token in tokens:
            if not self.is_operator(token):
                self.postfix_stack.append(token)
            elif token == '(':
                op_stack.append(token)
            elif token == ')':
                while op_stack and op_stack[-1] != '(':
                    self.postfix_stack.append(op_stack.pop())
                if op_stack:
                    op_stack.pop()  # discard '('
            else:
                # pop operators of higher or equal precedence than the current one
                while op_stack and op_stack[-1] != '(' and self.compare(op_stack[-1], token):
                    self.postfix_stack.append(op_stack.pop())
                op_stack.append(token)

        while op_stack:
            self.postfix_stack.append(op_stack.pop())


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
        def priority(op):
            if op == '%':
                # modulo has the same precedence as multiplication and division
                return self.operat_priority[ord('*') - 40]
            return self.operat_priority[ord(op) - 40]

        return priority(cur) >= priority(peek)


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
        raise ValueError(f"Unknown operator: {current_op!r}")


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
        return ''.join(ch for ch in expression if not ch.isspace())