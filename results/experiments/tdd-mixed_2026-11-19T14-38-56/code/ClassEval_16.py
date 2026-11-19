import re
import unittest


class Calculator:
    """
    This is a class for a calculator, capable of performing basic arithmetic calculations on numerical expressions using the operators +, -, *, /, and ^ (exponentiation).
    """

    def __init__(self):
        """
        Initialize the operations performed by the five operators'+','-','*','/','^'
        """
        self.operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '^': lambda x, y: x ** y
        }

    def calculate(self, expression):
        """
        Calculate the value of a given expression
        :param expression: string, given expression
        :return:If successful, returns the value of the expression; otherwise, returns None
        >>> calculator = Calculator()
        >>> calculator.calculate('1+2-3')
        0.0
        """
        if not isinstance(expression, str):
            return None

        token_re = re.compile(r'\s*(?:(\d+(?:\.\d+)?|\.\d+)|([-+*/^]))')
        tokens = []
        pos = 0
        n = len(expression)
        while pos < n:
            m = token_re.match(expression, pos)
            if not m:
                if expression[pos:].isspace():
                    break
                return None
            if m.group(1) is not None:
                tokens.append(float(m.group(1)))
            else:
                tokens.append(m.group(2))
            pos = m.end()

        if not tokens:
            return None

        # Validate alternation: operand, operator, operand, ..., operand
        expect_operand = True
        for tok in tokens:
            is_number = isinstance(tok, float)
            if expect_operand:
                if not is_number:
                    return None
            else:
                if is_number:
                    return None
            expect_operand = not expect_operand
        if expect_operand:
            # Expression ended while expecting an operand
            return None

        operand_stack = []
        operator_stack = []
        try:
            for tok in tokens:
                if isinstance(tok, float):
                    operand_stack.append(tok)
                else:
                    p = self.precedence(tok)
                    while operator_stack:
                        top_p = self.precedence(operator_stack[-1])
                        if top_p > p or (top_p == p and tok != '^'):
                            self.apply_operator(operand_stack, operator_stack)
                        else:
                            break
                    operator_stack.append(tok)
            while operator_stack:
                self.apply_operator(operand_stack, operator_stack)
        except (ZeroDivisionError, OverflowError):
            return None

        if len(operand_stack) != 1:
            return None
        return operand_stack[0]

    def precedence(self, operator):
        """
        Returns the priority of the specified operator, where the higher the priority, the greater the assignment. The priority of '^' is greater than '/' and '*', and the priority of '/' and '*' is greater than '+' and '-'
        :param operator: string, given operator
        :return: int, the priority of the given operator, otherwise return 0
        >>> calculator = Calculator()
        >>> calculator.precedence('+')
        1
        >>> calculator.precedence('^')
        3
        """
        priorities = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3
        }
        return priorities.get(operator, 0)

    def apply_operator(self, operand_stack, operator_stack):
        """
        Use the operator at the top of the operator stack to perform the operation on the two numbers at the top of the operator stack, and store the results at the top of the operator stack
        :param operand_stack:list
        :param operator_stack:list
        :return: the updated operand_stack and operator_stack
        >>> calculator = Calculator()
        >>> calculator.apply_operator([1, 2, 3], ['+', '-'])
        ([1, -1], ['-'])
        """
        operator = operator_stack.pop()
        right = operand_stack.pop()
        left = operand_stack.pop()
        operand_stack.append(self.operators[operator](left, right))
        return operand_stack, operator_stack