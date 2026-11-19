import unittest




class DataStatistics4TestCorrelationCoefficient(unittest.TestCase):
    def test_correlation_coefficient(self):
        self.assertEqual(DataStatistics4.correlation_coefficient([1, 2, 3], [4, 5, 6]), 0.9999999999999998)

    def test_correlation_coefficient_2(self):
        self.assertEqual(DataStatistics4.correlation_coefficient([1, 1, 1], [2, 2, 2]), 0)

    def test_correlation_coefficient_3(self):
        self.assertEqual(DataStatistics4.correlation_coefficient([1, 2, 3], [1, 2, 3]), 0.9999999999999998)

import unittest

import math

class AgentTest_correlation_coefficient(unittest.TestCase):
    def test_correlation_coefficient_1(self):
        self.assertAlmostEqual(DataStatistics4.correlation_coefficient([1, 2, 3], [6, 5, 4]), -1.0, places=10)

    def test_correlation_coefficient_2(self):
        self.assertAlmostEqual(
            DataStatistics4.correlation_coefficient([1, 2, 3, 4, 5], [2, 4, 5, 4, 5]),
            6 / math.sqrt(60),
            places=10
        )

class DataStatistics4TestSkewness(unittest.TestCase):
    def test_skewness(self):
        self.assertEqual(DataStatistics4.skewness([1, 2, 5]), 2.3760224064818463)

    def test_skewness_2(self):
        self.assertEqual(DataStatistics4.skewness([1, 1, 1]), 0)

    def test_skewness_3(self):
        self.assertEqual(DataStatistics4.skewness([1, 2, 3]), 0)

import unittest

import math

class AgentTest_skewness(unittest.TestCase):
    def test_skewness_1(self):
        self.assertAlmostEqual(DataStatistics4.skewness([1, 2, 3, 4, 5]), 0, places=10)

    def test_skewness_2(self):
        self.assertAlmostEqual(DataStatistics4.skewness([-2, -1, 0, 1, 2]), 0, places=10)

class DataStatistics4TestKurtosis(unittest.TestCase):
    def test_kurtosis(self):
        self.assertEqual(DataStatistics4.kurtosis([1, 2, 5]), -1.5000000000000002)

    def test_kurtosis_2(self):
        self.assertTrue(math.isnan(DataStatistics4.kurtosis([1, 1, 1])))

    def test_kurtosis_3(self):
        self.assertEqual(DataStatistics4.kurtosis([1, 2, 3]), -1.5000000000000002)

import unittest

import math

class AgentTest_kurtosis(unittest.TestCase):
    def test_kurtosis_1(self):
        self.assertAlmostEqual(DataStatistics4.kurtosis([1, 20, 100]), -1.5000000000000007, places=10)

    def test_kurtosis_2(self):
        self.assertIsInstance(DataStatistics4.kurtosis([1, 20, 100]), float)

class DataStatistics4TestPDF(unittest.TestCase):
    def test_pdf(self):
        self.assertEqual(DataStatistics4.pdf([1, 2, 3], 1, 1),
                         [0.3989422804014327, 0.24197072451914337, 0.05399096651318806])

    def test_pdf_2(self):
        self.assertEqual(DataStatistics4.pdf([1, 1, 1], 1, 1),
                         [0.3989422804014327, 0.3989422804014327, 0.3989422804014327])

    def test_pdf_3(self):
        self.assertEqual(DataStatistics4.pdf([1, 2, 3], 2, 1),
                         [0.24197072451914337, 0.3989422804014327, 0.24197072451914337])

import math

class AgentTest_pdf(unittest.TestCase):
    def test_pdf_1(self):
        result = DataStatistics4.pdf([0, 2], 1, 1)
        expected = math.exp(-0.5) / math.sqrt(2 * math.pi)
        self.assertEqual(len(result), 2)
        self.assertAlmostEqual(result[0], expected, places=12)
        self.assertAlmostEqual(result[1], expected, places=12)

    def test_pdf_2(self):
        result = DataStatistics4.pdf([2], 0, 2)
        expected = math.exp(-0.5) / (2 * math.sqrt(2 * math.pi))
        self.assertEqual(len(result), 1)
        self.assertAlmostEqual(result[0], expected, places=12)