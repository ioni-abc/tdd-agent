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
        try:
            tokens = self._tokenize(expression)
            if tokens is None or not tokens:
                return None

            output = []
            ops = []
            for tok in tokens:
                if isinstance(tok, float):
                    output.append(tok)
                elif tok == '(':
                    ops.append(tok)
                elif tok == ')':
                    while ops and ops[-1] != '(':
                        output.append(ops.pop())
                    if not ops:
                        return None
                    ops.pop()
                else:
                    while (ops and ops[-1] != '('
                           and (self.precedence(ops[-1]) > self.precedence(tok)
                                or (self.precedence(ops[-1]) == self.precedence(tok)
                                    and tok != '^'))):
                        output.append(ops.pop())
                    ops.append(tok)

            while ops:
                top = ops.pop()
                if top == '(':
                    return None
                output.append(top)

            stack = []
            for tok in output:
                if isinstance(tok, float):
                    stack.append(tok)
                else:
                    if len(stack) < 2:
                        return None
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(self._apply_op(tok, a, b))

            if len(stack) != 1:
                return None
            result = stack[0]
            if isinstance(result, complex):
                return None
            return float(result)
        except (ValueError, ZeroDivisionError, IndexError, OverflowError, TypeError):
            return None

    def _apply_op(self, op, a, b):
        return self.operators[op](a, b)

    def _tokenize(self, expression):
        """Split expression into numbers (floats), operators and parentheses.
        Returns None if the expression contains invalid characters."""
        if not isinstance(expression, str):
            return None
        s = re.sub(r'\s+', '', expression)
        pattern = r'\d+\.?\d*|\.\d+|[-+*/^()]'
        raw = re.findall(pattern, s)
        if ''.join(raw) != s:
            return None

        tokens = []
        prev = None  # previous raw token
        for tok in raw:
            if re.fullmatch(r'\d+\.?\d*|\.\d+', tok):
                tokens.append(float(tok))
            elif tok == '-' and (prev is None or prev in '+-*/^('):
                # unary minus: treat as 0 - operand
                tokens.append(0.0)
                tokens.append('-')
            elif tok == '+' and (prev is None or prev in '+-*/^('):
                # unary plus: ignore
                pass
            else:
                tokens.append(tok)
            prev = tok
        return tokens

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
        ([1, -1], ['-'])
        """
        operator = operator_stack[-1]
        b = operand_stack.pop()
        a = operand_stack.pop()
        operand_stack.append(self._apply_op(operator, a, b))
        del operator_stack[0]
        return operand_stack, operator_stack