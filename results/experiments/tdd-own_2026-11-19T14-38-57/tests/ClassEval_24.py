import unittest


import unittest

class AgentTest_add(unittest.TestCase):

    def test_add_1(self):
        # Example from the add docstring
        result = ComplexCalculator.add(1+2j, 3+4j)
        self.assertEqual(result, 4+6j)

    def test_add_2(self):
        # add is a staticmethod, so it can also be called through an instance
        calculator = ComplexCalculator()
        result = calculator.add(1+2j, 3+4j)
        self.assertEqual(result, 4+6j)

    def test_add_3(self):
        # Adding zero leaves the other operand unchanged
        result = ComplexCalculator.add(2-3j, 0j)
        self.assertEqual(result, 2-3j)

    def test_add_4(self):
        # Negative real and imaginary parts
        result = ComplexCalculator.add(-1-1j, -2+5j)
        self.assertEqual(result, -3+4j)

    def test_add_5(self):
        # Non-integer components; the result is a complex number
        result = ComplexCalculator.add(0.5+1.25j, 0.25+0.75j)
        self.assertIsInstance(result, complex)
        self.assertAlmostEqual(result, 0.75+2j)

class AgentTest_subtract(unittest.TestCase):

    def test_subtract_1(self):
        # Example from the subtract docstring
        result = ComplexCalculator.subtract(1+2j, 3+4j)
        self.assertEqual(result, -2-2j)

    def test_subtract_2(self):
        # subtract is a staticmethod, so it can also be called through an instance
        calculator = ComplexCalculator()
        result = calculator.subtract(1+2j, 3+4j)
        self.assertEqual(result, -2-2j)

    def test_subtract_3(self):
        # Subtracting zero leaves the first operand unchanged
        result = ComplexCalculator.subtract(2-3j, 0j)
        self.assertEqual(result, 2-3j)

    def test_subtract_4(self):
        # Subtracting from zero yields the negation of the second operand
        result = ComplexCalculator.subtract(0j, 2-3j)
        self.assertEqual(result, -2+3j)

    def test_subtract_5(self):
        # Non-integer components; the result is a complex number
        result = ComplexCalculator.subtract(0.5+1.25j, 0.25+0.75j)
        self.assertIsInstance(result, complex)
        self.assertAlmostEqual(result, 0.25+0.5j)

import unittest

class AgentTest_multiply(unittest.TestCase):

    def test_multiply_1(self):
        # Example from the multiply docstring
        result = ComplexCalculator.multiply(1+2j, 3+4j)
        self.assertEqual(result, -5+10j)

    def test_multiply_2(self):
        # multiply is a staticmethod, so it can also be called through an instance
        calculator = ComplexCalculator()
        result = calculator.multiply(1+2j, 3+4j)
        self.assertEqual(result, -5+10j)

    def test_multiply_3(self):
        # Multiplying by zero yields zero
        result = ComplexCalculator.multiply(2-3j, 0j)
        self.assertEqual(result, 0j)

    def test_multiply_4(self):
        # The imaginary unit squared equals -1
        result = ComplexCalculator.multiply(1j, 1j)
        self.assertEqual(result, -1+0j)

    def test_multiply_5(self):
        # Non-integer components; the result is a complex number
        result = ComplexCalculator.multiply(0.5+1.25j, 0.25+0.75j)
        self.assertIsInstance(result, complex)
        self.assertAlmostEqual(result, -0.8125+0.6875j)

import unittest

class AgentTest_divide(unittest.TestCase):

    def test_divide_1(self):
        # Example from the divide docstring
        result = ComplexCalculator.divide(1+2j, 3+4j)
        self.assertAlmostEqual(result, 0.44+0.08j)

    def test_divide_2(self):
        # divide is a staticmethod, so it can also be called through an instance
        calculator = ComplexCalculator()
        result = calculator.divide(1+2j, 3+4j)
        self.assertAlmostEqual(result, 0.44+0.08j)

    def test_divide_3(self):
        # Dividing a non-zero complex number by itself yields one
        result = ComplexCalculator.divide(2-3j, 2-3j)
        self.assertAlmostEqual(result, 1+0j)

    def test_divide_4(self):
        # Dividing zero by a non-zero complex number yields zero
        result = ComplexCalculator.divide(0j, 3+4j)
        self.assertAlmostEqual(result, 0j)

    def test_divide_5(self):
        # Exact quotient with a purely imaginary divisor; the result is a complex number
        result = ComplexCalculator.divide(-4+2j, 2j)
        self.assertIsInstance(result, complex)
        self.assertAlmostEqual(result, 1+2j)