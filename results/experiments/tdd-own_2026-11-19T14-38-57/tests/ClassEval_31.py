import unittest


import unittest

import math

class AgentTest_correlation_coefficient(unittest.TestCase):

    def test_correlation_coefficient_1(self):
        # Docstring example
        result = DataStatistics4.correlation_coefficient([1, 2, 3], [4, 5, 6])
        self.assertAlmostEqual(result, 0.9999999999999998, places=7)

    def test_correlation_coefficient_2(self):
        # Perfect positive linear relationship gives a coefficient of 1
        result = DataStatistics4.correlation_coefficient([1, 2, 3, 4], [10, 20, 30, 40])
        self.assertAlmostEqual(result, 1.0, places=7)

    def test_correlation_coefficient_3(self):
        # Perfect negative linear relationship gives a coefficient of -1
        result = DataStatistics4.correlation_coefficient([1, 2, 3], [3, 2, 1])
        self.assertAlmostEqual(result, -1.0, places=7)

    def test_correlation_coefficient_4(self):
        # Correlation is symmetric: swapping the two data sets gives the same result
        data1 = [2.0, 4.5, 1.0, 7.0, 3.5]
        data2 = [1.5, 3.0, 2.5, 6.0, 4.0]
        forward = DataStatistics4.correlation_coefficient(data1, data2)
        backward = DataStatistics4.correlation_coefficient(data2, data1)
        self.assertAlmostEqual(forward, backward, places=7)

    def test_correlation_coefficient_5(self):
        # The result is a float and lies within the range [-1, 1]
        result = DataStatistics4.correlation_coefficient([1, 3, 2, 5, 4], [2, 1, 4, 3, 6])
        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, -1.0)
        self.assertLessEqual(result, 1.0)

import unittest

import math

class AgentTest_skewness(unittest.TestCase):

    def test_skewness_1(self):
        # Docstring example
        result = DataStatistics4.skewness([1, 2, 5])
        self.assertAlmostEqual(result, 2.3760224064818463, places=7)

    def test_skewness_2(self):
        # A perfectly symmetric data set has zero skewness
        result = DataStatistics4.skewness([1, 2, 3, 4, 5])
        self.assertAlmostEqual(result, 0.0, places=7)

    def test_skewness_3(self):
        # Negating every value reverses the asymmetry, so the skewness changes sign
        positive = DataStatistics4.skewness([1, 2, 5])
        negative = DataStatistics4.skewness([-1, -2, -5])
        self.assertAlmostEqual(negative, -positive, places=7)

    def test_skewness_4(self):
        # A long right tail (one large outlier) gives positive skewness
        result = DataStatistics4.skewness([1, 2, 3, 4, 100])
        self.assertGreater(result, 0.0)

    def test_skewness_5(self):
        # The result is returned as a float
        result = DataStatistics4.skewness([1, 2, 5])
        self.assertIsInstance(result, float)

import unittest

import math

class AgentTest_kurtosis(unittest.TestCase):

    def test_kurtosis_1(self):
        # Docstring example
        result = DataStatistics4.kurtosis([1, 20, 100])
        self.assertAlmostEqual(result, -1.5000000000000007, places=7)

    def test_kurtosis_2(self):
        # For [1, 2, 3, 4, 5] the population second moment is 2 and the fourth is 6.8,
        # so the kurtosis (in the same convention as the docstring example) is 6.8/4 - 3 = -1.3
        result = DataStatistics4.kurtosis([1, 2, 3, 4, 5])
        self.assertAlmostEqual(result, -1.3, places=7)

    def test_kurtosis_3(self):
        # Kurtosis describes the shape of the distribution, so adding a constant to every value leaves it unchanged
        original = DataStatistics4.kurtosis([1, 20, 100])
        shifted = DataStatistics4.kurtosis([11, 30, 110])
        self.assertAlmostEqual(original, shifted, places=7)

    def test_kurtosis_4(self):
        # Kurtosis is unchanged when every value is multiplied by the same non-zero factor
        original = DataStatistics4.kurtosis([1, 20, 100])
        scaled = DataStatistics4.kurtosis([2, 40, 200])
        self.assertAlmostEqual(original, scaled, places=7)

    def test_kurtosis_5(self):
        # The result is returned as a float
        result = DataStatistics4.kurtosis([1, 20, 100])
        self.assertIsInstance(result, float)

import unittest

import math

class AgentTest_pdf(unittest.TestCase):

    def test_pdf_1(self):
        # Docstring example
        result = DataStatistics4.pdf([1, 2, 3], 1, 1)
        expected = [0.3989422804014327, 0.24197072451914337, 0.05399096651318806]
        self.assertEqual(len(result), len(expected))
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, places=7)

    def test_pdf_2(self):
        # At the mean of a standard normal distribution the density is 1/sqrt(2*pi)
        result = DataStatistics4.pdf([0], 0, 1)
        self.assertAlmostEqual(result[0], 1 / math.sqrt(2 * math.pi), places=7)

    def test_pdf_3(self):
        # The normal density is symmetric about the mean
        result = DataStatistics4.pdf([4.0, 6.0], 5, 2)
        self.assertAlmostEqual(result[0], result[1], places=7)

    def test_pdf_4(self):
        # One standard deviation from the mean: density is exp(-0.5) / (sigma * sqrt(2*pi))
        sigma = 2.0
        result = DataStatistics4.pdf([5 + sigma], 5, sigma)
        expected = math.exp(-0.5) / (sigma * math.sqrt(2 * math.pi))
        self.assertAlmostEqual(result[0], expected, places=7)

    def test_pdf_5(self):
        # The result is a list with one float per input value
        result = DataStatistics4.pdf([1, 2, 3, 4], 2.5, 1.5)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 4)
        for value in result:
            self.assertIsInstance(value, float)