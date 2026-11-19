import unittest


import unittest

class AgentTest_is_operator(unittest.TestCase):

    def test_is_operator_1(self):
        calc = ExpressionCalculator()
        for op in ['+', '-', '*', '/']:
            self.assertTrue(calc.is_operator(op), f"'{op}' should be an operator")

    def test_is_operator_2(self):
        calc = ExpressionCalculator()
        for op in ['(', ')', '%']:
            self.assertTrue(calc.is_operator(op), f"'{op}' should be an operator")

    def test_is_operator_3(self):
        calc = ExpressionCalculator()
        for digit in '0123456789':
            self.assertFalse(calc.is_operator(digit), f"'{digit}' should not be an operator")

    def test_is_operator_4(self):
        calc = ExpressionCalculator()
        for ch in ['a', 'Z', 'x']:
            self.assertFalse(calc.is_operator(ch), f"'{ch}' should not be an operator")

    def test_is_operator_5(self):
        calc = ExpressionCalculator()
        self.assertIsInstance(calc.is_operator('+'), bool)
        self.assertIsInstance(calc.is_operator('3'), bool)
        self.assertFalse(calc.is_operator(' '))
        self.assertFalse(calc.is_operator('.'))

import unittest

class AgentTest_compare(unittest.TestCase):

    def test_compare_1(self):
        calc = ExpressionCalculator()
        self.assertTrue(calc.compare("+", "-"))

    def test_compare_2(self):
        calc = ExpressionCalculator()
        self.assertTrue(calc.compare("+", "+"), "equal precedence should return True")
        self.assertTrue(calc.compare("-", "-"), "equal precedence should return True")

    def test_compare_3(self):
        calc = ExpressionCalculator()
        self.assertTrue(calc.compare("-", "+"), "'-' and '+' have equal precedence")
        self.assertTrue(calc.compare("+", "-"), "'+' and '-' have equal precedence")

    def test_compare_4(self):
        calc = ExpressionCalculator()
        self.assertTrue(calc.compare("*", "+"), "'*' has higher precedence than '+'")
        self.assertTrue(calc.compare("/", "-"), "'/' has higher precedence than '-'")
        self.assertTrue(calc.compare("*", "/"), "'*' and '/' have equal precedence")

    def test_compare_5(self):
        calc = ExpressionCalculator()
        self.assertFalse(calc.compare("+", "*"), "'+' has lower precedence than '*'")
        self.assertFalse(calc.compare("-", "/"), "'-' has lower precedence than '/'")
        result = calc.compare("+", "-")
        self.assertIsInstance(result, bool)

class AgentTest_prepare(unittest.TestCase):

    def test_prepare_1(self):
        calc = ExpressionCalculator()
        calc.prepare("2+3*4")
        self.assertEqual(list(calc.postfix_stack), ['2', '3', '4', '*', '+'])

    def test_prepare_2(self):
        calc = ExpressionCalculator()
        calc.prepare("2 + 3 * 4")
        self.assertEqual(list(calc.postfix_stack), ['2', '3', '4', '*', '+'])

    def test_prepare_3(self):
        calc = ExpressionCalculator()
        calc.prepare("7")
        self.assertEqual(list(calc.postfix_stack), ['7'])

    def test_prepare_4(self):
        calc = ExpressionCalculator()
        calc.prepare("(2+3)*4")
        self.assertEqual(list(calc.postfix_stack), ['2', '3', '+', '4', '*'])

    def test_prepare_5(self):
        calc = ExpressionCalculator()
        calc.prepare("8-3-2")
        self.assertEqual(list(calc.postfix_stack), ['8', '3', '-', '2', '-'])

import unittest

from decimal import Decimal

class AgentTest__calculate(unittest.TestCase):

    def test__calculate_1(self):
        calc = ExpressionCalculator()
        self.assertEqual(float(ExpressionCalculator._calculate("2", "3", "+")), 5.0)
        self.assertEqual(float(ExpressionCalculator._calculate("10", "4", "-")), 6.0)

    def test__calculate_2(self):
        calc = ExpressionCalculator()
        self.assertEqual(float(ExpressionCalculator._calculate("2", "3", "*")), 6.0)
        self.assertEqual(float(ExpressionCalculator._calculate("0", "7", "*")), 0.0)

    def test__calculate_3(self):
        calc = ExpressionCalculator()
        self.assertEqual(float(ExpressionCalculator._calculate("8", "2", "/")), 4.0)
        self.assertEqual(float(ExpressionCalculator._calculate("9", "3", "/")), 3.0)

    def test__calculate_4(self):
        calc = ExpressionCalculator()
        self.assertEqual(float(ExpressionCalculator._calculate("7", "3", "%")), 1.0)
        self.assertEqual(float(ExpressionCalculator._calculate("10", "5", "%")), 0.0)

    def test__calculate_5(self):
        calc = ExpressionCalculator()
        result = ExpressionCalculator._calculate("2", "3", "+")
        self.assertIsInstance(result, Decimal)
        self.assertEqual(float(result), 5.0)
        self.assertEqual(result, 5.0)

import unittest

class AgentTest_transform(unittest.TestCase):

    def test_transform_1(self):
        self.assertEqual(ExpressionCalculator.transform("2 + 3 * 4"), "2+3*4")

    def test_transform_2(self):
        self.assertEqual(ExpressionCalculator.transform("2+3*4"), "2+3*4")

    def test_transform_3(self):
        self.assertEqual(ExpressionCalculator.transform("(2 + 3) % 4"), "(2+3)%4")

    def test_transform_4(self):
        result = ExpressionCalculator.transform("10 - 25 / 5")
        self.assertIsInstance(result, str)
        self.assertEqual(result, "10-25/5")

    def test_transform_5(self):
        calc = ExpressionCalculator()
        self.assertEqual(calc.transform("  7 *  (8 - 1)  "), "7*(8-1)")

class AgentTest_calculate(unittest.TestCase):

    def test_calculate_1(self):
        calc = ExpressionCalculator()
        result = calc.calculate("2 + 3 * 4")
        self.assertIsInstance(result, float)
        self.assertEqual(result, 14.0)

    def test_calculate_2(self):
        calc = ExpressionCalculator()
        self.assertEqual(calc.calculate("(2+3)*4"), 20.0)
        self.assertEqual(calc.calculate("(2 + 3) * 4"), 20.0)

    def test_calculate_3(self):
        calc = ExpressionCalculator()
        self.assertEqual(calc.calculate("8-3-2"), 3.0)
        self.assertEqual(calc.calculate("10 - 4 - 3"), 3.0)

    def test_calculate_4(self):
        calc = ExpressionCalculator()
        self.assertEqual(calc.calculate("7 % 3"), 1.0)
        self.assertEqual(calc.calculate("8 / 2"), 4.0)
        self.assertEqual(calc.calculate("9 / 3 + 1"), 4.0)

    def test_calculate_5(self):
        calc = ExpressionCalculator()
        result = calc.calculate("7")
        self.assertIsInstance(result, float)
        self.assertEqual(result, 7.0)
        self.assertEqual(calc.calculate("  7 *  (8 - 1)  "), 49.0)