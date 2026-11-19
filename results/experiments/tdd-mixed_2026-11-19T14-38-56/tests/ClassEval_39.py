import unittest




class ExpressionCalculatorTestIsOperator(unittest.TestCase):
    def setUp(self):
        self.expression_calculator = ExpressionCalculator()

    def test_is_operator_1(self):
        self.assertTrue(self.expression_calculator.is_operator("+"))

    def test_is_operator_2(self):
        self.assertTrue(self.expression_calculator.is_operator("-"))

    def test_is_operator_3(self):
        self.assertTrue(self.expression_calculator.is_operator("*"))

import unittest

class AgentTest_is_operator(unittest.TestCase):
    def setUp(self):
        self.expression_calculator = ExpressionCalculator()

    def test_is_operator_1(self):
        self.assertTrue(self.expression_calculator.is_operator("/"))
        self.assertTrue(self.expression_calculator.is_operator("%"))

    def test_is_operator_2(self):
        self.assertFalse(self.expression_calculator.is_operator("5"))
        self.assertFalse(self.expression_calculator.is_operator("a"))
        self.assertFalse(self.expression_calculator.is_operator(" "))
        self.assertFalse(self.expression_calculator.is_operator("."))

class ExpressionCalculatorTestCompare(unittest.TestCase):
    def setUp(self):
        self.expression_calculator = ExpressionCalculator()

    def test_compare_1(self):
        result = self.expression_calculator.compare("+", "-")
        self.assertTrue(result)

    def test_compare_2(self):
        result = self.expression_calculator.compare("*", "/")
        self.assertTrue(result)

    def test_compare_3(self):
        result = self.expression_calculator.compare("+", "*")
        self.assertTrue(result)

    def test_compare_4(self):
        result = self.expression_calculator.compare("*", "+")
        self.assertFalse(result)

    def test_compare_5(self):
        result = self.expression_calculator.compare("/", "+")
        self.assertFalse(result)

import unittest

class AgentTest_compare(unittest.TestCase):
    def setUp(self):
        self.expression_calculator = ExpressionCalculator()

    def test_compare_1(self):
        self.assertTrue(self.expression_calculator.compare("+", "+"))
        self.assertTrue(self.expression_calculator.compare("-", "+"))
        self.assertTrue(self.expression_calculator.compare("/", "*"))

    def test_compare_2(self):
        self.assertFalse(self.expression_calculator.compare("-", "*"))
        self.assertFalse(self.expression_calculator.compare("-", "/"))
        self.assertFalse(self.expression_calculator.compare("+", "/"))

class ExpressionCalculatorTestPrepare(unittest.TestCase):
    def setUp(self):
        self.expression_calculator = ExpressionCalculator()

    def test_prepare_1(self):
        self.expression_calculator.prepare("2+3*4")
        self.assertEqual(self.expression_calculator.postfix_stack, deque(['2', '3', '4', '*', '+']))

    def test_prepare_2(self):
        self.expression_calculator.prepare("2+3/4")
        self.assertEqual(self.expression_calculator.postfix_stack, deque(['2', '3', '4', '/', '+']))

    def test_prepare_3(self):
        self.expression_calculator.prepare("2-3*4")
        self.assertEqual(self.expression_calculator.postfix_stack, deque(['2', '3', '4', '*', '-']))

    def test_prepare_4(self):
        self.expression_calculator.prepare("1+3*4")
        self.assertEqual(self.expression_calculator.postfix_stack, deque(['1', '3', '4', '*', '+']))

from collections import deque

class AgentTest_prepare(unittest.TestCase):
    def setUp(self):
        self.expression_calculator = ExpressionCalculator()

    def test_prepare_1(self):
        self.expression_calculator.prepare("(2+3)*4")
        self.assertEqual(self.expression_calculator.postfix_stack, deque(['2', '3', '+', '4', '*']))

    def test_prepare_2(self):
        self.expression_calculator.prepare("12+3*45")
        self.assertEqual(self.expression_calculator.postfix_stack, deque(['12', '3', '45', '*', '+']))

