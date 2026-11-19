import unittest



class CalculatorTestPrecedence(unittest.TestCase):
    def test_precedence_1(self):
        calculator = Calculator()
        res1 = calculator.precedence('+')
        res2 = calculator.precedence('-')
        self.assertEqual(res1, res2)

    def test_precedence_2(self):
        calculator = Calculator()
        res1 = calculator.precedence('*')
        res2 = calculator.precedence('/')
        self.assertEqual(res1, res2)

    def test_precedence_3(self):
        calculator = Calculator()
        res1 = calculator.precedence('+')
        res2 = calculator.precedence('/')
        self.assertNotEqual(res1, res2)

import unittest

class AgentTest_precedence(unittest.TestCase):
    def test_precedence_1(self):
        calculator = Calculator()
        self.assertEqual(calculator.precedence('+'), 1)
        self.assertEqual(calculator.precedence('^'), 3)

    def test_precedence_2(self):
        calculator = Calculator()
        self.assertEqual(calculator.precedence('%'), 0)
        self.assertEqual(calculator.precedence('('), 0)
        self.assertEqual(calculator.precedence(''), 0)

class CalculatorTestApplyOperator(unittest.TestCase):
    def test_apply_operator_1(self):
        calculator = Calculator()
        operand_stack = [1, 2, 3]
        operator_stack = ['+', '-']
        calculator.apply_operator(operand_stack, operator_stack)
        self.assertEqual(operand_stack, [1, -1])
        self.assertEqual(operator_stack, ['+'])

    def test_apply_operator_2(self):
        calculator = Calculator()
        operand_stack = [1, 2, 3]
        operator_stack = ['+', '*']
        calculator.apply_operator(operand_stack, operator_stack)
        self.assertEqual(operand_stack, [1, 6])
        self.assertEqual(operator_stack, ['+'])

    def test_apply_operator_3(self):
        calculator = Calculator()
        operand_stack = [6, 3, 3]
        operator_stack = ['+', '/']
        calculator.apply_operator(operand_stack, operator_stack)
        self.assertEqual(operand_stack, [6, 1])
        self.assertEqual(operator_stack, ['+'])

import unittest

class AgentTest_apply_operator(unittest.TestCase):
    def test_apply_operator_1(self):
        calculator = Calculator()
        operand_stack = [2, 3, 4]
        operator_stack = ['+', '^']
        result = calculator.apply_operator(operand_stack, operator_stack)
        self.assertEqual(operand_stack, [2, 81])
        self.assertEqual(operator_stack, ['+'])
        self.assertEqual(result, ([2, 81], ['+']))

    def test_apply_operator_2(self):
        calculator = Calculator()
        operand_stack = [1, 7, 2]
        operator_stack = ['/']
        calculator.apply_operator(operand_stack, operator_stack)
        self.assertEqual(operand_stack, [1, 3.5])
        self.assertEqual(operator_stack, [])

class CalculatorTestCalculate(unittest.TestCase):
    def test_calculate_1(self):
        calculator = Calculator()
        res = calculator.calculate('1+2')
        self.assertEqual(res, 3)

    def test_calculate_2(self):
        calculator = Calculator()
        res = calculator.calculate('1+2*3')
        self.assertEqual(res, 7)

    def test_calculate_3(self):
        calculator = Calculator()
        res = calculator.calculate('1+2*3+4')
        self.assertEqual(res, 11)

    def test_calculate_4(self):
        calculator = Calculator()
        res = calculator.calculate('1+2^3*2+4*5')
        self.assertEqual(res, 37)

    def test_calculate_5(self):
        calculator = Calculator()
        res = calculator.calculate('1+2+3')
        self.assertEqual(res, 6)

import unittest

class AgentTest_calculate(unittest.TestCase):
    def test_calculate_1(self):
        calculator = Calculator()
        self.assertEqual(calculator.calculate('10-4-3'), 3)
        self.assertEqual(calculator.calculate('8/4/2'), 1)

    def test_calculate_2(self):
        calculator = Calculator()
        self.assertEqual(calculator.calculate('7/2'), 3.5)
        self.assertEqual(calculator.calculate('1.5*4'), 6)

    def test_calculate_3(self):
        calculator = Calculator()
        self.assertIsNone(calculator.calculate('1+'))
        self.assertIsNone(calculator.calculate('a+2'))