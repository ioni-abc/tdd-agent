import unittest




class KappaCalculatorTestKappa(unittest.TestCase):
    def test_kappa_1(self):
        self.assertEqual(KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]], 3), 0.25)

    def test_kappa_2(self):
        self.assertAlmostEqual(KappaCalculator.kappa([[2, 2, 1], [1, 2, 1], [1, 1, 2]], 3), 0.19469026548672572)

    def test_kappa_3(self):
        self.assertAlmostEqual(KappaCalculator.kappa([[2, 1, 2], [1, 2, 1], [1, 1, 2]], 3), 0.19469026548672572)

import unittest

class AgentTest_kappa(unittest.TestCase):
    def test_kappa_1(self):
        # Perfect agreement: all mass on the diagonal, so kappa is 1.
        self.assertAlmostEqual(KappaCalculator.kappa([[3, 0], [0, 3]], 2), 1.0)

    def test_kappa_2(self):
        # Agreement equals chance agreement (observed 0.5, expected 0.5), so kappa is 0.
        self.assertAlmostEqual(KappaCalculator.kappa([[1, 1], [1, 1]], 2), 0.0)

class KappaCalculatorTestFleissKappa(unittest.TestCase):
    def test_fleiss_kappa_1(self):
        self.assertAlmostEqual(KappaCalculator.fleiss_kappa([[0, 0, 0, 0, 14],
                                                       [0, 2, 6, 4, 2],
                                                       [0, 0, 3, 5, 6],
                                                       [0, 3, 9, 2, 0],
                                                       [2, 2, 8, 1, 1],
                                                       [7, 7, 0, 0, 0],
                                                       [3, 2, 6, 3, 0],
                                                       [2, 5, 3, 2, 2],
                                                       [6, 5, 2, 1, 0],
                                                       [0, 2, 2, 3, 7]], 10, 5, 14), 0.20993070442195522)

    def test_fleiss_kappa_2(self):
        self.assertAlmostEqual(KappaCalculator.fleiss_kappa([[1, 0, 0, 0, 14],
                                                       [0, 2, 6, 4, 2],
                                                       [0, 0, 3, 5, 6],
                                                       [0, 3, 9, 2, 0],
                                                       [2, 2, 8, 1, 1],
                                                       [7, 7, 0, 0, 0],
                                                       [3, 2, 6, 3, 0],
                                                       [2, 5, 3, 2, 2],
                                                       [6, 5, 2, 1, 0],
                                                       [0, 2, 2, 3, 7]], 10, 5, 14), 0.2115748928799344)

    def test_fleiss_kappa_3(self):
        self.assertAlmostEqual(KappaCalculator.fleiss_kappa([[0, 1, 0, 0, 14],
                                                       [0, 2, 6, 4, 2],
                                                       [0, 0, 3, 5, 6],
                                                       [0, 3, 9, 2, 0],
                                                       [2, 2, 8, 1, 1],
                                                       [7, 7, 0, 0, 0],
                                                       [3, 2, 6, 3, 0],
                                                       [2, 5, 3, 2, 2],
                                                       [6, 5, 2, 1, 0],
                                                       [0, 2, 2, 3, 7]], 10, 5, 14), 0.21076904123090398)

import unittest

class AgentTest_fleiss_kappa(unittest.TestCase):
    def test_fleiss_kappa_1(self):
        # Perfect agreement: every sample has all 3 raters choosing the same category,
        # so the observed agreement is 1 and kappa is 1.
        self.assertAlmostEqual(KappaCalculator.fleiss_kappa([[3, 0],
                                                             [0, 3],
                                                             [3, 0]], 3, 2, 3), 1.0)

    def test_fleiss_kappa_2(self):
        # Observed agreement (0.5) equals chance agreement (0.5), so kappa is 0.
        self.assertAlmostEqual(KappaCalculator.fleiss_kappa([[2, 0],
                                                             [0, 2],
                                                             [1, 1],
                                                             [1, 1]], 4, 2, 2), 0.0)