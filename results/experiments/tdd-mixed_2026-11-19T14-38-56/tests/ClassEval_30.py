import unittest




class DataStatistics2TestGetSum(unittest.TestCase):
    def test_get_sum_1(self):
        ds2 = DataStatistics2([1, 2, 3, 4])
        res = ds2.get_sum()
        self.assertEqual(res, 10)

    def test_get_sum_2(self):
        ds2 = DataStatistics2([1, 2, 203, 4])
        res = ds2.get_sum()
        self.assertEqual(res, 210)

    def test_get_sum_3(self):
        ds2 = DataStatistics2([1, 2, 33, 4])
        res = ds2.get_sum()
        self.assertEqual(res, 40)

import unittest

class AgentTest_get_sum(unittest.TestCase):
    def test_get_sum_1(self):
        ds2 = DataStatistics2([-5, 10, -3])
        res = ds2.get_sum()
        self.assertEqual(res, 2)

    def test_get_sum_2(self):
        ds2 = DataStatistics2([1.5, 2.5, 3.0])
        res = ds2.get_sum()
        self.assertEqual(res, 7.0)

class DataStatistics2TestGetMin(unittest.TestCase):
    def test_get_min_1(self):
        ds2 = DataStatistics2([1, 2, 3, 4])
        res = ds2.get_min()
        self.assertEqual(res, 1)

    def test_get_min_2(self):
        ds2 = DataStatistics2([1, 2, 203, 4])
        res = ds2.get_min()
        self.assertEqual(res, 1)

    def test_get_min_3(self):
        ds2 = DataStatistics2([0, -1, -3, 2])
        res = ds2.get_min()
        self.assertEqual(res, -3)

import unittest

class AgentTest_get_min(unittest.TestCase):
    def test_get_min_1(self):
        ds2 = DataStatistics2([-7, -2, -15, -4])
        res = ds2.get_min()
        self.assertEqual(res, -15)

    def test_get_min_2(self):
        ds2 = DataStatistics2([2.5, 2.5, 3.1])
        res = ds2.get_min()
        self.assertEqual(res, 2.5)

class DataStatistics2TestGetMax(unittest.TestCase):
    def test_get_max_1(self):
        ds2 = DataStatistics2([1, 2, 3, 4])
        res = ds2.get_max()
        self.assertEqual(res, 4)

    def test_get_max_2(self):
        ds2 = DataStatistics2([1, 2, 203, 4])
        res = ds2.get_max()
        self.assertEqual(res, 203)

    def test_get_max_3(self):
        ds2 = DataStatistics2([-1, -4, 3, 2])
        res = ds2.get_max()
        self.assertEqual(res, 3)

class AgentTest_get_max(unittest.TestCase):
    def test_get_max_1(self):
        ds2 = DataStatistics2([1.5, 2.5, 0.5])
        res = ds2.get_max()
        self.assertEqual(res, 2.5)

    def test_get_max_2(self):
        ds2 = DataStatistics2([42])
        res = ds2.get_max()
        self.assertEqual(res, 42)

class DataStatistics2TestGetVariance(unittest.TestCase):
    def test_get_variance_1(self):
        ds2 = DataStatistics2([1, 2, 3, 4])
        res = ds2.get_variance()
        self.assertEqual(res, 1.25)

    def test_get_variance_2(self):
        ds2 = DataStatistics2([1, 2, 203, 4])
        res = ds2.get_variance()
        self.assertEqual(res, 7551.25)

    def test_get_variance_3(self):
        ds2 = DataStatistics2([1, 4, 3, 2])
        res = ds2.get_variance()
        self.assertEqual(res, 1.25)

import unittest

import numpy as np

class AgentTest_get_variance(unittest.TestCase):
    def test_get_variance_1(self):
        ds2 = DataStatistics2([5, 5, 5])
        res = ds2.get_variance()
        self.assertAlmostEqual(res, 0.0, places=2)

    def test_get_variance_2(self):
        ds2 = DataStatistics2([-1.5, 2.5, 0.0])
        res = ds2.get_variance()
        self.assertAlmostEqual(res, 2.72, places=2)

class DataStatistics2TestGetStdDeviation(unittest.TestCase):
    def test_get_std_deviation_1(self):
        ds2 = DataStatistics2([1, 2, 3, 4])
        res = ds2.get_std_deviation()
        self.assertEqual(res, 1.12)

    def test_get_std_deviation_2(self):
        ds2 = DataStatistics2([1, 2, 203, 4])
        res = ds2.get_std_deviation()
        self.assertEqual(res, 86.9)

    def test_get_std_deviation_3(self):
        ds2 = DataStatistics2([1, 4, 3, 2])
        res = ds2.get_std_deviation()
        self.assertEqual(res, 1.12)

import unittest

class AgentTest_get_std_deviation(unittest.TestCase):
    def test_get_std_deviation_1(self):
        ds2 = DataStatistics2([5, 5, 5])
        res = ds2.get_std_deviation()
        self.assertAlmostEqual(res, 0.0, places=2)

    def test_get_std_deviation_2(self):
        ds2 = DataStatistics2([2, 4, 4, 4, 5, 5, 7, 9])
        res = ds2.get_std_deviation()
        self.assertAlmostEqual(res, 2.0, places=2)

class DataStatistics2TestGetCorrelation(unittest.TestCase):
    def test_get_correlation_1(self):
        ds2 = DataStatistics2([1, 2, 3, 4])
        res = ds2.get_correlation()
        self.assertEqual(res, 1.0)

    def test_get_correlation_2(self):
        ds2 = DataStatistics2([1, 2, 203, 4])
        res = ds2.get_correlation()
        self.assertEqual(res, 1.0)

    def test_get_correlation_3(self):
        ds2 = DataStatistics2([1, 4, 3, 2])
        res = ds2.get_correlation()
        self.assertEqual(res, 1.0)

import unittest

import numpy as np

class AgentTest_get_correlation(unittest.TestCase):
    def test_get_correlation_1(self):
        ds2 = DataStatistics2([5, 3, 8, 1, 7])
        res = ds2.get_correlation()
        self.assertIsInstance(res, float)

    def test_get_correlation_2(self):
        ds2 = DataStatistics2([5, 3, 8, 1, 7])
        res = ds2.get_correlation()
        self.assertGreaterEqual(res, -1.0)
        self.assertLessEqual(res, 1.0)