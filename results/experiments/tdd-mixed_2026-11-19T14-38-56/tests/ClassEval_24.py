import unittest



class ComplexCalculatorTestAdd(unittest.TestCase):
    def test_add(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.add(1+2j, 3+4j), (4+6j))

    def test_add_2(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.add(-1 - 2j, -3 - 4j), (-4 - 6j))

    def test_add_3(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.add(1-2j, 3-4j), (4-6j))

import unittest

class AgentTest_add(unittest.TestCase):
    def test_add_1(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.add(0j, 3+4j), (3+4j))
        self.assertEqual(complexCalculator.add(3+4j, 0j), (3+4j))

    def test_add_2(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.add(0.5+1.5j, 2.25-0.75j), (2.75+0.75j))
        self.assertEqual(complexCalculator.add(2.25-0.75j, 0.5+1.5j), (2.75+0.75j))

class ComplexCalculatorTestSubtract(unittest.TestCase):
    def test_subtract(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.subtract(1+2j, 3+4j), (-2-2j))

    def test_subtract_2(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.subtract(-1-2j, -3-4j), (2+2j))

    def test_subtract_3(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.subtract(1-2j, 3-4j), (-2+2j))

import unittest

class AgentTest_subtract(unittest.TestCase):
    def test_subtract_1(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.subtract(0j, 3+4j), (-3-4j))
        self.assertEqual(complexCalculator.subtract(3+4j, 0j), (3+4j))

    def test_subtract_2(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.subtract(2.5+1.5j, 0.5+0.75j), (2+0.75j))
        self.assertEqual(complexCalculator.subtract(0.5+0.75j, 2.5+1.5j), (-2-0.75j))
        self.assertEqual(complexCalculator.subtract(1.25-2.5j, 1.25-2.5j), (0j))

class ComplexCalculatorTestMultiply(unittest.TestCase):
    def test_multiply(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.multiply(1+2j, 3+4j), (-5+10j))

    def test_multiply_2(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.multiply(-1-2j, -3-4j), (-5+10j))

    def test_multiply_3(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.multiply(1-2j, 3-4j), (-5-10j))

import unittest

class AgentTest_multiply(unittest.TestCase):
    def test_multiply_1(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.multiply(0j, 3+4j), (0j))
        self.assertEqual(complexCalculator.multiply(3+4j, 0j), (0j))
        self.assertEqual(complexCalculator.multiply(1+0j, 3+4j), (3+4j))
        self.assertEqual(complexCalculator.multiply(3+4j, 1+0j), (3+4j))

    def test_multiply_2(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.multiply(1j, 1j), (-1+0j))
        self.assertEqual(complexCalculator.multiply(2j, 3j), (-6+0j))
        self.assertEqual(complexCalculator.multiply(0.5+1.5j, 2-1j), (2.5+2.5j))
        self.assertEqual(complexCalculator.multiply(2-1j, 0.5+1.5j), (2.5+2.5j))

class ComplexCalculatorTestDivide(unittest.TestCase):
    def test_divide(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.divide(1+2j, 3+4j), (0.44+0.08j))

    def test_divide_2(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.divide(-1-2j, -3-4j), (0.44+0.08j))

    def test_divide_3(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.divide(1-2j, 3-4j), (0.44-0.08j))

import unittest

class AgentTest_divide(unittest.TestCase):
    def test_divide_1(self):
        complexCalculator = ComplexCalculator()
        self.assertAlmostEqual(complexCalculator.divide(0j, 3+4j), (0j))
        self.assertAlmostEqual(complexCalculator.divide(3+4j, 1+0j), (3+4j))
        self.assertAlmostEqual(complexCalculator.divide(2-5j, 2-5j), (1+0j))

    def test_divide_2(self):
        complexCalculator = ComplexCalculator()
        self.assertAlmostEqual(complexCalculator.divide(6+8j, 2+0j), (3+4j))
        self.assertAlmostEqual(complexCalculator.divide(1+0j, 1j), (-1j))
        self.assertAlmostEqual(complexCalculator.divide(3+4j, 1j), (4-3j))