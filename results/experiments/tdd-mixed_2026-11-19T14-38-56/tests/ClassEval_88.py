import unittest




class TriCalculatorTestFactorial(unittest.TestCase):
    def test_factorial_1(self):
        tricalculator = TriCalculator()
        self.assertEqual(tricalculator.factorial(5), 120)

    def test_factorial_2(self):
        tricalculator = TriCalculator()
        self.assertEqual(tricalculator.factorial(4), 24)

    def test_factorial_3(self):
        tricalculator = TriCalculator()
        self.assertEqual(tricalculator.factorial(3), 6)

import unittest

class AgentTest_factorial(unittest.TestCase):
    def test_factorial_1(self):
        tricalculator = TriCalculator()
        self.assertEqual(tricalculator.factorial(1), 1)

    def test_factorial_2(self):
        tricalculator = TriCalculator()
        self.assertEqual(tricalculator.factorial(10), 3628800)

class TriCalculatorTestTaylor(unittest.TestCase):
    def test_taylor_1(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.taylor(60, 50), 0.5)

    def test_taylor_2(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.taylor(30, 50), 0.8660254037844386)

    def test_taylor_3(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.taylor(90, 50), 0.0)

import unittest

class AgentTest_taylor(unittest.TestCase):
    def test_taylor_1(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.taylor(0, 50), 1.0)

    def test_taylor_2(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.taylor(180, 50), -1.0)

class TriCalculatorTestCos(unittest.TestCase):
    def test_cos_1(self):
        tricalculator = TriCalculator()
        self.assertEqual(tricalculator.cos(60), 0.5)

    def test_cos_2(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.cos(30), 0.8660254038)

    def test_cos_3(self):
        tricalculator = TriCalculator()
        self.assertEqual(tricalculator.cos(0), 1.0)

import unittest

class AgentTest_cos(unittest.TestCase):
    def test_cos_1(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.cos(180), -1.0)

    def test_cos_2(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.cos(90), 0.0)

class TriCalculatorTestSin(unittest.TestCase):
    def test_sin_1(self):
        tricalculator = TriCalculator()
        self.assertEqual(tricalculator.sin(30), 0.5)

    def test_sin_2(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.sin(60), 0.8660254038)

    def test_sin_3(self):
        tricalculator = TriCalculator()
        self.assertEqual(tricalculator.sin(0), 0.0)

import unittest

class AgentTest_sin(unittest.TestCase):
    def test_sin_1(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.sin(90), 1.0)

    def test_sin_2(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.sin(45), 0.7071067811865476)

class TriCalculatorTestTan(unittest.TestCase):
    def test_tan_1(self):
        tricalculator = TriCalculator()
        self.assertEqual(tricalculator.tan(45), 1.0)

    def test_tan_2(self):
        tricalculator = TriCalculator()
        self.assertEqual(tricalculator.tan(90), False)

    def test_tan_3(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.tan(30), 0.5773502692)

class AgentTest_tan(unittest.TestCase):
    def test_tan_1(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.tan(0), 0.0)

    def test_tan_2(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.tan(60), 1.7320508075688772)