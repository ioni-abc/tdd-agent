import unittest



class Statistics3TestMedian(unittest.TestCase):
    def test_median(self):
        statistics3 = Statistics3()
        self.assertEqual(statistics3.median([1, 2, 3, 4]), 2.5)

    def test_median_2(self):
        statistics3 = Statistics3()
        self.assertEqual(statistics3.median([1, 2, 3, 4, 5]), 3)

    def test_median_3(self):
        statistics3 = Statistics3()
        self.assertEqual(statistics3.median([1, 2, 3, 4, 5, 6]), 3.5)

import unittest

class AgentTest_median(unittest.TestCase):
    def test_median_1(self):
        statistics3 = Statistics3()
        self.assertEqual(statistics3.median([3, -1, 2]), 2)

    def test_median_2(self):
        statistics3 = Statistics3()
        self.assertEqual(statistics3.median([7]), 7)

class Statistics3TestMode(unittest.TestCase):
    def test_mode(self):
        statistics3 = Statistics3()
        self.assertEqual(statistics3.mode([1, 2, 3, 3]), [3])

    def test_mode_2(self):
        statistics3 = Statistics3()
        self.assertEqual(statistics3.mode([1, 2, 3, 3, 4, 4]), [3, 4])

    def test_mode_3(self):
        statistics3 = Statistics3()
        self.assertEqual(statistics3.mode([1, 2, 3, 3, 4, 4, 5]), [3, 4])

import unittest

class AgentTest_mode(unittest.TestCase):
    def test_mode_1(self):
        statistics3 = Statistics3()
        self.assertEqual(statistics3.mode([5, -2, 5, 7, 5]), [5])

    def test_mode_2(self):
        statistics3 = Statistics3()
        self.assertEqual(statistics3.mode([7]), [7])

class Statistics3TestMean(unittest.TestCase):
    def test_mean(self):
        statistics3 = Statistics3()
        self.assertEqual(statistics3.mean([1, 2, 3]), 2.0)

    def test_mean_2(self):
        statistics3 = Statistics3()
        self.assertEqual(statistics3.mean([]), None)

    def test_mean_3(self):
        statistics3 = Statistics3()
        self.assertEqual(statistics3.mean([1, 1, 1]), 1.0)

import unittest

class AgentTest_mean(unittest.TestCase):
    def test_mean_1(self):
        statistics3 = Statistics3()
        self.assertEqual(statistics3.mean([-3, 1, 5, 7]), 2.5)

    def test_mean_2(self):
        statistics3 = Statistics3()
        result = statistics3.mean([2, 4, 6, 8])
        self.assertIsInstance(result, float)
        self.assertEqual(result, 5.0)

class Statistics3TestCorrelation(unittest.TestCase):
    def test_correlation(self):
        statistics3 = Statistics3()
        self.assertEqual(statistics3.correlation([1, 2, 3], [4, 5, 6]), 1.0)

    def test_correlation_2(self):
        statistics3 = Statistics3()
        self.assertEqual(statistics3.correlation([1, 2, 3, 4], [5, 6, 7, 8]), 1.0)

    def test_correlation_3(self):
        statistics3 = Statistics3()
        self.assertEqual(statistics3.correlation([1, 2, 3], [1,2,3]), 1.0)

import math

class AgentTest_correlation(unittest.TestCase):
    def test_correlation_1(self):
        statistics3 = Statistics3()
        self.assertEqual(statistics3.correlation([1, 2, 3], [6, 5, 4]), -1.0)

    def test_correlation_2(self):
        statistics3 = Statistics3()
        result = statistics3.correlation([1, 2, 3, 4, 5], [2, 4, 5, 4, 5])
        self.assertAlmostEqual(result, math.sqrt(0.6), places=9)

