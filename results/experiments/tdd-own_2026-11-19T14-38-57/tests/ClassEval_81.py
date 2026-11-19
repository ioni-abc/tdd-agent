import unittest


import unittest

class AgentTest_median(unittest.TestCase):

    def test_median_1(self):
        result = Statistics3.median([1, 2, 3, 4])
        self.assertEqual(result, 2.5)
        self.assertIsInstance(result, float)

    def test_median_2(self):
        result = Statistics3.median([1, 2, 3])
        self.assertEqual(result, 2.0)
        self.assertIsInstance(result, float)

    def test_median_3(self):
        self.assertEqual(Statistics3.median([7, 1, 5, 3, 9]), 5.0)

    def test_median_4(self):
        self.assertEqual(Statistics3.median([5]), 5.0)

    def test_median_5(self):
        self.assertEqual(Statistics3.median([-1, -1, 4, 10]), 1.5)

import unittest

class AgentTest_mode(unittest.TestCase):

    def test_mode_1(self):
        result = Statistics3.mode([1, 2, 3, 3])
        self.assertEqual(result, [3])
        self.assertIsInstance(result, list)

    def test_mode_2(self):
        result = Statistics3.mode([5])
        self.assertEqual(result, [5])
        self.assertIsInstance(result, list)

    def test_mode_3(self):
        result = Statistics3.mode([4, 4, 4, 1, 2])
        self.assertEqual(result, [4])

    def test_mode_4(self):
        result = Statistics3.mode([1, 1, 2, 2, 3])
        self.assertIsInstance(result, list)
        self.assertCountEqual(result, [1, 2])

    def test_mode_5(self):
        result = Statistics3.mode([-1.5, 2, -1.5, 7])
        self.assertEqual(result, [-1.5])

import unittest

class AgentTest_mean(unittest.TestCase):

    def test_mean_1(self):
        result = Statistics3.mean([1, 2, 3])
        self.assertEqual(result, 2.0)
        self.assertIsInstance(result, float)

    def test_mean_2(self):
        result = Statistics3.mean([5])
        self.assertEqual(result, 5.0)
        self.assertIsInstance(result, float)

    def test_mean_3(self):
        self.assertEqual(Statistics3.mean([-1, -2, -3]), -2.0)

    def test_mean_4(self):
        self.assertEqual(Statistics3.mean([1.5, 2.5]), 2.0)

    def test_mean_5(self):
        self.assertAlmostEqual(Statistics3.mean([0.1, 0.2, 0.3]), 0.2)

import unittest

class AgentTest_correlation(unittest.TestCase):

    def test_correlation_1(self):
        result = Statistics3.correlation([1, 2, 3], [4, 5, 6])
        self.assertEqual(result, 1.0)
        self.assertIsInstance(result, float)

    def test_correlation_2(self):
        self.assertAlmostEqual(Statistics3.correlation([1, 2, 3], [6, 5, 4]), -1.0)

    def test_correlation_3(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 5, 4, 5]
        self.assertAlmostEqual(Statistics3.correlation(x, y), 0.7745966692414834, places=6)

    def test_correlation_4(self):
        self.assertAlmostEqual(Statistics3.correlation([1, 2, 3, 4], [1, -1, -1, 1]), 0.0)

    def test_correlation_5(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 5, 4, 5]
        shifted = [value + 100 for value in y]
        self.assertAlmostEqual(
            Statistics3.correlation(x, shifted),
            Statistics3.correlation(x, y),
            places=6,
        )

import unittest

