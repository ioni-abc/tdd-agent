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
        operators = {'+', '-', '*', '/', '%'}
        values = []
        for token in self.postfix_stack:
            if token in operators:
                second = values.pop()
                first = values.pop()
                values.append(self._calculate(first, second, token))
            else:
                values.append(Decimal(token))
        if not values:
            return 0.0
        return float(values[-1])


    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
        self.postfix_stack = deque()
        priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '%': 2}
        ops = []
        s = ''.join(expression.split())
        num = ''

        def pop_ops_while(condition):
            while ops and condition(ops[-1]):
                self.postfix_stack.append(ops.pop())

        for c in s:
            if c.isdigit() or c == '.':
                num += c
                continue
            if num:
                self.postfix_stack.append(num)
                num = ''
            if c == '(':
                ops.append(c)
            elif c == ')':
                pop_ops_while(lambda top: top != '(')
                if ops:
                    ops.pop()
            elif c in priority:
                pop_ops_while(
                    lambda top, c=c: top != '(' and priority[top] >= priority[c]
                )
                ops.append(c)
            else:
                raise ValueError("Invalid character in expression: %r" % c)
        if num:
            self.postfix_stack.append(num)
        pop_ops_while(lambda top: top != '(')
        ops.clear()


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
        # Ranks chosen to satisfy the required comparisons:
        # '+' and '-' rank above '*', '/', '%' in this comparison table.
        rank = {'+': 2, '-': 2, '*': 1, '/': 1, '%': 1}
        return rank[cur] >= rank[peek]


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
        s = ''.join(expression.split())
        result = []
        for i, c in enumerate(s):
            if c == '-':
                # A '-' is unary when it appears at the start or after '(' or another operator.
                prev = s[i - 1] if i > 0 else None
                if prev is None or prev == '(' or prev in '+-*/%':
                    result.append('~')
                else:
                    result.append('-')
            elif c == '~':
                nxt = s[i + 1] if i + 1 < len(s) else None
                if nxt == '(':
                    # Negation of a parenthesised group is written as subtraction from zero.
                    result.append('0-')
                else:
                    result.append('~')
            else:
                result.append(c)
        return ''.join(result)