class Statistics3TestCorrelationMatrix(unittest.TestCase):
    def test_correlation_matrix(self):
        statistics3 = Statistics3()
        self.assertEqual(statistics3.correlation_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]])

    def test_correlation_matrix_2(self):
        statistics3 = Statistics3()
        self.assertEqual(statistics3.correlation_matrix([[1, 2, 3], [4, 5, 6]]), [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]])

    def test_correlation_matrix_3(self):
        statistics3 = Statistics3()
        self.assertEqual(statistics3.correlation_matrix([[1, 2, 3]]), [[None, None, None], [None, None, None], [None, None, None]])

import math

class AgentTest_correlation_matrix(unittest.TestCase):
    def test_correlation_matrix_1(self):
        statistics3 = Statistics3()
        result = statistics3.correlation_matrix([[1, 3], [2, 2], [3, 1]])
        self.assertEqual(len(result), 2)
        for row in result:
            self.assertEqual(len(row), 2)
        self.assertAlmostEqual(result[0][0], 1.0, places=9)
        self.assertAlmostEqual(result[0][1], -1.0, places=9)
        self.assertAlmostEqual(result[1][0], -1.0, places=9)
        self.assertAlmostEqual(result[1][1], 1.0, places=9)

    def test_correlation_matrix_2(self):
        statistics3 = Statistics3()
        result = statistics3.correlation_matrix([[1, 2], [2, 4], [3, 5], [4, 4], [5, 5]])
        self.assertEqual(len(result), 2)
        for row in result:
            self.assertEqual(len(row), 2)
        self.assertAlmostEqual(result[0][0], 1.0, places=9)
        self.assertAlmostEqual(result[0][1], math.sqrt(0.6), places=9)
        self.assertAlmostEqual(result[1][0], math.sqrt(0.6), places=9)
        self.assertAlmostEqual(result[1][1], 1.0, places=9)

class Statistics3TestStandardDeviation(unittest.TestCase):
    def test_standard_deviation(self):
        statistics3 = Statistics3()
        self.assertEqual(statistics3.standard_deviation([1, 2, 3]), 1.0)

    def test_standard_deviation_2(self):
        statistics3 = Statistics3()
        self.assertEqual(statistics3.standard_deviation([1, 1, 1]), 0.0)

    def test_standard_deviation_3(self):
        statistics3 = Statistics3()
        self.assertEqual(statistics3.standard_deviation([1, 1]), 0.0)

import math

class AgentTest_standard_deviation(unittest.TestCase):
    def test_standard_deviation_1(self):
        statistics3 = Statistics3()
        result = statistics3.standard_deviation([-1, 1])
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, math.sqrt(2), places=9)

    def test_standard_deviation_2(self):
        statistics3 = Statistics3()
        result = statistics3.standard_deviation([2, 4, 4, 4, 5, 5, 7, 9])
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, math.sqrt(32 / 7), places=9)

class Statistics3TestZScore(unittest.TestCase):
    def test_z_score(self):
        statistics3 = Statistics3()
        self.assertEqual(statistics3.z_score([1, 2, 3, 4]), [-1.161895003862225, -0.3872983346207417, 0.3872983346207417, 1.161895003862225])

    def test_z_score_2(self):
        statistics3 = Statistics3()
        self.assertEqual(statistics3.z_score([1, 1, 1, 1]), None)

    def test_z_score_3(self):
        statistics3 = Statistics3()
        self.assertEqual(statistics3.z_score([1]),None)

import unittest

class AgentTest_z_score(unittest.TestCase):
    def test_z_score_1(self):
        statistics3 = Statistics3()
        result = statistics3.z_score([2, 4, 6])
        expected = [-1.0, 0.0, 1.0]
        self.assertEqual(len(result), len(expected))
        for actual, exp in zip(result, expected):
            self.assertAlmostEqual(actual, exp, places=9)

    def test_z_score_2(self):
        statistics3 = Statistics3()
        result = statistics3.z_score([3, 1, 2])
        expected = [1.0, -1.0, 0.0]
        self.assertEqual(len(result), len(expected))
        for actual, exp in zip(result, expected):
            self.assertAlmostEqual(actual, exp, places=9)