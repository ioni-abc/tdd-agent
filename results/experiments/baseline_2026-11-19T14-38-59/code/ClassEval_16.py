import re


class Calculator:
    """
    This is a class for a calculator, capable of performing basic arithmetic calculations on numerical expressions using the operators +, -, *, /, and ^ (exponentiation).
    """

    _TOKEN_PATTERN = re.compile(r'\d+\.?\d*|\.\d+|[-+*/^()]')

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

    def _tokenize(self, expression):
        """Split the expression into number, operator and parenthesis tokens.
        Returns None if the expression contains invalid characters."""
        text = expression.replace(' ', '').replace('\t', '')
        tokens = []
        pos = 0
        while pos < len(text):
            match = self._TOKEN_PATTERN.match(text, pos)
            if not match:
                return None
            tokens.append(match.group())
            pos = match.end()
        return tokens

    def calculate(self, expression):
        """
        Calculate the value of a given expression
        :param expression: string, given expression
        :return:If successful, returns the value of the expression; otherwise, returns None
        >>> calculator = Calculator()
        >>> calculator.calculate('1+2-3')
        0.0
        """
        try:
            if not isinstance(expression, str):
                return None
            tokens = self._tokenize(expression)
            if not tokens:
                return None

            operand_stack = []
            operator_stack = []
            expect_operand = True

            for tok in tokens:
                if tok[0].isdigit() or tok[0] == '.':
                    if not expect_operand:
                        return None
                    operand_stack.append(float(tok))
                    expect_operand = False
                elif tok == '(':
                    if not expect_operand:
                        return None
                    operator_stack.append(tok)
                    expect_operand = True
                elif tok == ')':
                    if expect_operand:
                        return None
                    while operator_stack and operator_stack[-1] != '(':
                        operand_stack, operator_stack = self.apply_operator(
                            operand_stack, operator_stack)
                    if not operator_stack:
                        return None
                    operator_stack.pop()  # remove '('
                    expect_operand = False
                elif tok in self.operators:
                    if expect_operand:
                        # unary plus / minus
                        if tok == '-':
                            operand_stack.append(0.0)
                        elif tok == '+':
                            continue
                        else:
                            return None
                    while (operator_stack and operator_stack[-1] != '(' and
                           (self.precedence(operator_stack[-1]) > self.precedence(tok) or
                            (self.precedence(operator_stack[-1]) == self.precedence(tok)
                             and tok != '^'))):
                        operand_stack, operator_stack = self.apply_operator(
                            operand_stack, operator_stack)
                    operator_stack.append(tok)
                    expect_operand = True
                else:
                    return None

            if expect_operand:
                return None

            while operator_stack:
                if operator_stack[-1] == '(':
                    return None
                operand_stack, operator_stack = self.apply_operator(
                    operand_stack, operator_stack)

            if len(operand_stack) != 1:
                return None
            return float(operand_stack[0])
        except (ZeroDivisionError, ValueError, TypeError, IndexError, OverflowError):
            return None

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
        if operator in ('+', '-'):
            return 1
        if operator in ('*', '/'):
            return 2
        if operator == '^':
            return 3
        return 0

    def apply_operator(self, operand_stack, operator_stack):
        """
        Use the operator at the top of the operator stack to perform the operation on the two numbers at the top of the operator stack, and store the results at the top of the operator stack
        :param operand_stack:list
        :param operator_stack:list
        :return: the updated operand_stack and operator_stack
        >>> calculator = Calculator()
        >>> calculator.apply_operator([1, 2, 3], ['+', '-'])
        ([1, -1], ['+'])
        """
        operator = operator_stack.pop()
        right = operand_stack.pop()
        left = operand_stack.pop()
        operand_stack.append(self.operators[operator](left, right))
        return operand_stack, operator_stack