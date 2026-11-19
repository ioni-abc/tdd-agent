import re


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

        tokens = []
        pos = 0
        token_pattern = re.compile(r'\s*(\d+\.?\d*|\.\d+|[-+*/^()])')
        length = len(expression)
        while pos < length:
            if expression[pos:].strip() == '':
                break
            match = token_pattern.match(expression, pos)
            if not match:
                return None
            tokens.append(match.group(1))
            pos = match.end()

        if not tokens:
            return None

        operand_stack = []
        operator_stack = []
        expect_operand = True

        try:
            for token in tokens:
                if token[0].isdigit() or token[0] == '.':
                    if not expect_operand:
                        return None
                    operand_stack.append(float(token))
                    expect_operand = False
                elif token == '(':
                    if not expect_operand:
                        return None
                    operator_stack.append(token)
                elif token == ')':
                    if expect_operand:
                        return None
                    while operator_stack and operator_stack[-1] != '(':
                        self._reduce(operand_stack, operator_stack)
                    if not operator_stack:
                        return None
                    operator_stack.pop()
                    expect_operand = False
                else:
                    # binary operator
                    if expect_operand:
                        return None
                    while (operator_stack and operator_stack[-1] != '(' and
                           (self.precedence(operator_stack[-1]) > self.precedence(token) or
                            (self.precedence(operator_stack[-1]) == self.precedence(token)
                             and token != '^'))):
                        self._reduce(operand_stack, operator_stack)
                    operator_stack.append(token)
                    expect_operand = True

            if expect_operand:
                return None

            while operator_stack:
                if operator_stack[-1] == '(':
                    return None
                self._reduce(operand_stack, operator_stack)

            if len(operand_stack) != 1:
                return None
            return float(operand_stack[0])
        except (ZeroDivisionError, OverflowError, ValueError, IndexError):
            return None

    def _reduce(self, operand_stack, operator_stack):
        """
        Pop one operator and its two operands, apply the operator and push the result.
        """
        operator = operator_stack.pop()
        right = operand_stack.pop()
        left = operand_stack.pop()
        operand_stack.append(self.operators[operator](left, right))

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
        operator = operator_stack[-1]
        right = operand_stack.pop()
        left = operand_stack.pop()
        operand_stack.append(self.operators[operator](left, right))
        if operator_stack:
            del operator_stack[0]
        return operand_stack, operator_stack