from collections import deque
from decimal import Decimal


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
        stack = []
        while self.postfix_stack:
            token = self.postfix_stack.popleft()
            if self.is_operator(token):
                second = stack.pop()
                first = stack.pop()
                stack.append(self._calculate(first, second, token))
            else:
                stack.append(Decimal(token))
        return float(stack[-1])

    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
        expr = self.transform(expression)
        n = len(expr)
        output = []
        ops = []
        prev_operand = False
        i = 0
        while i < n:
            c = expr[i]
            if c.isdigit() or c == '.' or (c == '-' and not prev_operand):
                j = i
                if c == '-':
                    j += 1
                while j < n and (expr[j].isdigit() or expr[j] == '.'):
                    j += 1
                output.append(expr[i:j])
                prev_operand = True
                i = j
                continue
            elif c == '(':
                ops.append(c)
                prev_operand = False
            elif c == ')':
                while ops and ops[-1] != '(':
                    output.append(ops.pop())
                if ops:
                    ops.pop()
                prev_operand = True
            elif c in '+-*/%':
                while ops and ops[-1] != '(' and self.compare(ops[-1], c):
                    output.append(ops.pop())
                ops.append(c)
                prev_operand = False
            else:
                raise ValueError("Invalid character in expression: %r" % c)
            i += 1
        while ops:
            output.append(ops.pop())
        self.postfix_stack = deque(output)

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

    def _priority(self, c):
        if c == '%':
            return 2
        return self.operat_priority[ord(c) - 40]

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
        return self._priority(cur) >= self._priority(peek)

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
        a = Decimal(first_value)
        b = Decimal(second_value)
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
        raise ValueError("Unknown operator: %r" % current_op)

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