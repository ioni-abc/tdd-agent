import unittest


import unittest

class AgentTest_factorial(unittest.TestCase):

    def test_factorial_1(self):
        tricalculator = TriCalculator()
        self.assertEqual(tricalculator.factorial(5), 120)

    def test_factorial_2(self):
        tricalculator = TriCalculator()
        self.assertEqual(tricalculator.factorial(1), 1)

    def test_factorial_3(self):
        tricalculator = TriCalculator()
        self.assertEqual(tricalculator.factorial(3), 6)

    def test_factorial_4(self):
        tricalculator = TriCalculator()
        self.assertEqual(tricalculator.factorial(10), 3628800)

    def test_factorial_5(self):
        tricalculator = TriCalculator()
        result = tricalculator.factorial(5)
        self.assertIsInstance(result, int)

import math

import unittest

import unittest

class AgentTest_taylor(unittest.TestCase):

    def test_taylor_1(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.taylor(60, 50), 0.5, places=7)

    def test_taylor_2(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.taylor(0, 50), 1.0, places=7)

    def test_taylor_3(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.taylor(180, 50), -1.0, places=7)

    def test_taylor_4(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.taylor(90, 50), 0.0, places=7)

    def test_taylor_5(self):
        tricalculator = TriCalculator()
        result = tricalculator.taylor(45, 50)
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, math.cos(math.radians(45)), places=7)

import math

import unittest

class AgentTest_cos(unittest.TestCase):

    def test_cos_1(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.cos(60), 0.5, places=7)

    def test_cos_2(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.cos(0), 1.0, places=7)

    def test_cos_3(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.cos(180), -1.0, places=7)

    def test_cos_4(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.cos(90), 0.0, places=7)

    def test_cos_5(self):
        tricalculator = TriCalculator()
        result = tricalculator.cos(45)
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, math.cos(math.radians(45)), places=7)

import math

import unittest

class AgentTest_sin(unittest.TestCase):

    def test_sin_1(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.sin(30), 0.5, places=7)

    def test_sin_2(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.sin(0), 0.0, places=7)

    def test_sin_3(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.sin(90), 1.0, places=7)

    def test_sin_4(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.sin(180), 0.0, places=7)

    def test_sin_5(self):
        tricalculator = TriCalculator()
        result = tricalculator.sin(45)
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, math.sin(math.radians(45)), places=7)

import math

import unittest

class AgentTest_tan(unittest.TestCase):

    def test_tan_1(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.tan(45), 1.0, places=7)

    def test_tan_2(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.tan(0), 0.0, places=7)

    def test_tan_3(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.tan(30), math.tan(math.radians(30)), places=7)

    def test_tan_4(self):
        tricalculator = TriCalculator()
        self.assertAlmostEqual(tricalculator.tan(180), 0.0, places=7)

    def test_tan_5(self):
        tricalculator = TriCalculator()
        result = tricalculator.tan(60)
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, math.tan(math.radians(60)), places=7)