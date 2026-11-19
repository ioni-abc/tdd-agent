import unittest


import unittest

class AgentTest_precedence(unittest.TestCase):

    def test_precedence_1(self):
        calculator = Calculator()
        self.assertEqual(calculator.precedence('+'), 1)

    def test_precedence_2(self):
        calculator = Calculator()
        self.assertEqual(calculator.precedence('^'), 3)

    def test_precedence_3(self):
        calculator = Calculator()
        self.assertGreater(calculator.precedence('*'), calculator.precedence('+'))
        self.assertGreater(calculator.precedence('*'), calculator.precedence('-'))
        self.assertGreater(calculator.precedence('/'), calculator.precedence('+'))
        self.assertGreater(calculator.precedence('/'), calculator.precedence('-'))

    def test_precedence_4(self):
        calculator = Calculator()
        self.assertGreater(calculator.precedence('^'), calculator.precedence('*'))
        self.assertGreater(calculator.precedence('^'), calculator.precedence('/'))

    def test_precedence_5(self):
        calculator = Calculator()
        self.assertEqual(calculator.precedence('%'), 0)
        self.assertEqual(calculator.precedence('a'), 0)

import unittest

class AgentTest_apply_operator(unittest.TestCase):

    def test_apply_operator_1(self):
        calculator = Calculator()
        operands, operators = calculator.apply_operator([1, 2, 3], ['+', '-'])
        self.assertEqual(operands, [1, -1])
        self.assertEqual(operators, ['-'])

    def test_apply_operator_2(self):
        calculator = Calculator()
        operands, operators = calculator.apply_operator([2, 3], ['*'])
        self.assertEqual(operands, [6])
        self.assertEqual(operators, [])

    def test_apply_operator_3(self):
        calculator = Calculator()
        operands, operators = calculator.apply_operator([10, 4], ['/'])
        self.assertEqual(operands, [2.5])
        self.assertEqual(operators, [])

    def test_apply_operator_4(self):
        calculator = Calculator()
        operands, operators = calculator.apply_operator([2, 3], ['^'])
        self.assertEqual(operands, [8])
        self.assertEqual(operators, [])

    def test_apply_operator_5(self):
        calculator = Calculator()
        operands, operators = calculator.apply_operator([1, 2, 3], ['+'])
        self.assertEqual(operands, [1, 5])
        self.assertEqual(operators, [])

import unittest

class AgentTest_calculate(unittest.TestCase):

    def test_calculate_1(self):
        calculator = Calculator()
        self.assertEqual(calculator.calculate('1+2-3'), 0.0)

    def test_calculate_2(self):
        calculator = Calculator()
        self.assertEqual(calculator.calculate('2+3*4'), 14)

    def test_calculate_3(self):
        calculator = Calculator()
        self.assertEqual(calculator.calculate('2*3^2'), 18)

    def test_calculate_4(self):
        calculator = Calculator()
        self.assertEqual(calculator.calculate('10/4'), 2.5)

    def test_calculate_5(self):
        calculator = Calculator()
        self.assertIsNone(calculator.calculate('abc'))