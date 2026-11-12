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
        if not expression:
            return None

        # Tokenize: numbers, operators and parentheses. Stop at the first
        # unrecognized character, keeping the valid prefix of the expression.
        tokens = []
        i = 0
        n = len(expression)
        while i < n:
            ch = expression[i]
            if ch.isspace():
                i += 1
            elif ch.isdigit() or ch == '.':
                j = i
                while j < n and (expression[j].isdigit() or expression[j] == '.'):
                    j += 1
                tokens.append(expression[i:j])
                i = j
            elif ch in self.operators or ch in '()':
                tokens.append(ch)
                i += 1
            else:
                break

        if not tokens:
            return None

        operand_stack = []
        operator_stack = []

        try:
            for token in tokens:
                if token == '(':
                    operator_stack.append(token)
                elif token == ')':
                    while operator_stack and operator_stack[-1] != '(':
                        if len(operand_stack) < 2:
                            return None
                        self.apply_operator(operand_stack, operator_stack)
                    if not operator_stack:
                        return None  # mismatched parenthesis
                    operator_stack.pop()
                elif token in self.operators:
                    current = self.precedence(token)
                    while operator_stack and operator_stack[-1] != '(':
                        top = self.precedence(operator_stack[-1])
                        # '^' is right-associative; others are left-associative
                        if token == '^':
                            should_apply = top > current
                        else:
                            should_apply = top >= current
                        if not should_apply:
                            break
                        if len(operand_stack) < 2:
                            return None
                        self.apply_operator(operand_stack, operator_stack)
                    operator_stack.append(token)
                else:
                    operand_stack.append(float(token))

            while operator_stack:
                if operator_stack[-1] == '(':
                    return None  # mismatched parenthesis
                if len(operand_stack) < 2:
                    return None
                self.apply_operator(operand_stack, operator_stack)
        except (ValueError, ZeroDivisionError, OverflowError, IndexError):
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
        Use the operator at the top of the operator stack to perform the operation on the two numbers at the top of the operand stack, and store the result back on the operand stack
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