class AgentTest_correlation_matrix(unittest.TestCase):

    def test_correlation_matrix_1(self):
        result = Statistics3.correlation_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(result, [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]])
        self.assertIsInstance(result, list)
        for row in result:
            self.assertIsInstance(row, list)

    def test_correlation_matrix_2(self):
        data = [[1, 2, 3, 4], [2, 4, 5, 4], [1, 0, -1, 3]]
        result = Statistics3.correlation_matrix(data)
        self.assertEqual(len(result), 3)
        for i in range(3):
            self.assertAlmostEqual(result[i][i], 1.0, places=6)

    def test_correlation_matrix_3(self):
        result = Statistics3.correlation_matrix([[1, 2, 3], [3, 2, 1]])
        self.assertEqual(len(result), 2)
        self.assertAlmostEqual(result[0][0], 1.0, places=6)
        self.assertAlmostEqual(result[0][1], -1.0, places=6)
        self.assertAlmostEqual(result[1][0], -1.0, places=6)
        self.assertAlmostEqual(result[1][1], 1.0, places=6)

    def test_correlation_matrix_4(self):
        data = [[1, 2, 3, 4, 5], [2, 4, 5, 4, 5], [5, 3, 4, 1, 2]]
        result = Statistics3.correlation_matrix(data)
        self.assertAlmostEqual(result[0][1], 0.7745966692414834, places=6)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(result[i][j], result[j][i], places=6)

    def test_correlation_matrix_5(self):
        data = [[1, 2, 3, 4, 5], [2, 4, 5, 4, 5], [5, 3, 4, 1, 2]]
        result = Statistics3.correlation_matrix(data)
        self.assertEqual(len(result), 3)
        for row in result:
            self.assertEqual(len(row), 3)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(
                    result[i][j],
                    Statistics3.correlation(data[i], data[j]),
                    places=6,
                )

import math

import unittest

class AgentTest_standard_deviation(unittest.TestCase):

    def test_standard_deviation_1(self):
        result = Statistics3.standard_deviation([1, 2, 3])
        self.assertEqual(result, 1.0)
        self.assertIsInstance(result, float)

    def test_standard_deviation_2(self):
        result = Statistics3.standard_deviation([1, 2, 3, 4])
        self.assertAlmostEqual(result, math.sqrt(5 / 3), places=6)

    def test_standard_deviation_3(self):
        self.assertAlmostEqual(Statistics3.standard_deviation([4, 4, 4]), 0.0, places=6)

    def test_standard_deviation_4(self):
        self.assertAlmostEqual(Statistics3.standard_deviation([-1, -2, -3]), 1.0, places=6)

    def test_standard_deviation_5(self):
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        self.assertAlmostEqual(
            Statistics3.standard_deviation(data),
            math.sqrt(32 / 7),
            places=6,
        )

import math

import unittest

class AgentTest_z_score(unittest.TestCase):

    def test_z_score_1(self):
        result = Statistics3.z_score([1, 2, 3, 4])
        expected = [-1.161895003862225, -0.3872983346207417, 0.3872983346207417, 1.161895003862225]
        self.assertEqual(len(result), 4)
        for actual, exp in zip(result, expected):
            self.assertAlmostEqual(actual, exp, places=6)

    def test_z_score_2(self):
        result = Statistics3.z_score([3, 7, 1, 9, 5])
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 5)
        for value in result:
            self.assertIsInstance(value, float)

    def test_z_score_3(self):
        result = Statistics3.z_score([1, 2, 3])
        self.assertAlmostEqual(result[0], -1.0, places=6)
        self.assertAlmostEqual(result[1], 0.0, places=6)
        self.assertAlmostEqual(result[2], 1.0, places=6)

    def test_z_score_4(self):
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        result = Statistics3.z_score(data)
        mean = 5.0
        std = math.sqrt(32 / 7)
        for actual, x in zip(result, data):
            self.assertAlmostEqual(actual, (x - mean) / std, places=6)

    def test_z_score_5(self):
        data = [-4.5, 0.5, 2.0, 7.0, 10.0]
        result = Statistics3.z_score(data)
        self.assertAlmostEqual(Statistics3.mean(result), 0.0, places=6)
        self.assertAlmostEqual(Statistics3.standard_deviation(result), 1.0, places=6)