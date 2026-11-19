import unittest


import unittest

class AgentTest_get_sum(unittest.TestCase):

    def test_get_sum_1(self):
        # Example from the docstring
        ds2 = DataStatistics2([1, 2, 3, 4])
        self.assertEqual(ds2.get_sum(), 10)

    def test_get_sum_2(self):
        # Negative and positive values summing to zero
        ds2 = DataStatistics2([-1, -2, 3])
        self.assertEqual(ds2.get_sum(), 0)

    def test_get_sum_3(self):
        # Floating-point values
        ds2 = DataStatistics2([0.5, 1.25, 2.25])
        self.assertAlmostEqual(ds2.get_sum(), 4.0)

    def test_get_sum_4(self):
        # Single-element dataset
        ds2 = DataStatistics2([7])
        self.assertEqual(ds2.get_sum(), 7)

    def test_get_sum_5(self):
        # Larger dataset: sum of 1..100
        ds2 = DataStatistics2(list(range(1, 101)))
        self.assertEqual(ds2.get_sum(), 5050)

import numpy as np

class AgentTest_get_min(unittest.TestCase):

    def test_get_min_1(self):
        # Example from the docstring
        ds2 = DataStatistics2([1, 2, 3, 4])
        self.assertEqual(ds2.get_min(), 1)

    def test_get_min_2(self):
        # Negative and positive values: minimum is the most negative value
        ds2 = DataStatistics2([3, -7, 0, 5, -2])
        self.assertEqual(ds2.get_min(), -7)

    def test_get_min_3(self):
        # Floating-point values
        ds2 = DataStatistics2([0.5, 1.25, -0.75, 2.25])
        self.assertAlmostEqual(ds2.get_min(), -0.75)

    def test_get_min_4(self):
        # Single-element dataset: the only value is the minimum
        ds2 = DataStatistics2([7])
        self.assertEqual(ds2.get_min(), 7)

    def test_get_min_5(self):
        # Minimum is not at the start or end of the dataset
        ds2 = DataStatistics2([10, 4, 25, 1, 9, 16])
        self.assertEqual(ds2.get_min(), 1)

import numpy as np

class AgentTest_get_max(unittest.TestCase):

    def test_get_max_1(self):
        # Example from the docstring
        ds2 = DataStatistics2([1, 2, 3, 4])
        self.assertEqual(ds2.get_max(), 4)

    def test_get_max_2(self):
        # Negative and positive values: maximum is the largest value
        ds2 = DataStatistics2([-10, -3, 0, 5, -2])
        self.assertEqual(ds2.get_max(), 5)

    def test_get_max_3(self):
        # All negative values: maximum is the one closest to zero
        ds2 = DataStatistics2([-8.5, -0.25, -3.0])
        self.assertAlmostEqual(ds2.get_max(), -0.25)

    def test_get_max_4(self):
        # Single-element dataset: the only value is the maximum
        ds2 = DataStatistics2([7])
        self.assertEqual(ds2.get_max(), 7)

    def test_get_max_5(self):
        # Maximum is not at the start or end of the dataset
        ds2 = DataStatistics2([10, 40, 25, 1, 9, 16])
        self.assertEqual(ds2.get_max(), 40)

import unittest

class AgentTest_get_variance(unittest.TestCase):

    def test_get_variance_1(self):
        # Example from the docstring
        ds2 = DataStatistics2([1, 2, 3, 4])
        self.assertAlmostEqual(ds2.get_variance(), 1.25, places=2)

    def test_get_variance_2(self):
        # All values identical: no spread, so variance is zero
        ds2 = DataStatistics2([5, 5, 5, 5])
        self.assertAlmostEqual(ds2.get_variance(), 0.0, places=2)

    def test_get_variance_3(self):
        # Classic dataset with known population variance of 4.0
        ds2 = DataStatistics2([2, 4, 4, 4, 5, 5, 7, 9])
        self.assertAlmostEqual(ds2.get_variance(), 4.0, places=2)

    def test_get_variance_4(self):
        # Negative values: deviations from mean -2 are 1, 0, 1; sum 2 / 3 = 0.67
        ds2 = DataStatistics2([-1, -2, -3])
        self.assertAlmostEqual(ds2.get_variance(), 0.67, places=2)

    def test_get_variance_5(self):
        # Larger dataset 1..100: population variance is (n^2 - 1) / 12 = 833.25
        ds2 = DataStatistics2(list(range(1, 101)))
        self.assertAlmostEqual(ds2.get_variance(), 833.25, places=2)

class AgentTest_get_std_deviation(unittest.TestCase):

    def test_get_std_deviation_1(self):
        # Example from the docstring: sqrt(1.25) is approximately 1.118, shown as 1.12
        ds2 = DataStatistics2([1, 2, 3, 4])
        self.assertAlmostEqual(ds2.get_std_deviation(), 1.12, places=2)

    def test_get_std_deviation_2(self):
        # All values identical: no spread, so standard deviation is zero
        ds2 = DataStatistics2([5, 5, 5, 5])
        self.assertAlmostEqual(ds2.get_std_deviation(), 0.0, places=2)

    def test_get_std_deviation_3(self):
        # Classic dataset with known population variance of 4.0, so standard deviation is 2.0
        ds2 = DataStatistics2([2, 4, 4, 4, 5, 5, 7, 9])
        self.assertAlmostEqual(ds2.get_std_deviation(), 2.0, places=2)

    def test_get_std_deviation_4(self):
        # Negative values: population variance is 0.67, so standard deviation is about 0.82
        ds2 = DataStatistics2([-1, -2, -3])
        self.assertAlmostEqual(ds2.get_std_deviation(), 0.82, places=2)

    def test_get_std_deviation_5(self):
        # Larger dataset 1..100: population variance is 833.25, so standard deviation is about 28.87
        ds2 = DataStatistics2(list(range(1, 101)))
        self.assertAlmostEqual(ds2.get_std_deviation(), 28.87, places=2)

import unittest

class AgentTest_get_correlation(unittest.TestCase):

    def test_get_correlation_1(self):
        # Example from the docstring
        ds2 = DataStatistics2([1, 2, 3, 4])
        self.assertAlmostEqual(ds2.get_correlation(), 1.0)

    def test_get_correlation_2(self):
        # Return value is a float, as stated in the docstring
        ds2 = DataStatistics2([1, 2, 3, 4])
        self.assertIsInstance(ds2.get_correlation(), float)

    def test_get_correlation_3(self):
        # Correlation is a normalised measure, so it must lie within [-1, 1]
        ds2 = DataStatistics2([3, 1, 4, 1, 5, 9, 2, 6])
        result = ds2.get_correlation()
        self.assertGreaterEqual(result, -1.0)
        self.assertLessEqual(result, 1.0)

    def test_get_correlation_4(self):
        # Mixed-sign integer dataset: result must still lie within [-1, 1]
        ds2 = DataStatistics2([10, -4, 7, 0, 2])
        result = ds2.get_correlation()
        self.assertGreaterEqual(result, -1.0)
        self.assertLessEqual(result, 1.0)

    def test_get_correlation_5(self):
        # Floating-point dataset: result must still lie within [-1, 1]
        ds2 = DataStatistics2([0.5, 1.25, 2.25, 3.0])
        result = ds2.get_correlation()
        self.assertGreaterEqual(result, -1.0)
        self.assertLessEqual(result, 1.0)