class ExpressionCalculatorTestCalculateMethod(unittest.TestCase):
    def setUp(self):
        self.expression_calculator = ExpressionCalculator()

    def test_calculate_method_1(self):
        result = self.expression_calculator._calculate("2", "3", "+")
        self.assertEqual(result, Decimal(5.0))

    def test_calculate_method_2(self):
        result = self.expression_calculator._calculate("3", "2", "-")
        self.assertEqual(result, Decimal(1.0))

    def test_calculate_method_3(self):
        result = self.expression_calculator._calculate("2", "3", "*")
        self.assertEqual(result, Decimal(6.0))

    def test_calculate_method_4(self):
        result = self.expression_calculator._calculate("3", "3", "/")
        self.assertEqual(result, Decimal(1.0))

    def test_calculate_method_5(self):
        result = self.expression_calculator._calculate("6", "2", "/")
        self.assertEqual(result, Decimal(3.0))

import unittest

from decimal import Decimal

class AgentTest__calculate(unittest.TestCase):
    def setUp(self):
        self.expression_calculator = ExpressionCalculator()

    def test__calculate_1(self):
        result = self.expression_calculator._calculate("7", "3", "%")
        self.assertEqual(result, Decimal(1))
        result = self.expression_calculator._calculate("10", "4", "%")
        self.assertEqual(result, Decimal(2))

    def test__calculate_2(self):
        result = self.expression_calculator._calculate("7", "2", "/")
        self.assertIsInstance(result, Decimal)
        self.assertEqual(result, Decimal("3.5"))

class ExpressionCalculatorTestTransform(unittest.TestCase):
    def setUp(self):
        self.expression_calculator = ExpressionCalculator()

    def test_transform_1(self):
        result = self.expression_calculator.transform("2 + 3 * 4")
        self.assertEqual(result, "2+3*4")

    def test_transform_2(self):
        result = self.expression_calculator.transform("2 + 3 / 4")
        self.assertEqual(result, "2+3/4")

    def test_transform_3(self):
        result = self.expression_calculator.transform("2 - 3 * 4")
        self.assertEqual(result, "2-3*4")

    def test_transform_4(self):
        result = self.expression_calculator.transform("1 + 3 * 4")
        self.assertEqual(result, "1+3*4")

import unittest

class AgentTest_transform(unittest.TestCase):
    def setUp(self):
        self.expression_calculator = ExpressionCalculator()

    def test_transform_1(self):
        result = self.expression_calculator.transform("(12+3)*45")
        self.assertEqual(result, "(12+3)*45")

        result = self.expression_calculator.transform("(12 + 3) * 45")
        self.assertEqual(result, "(12+3)*45")

    def test_transform_2(self):
        result = self.expression_calculator.transform("  2   +  3 * 4  ")
        self.assertEqual(result, "2+3*4")

class ExpressionCalculatorTestCalculate(unittest.TestCase):
    def setUp(self):
        self.expression_calculator = ExpressionCalculator()

    def test_calculate_1(self):
        result = self.expression_calculator.calculate("2 + 3 * 4")
        self.assertEqual(result, 14.0)

    def test_calculate_2(self):
        result = self.expression_calculator.calculate("2 + 3 + 4")
        self.assertEqual(result, 9.0)

    def test_calculate_3(self):
        result = self.expression_calculator.calculate("2 * 3 * 4")
        self.assertEqual(result, 24.0)

import unittest

class AgentTest_calculate(unittest.TestCase):
    def setUp(self):
        self.expression_calculator = ExpressionCalculator()

    def test_calculate_1(self):
        result = self.expression_calculator.calculate("10 - 4")
        self.assertEqual(result, 6.0)
        self.assertIsInstance(result, float)

        result = self.expression_calculator.calculate("(2 + 3) * 4")
        self.assertEqual(result, 20.0)
        self.assertIsInstance(result, float)

    def test_calculate_2(self):
        result = self.expression_calculator.calculate("7 / 2")
        self.assertEqual(result, 3.5)
        self.assertIsInstance(result, float)

        result = self.expression_calculator.calculate("10 % 4")
        self.assertEqual(result, 2.0)
        self.assertIsInstance(result, float)