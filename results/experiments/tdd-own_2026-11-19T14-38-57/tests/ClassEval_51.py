import unittest


import unittest

class AgentTest_kappa(unittest.TestCase):

    def test_kappa_1(self):
        # Example from the docstring of kappa
        result = KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]], 3)
        self.assertAlmostEqual(result, 0.25, places=7)

    def test_kappa_2(self):
        # Perfect agreement: all raters agree on every item, so kappa is 1
        result = KappaCalculator.kappa([[2, 0], [0, 2]], 2)
        self.assertAlmostEqual(result, 1.0, places=7)

    def test_kappa_3(self):
        # Agreement no better than chance: observed agreement 0.5, expected agreement 0.5, so kappa is 0
        result = KappaCalculator.kappa([[1, 1], [1, 1]], 2)
        self.assertAlmostEqual(result, 0.0, places=7)

    def test_kappa_4(self):
        # Worked 2x2 example: observed agreement 0.7, expected agreement 0.5, so kappa is 0.4
        result = KappaCalculator.kappa([[20, 5], [10, 15]], 2)
        self.assertAlmostEqual(result, 0.4, places=7)

    def test_kappa_5(self):
        # Perfect agreement on a 3-dimensional (3x3) matrix with uneven category counts, kappa is 1
        result = KappaCalculator.kappa([[3, 0, 0], [0, 1, 0], [0, 0, 4]], 3)
        self.assertAlmostEqual(result, 1.0, places=7)

import unittest

import numpy as np

class AgentTest_fleiss_kappa(unittest.TestCase):

    def test_fleiss_kappa_1(self):
        # Example from the docstring of fleiss_kappa
        data = [[0, 0, 0, 0, 14],
                [0, 2, 6, 4, 2],
                [0, 0, 3, 5, 6],
                [0, 3, 9, 2, 0],
                [2, 2, 8, 1, 1],
                [7, 7, 0, 0, 0],
                [3, 2, 6, 3, 0],
                [2, 5, 3, 2, 2],
                [6, 5, 2, 1, 0],
                [0, 2, 2, 3, 7]]
        result = KappaCalculator.fleiss_kappa(data, 10, 5, 14)
        self.assertAlmostEqual(result, 0.20993070442195522, places=7)

    def test_fleiss_kappa_2(self):
        # Perfect agreement: every rater agrees on every item, so kappa is 1
        data = [[2, 0],
                [0, 2],
                [2, 0]]
        result = KappaCalculator.fleiss_kappa(data, 3, 2, 2)
        self.assertAlmostEqual(result, 1.0, places=7)

    def test_fleiss_kappa_3(self):
        # Observed agreement 0.5 equals chance agreement 0.5, so kappa is 0
        data = [[2, 0],
                [0, 2],
                [1, 1],
                [1, 1]]
        result = KappaCalculator.fleiss_kappa(data, 4, 2, 2)
        self.assertAlmostEqual(result, 0.0, places=7)

    def test_fleiss_kappa_4(self):
        # Worked example: P_bar = 7/9, P_e = 41/81, so kappa = 0.55
        data = [[3, 0],
                [0, 3],
                [2, 1]]
        result = KappaCalculator.fleiss_kappa(data, 3, 2, 3)
        self.assertAlmostEqual(result, 0.55, places=7)

    def test_fleiss_kappa_5(self):
        # Observed agreement 0 with chance agreement 0.5, so kappa is -1
        data = [[1, 1],
                [1, 1]]
        result = KappaCalculator.fleiss_kappa(data, 2, 2, 2)
        self.assertAlmostEqual(result, -1.0, places=7)