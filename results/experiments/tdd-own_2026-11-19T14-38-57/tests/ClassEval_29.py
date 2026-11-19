import unittest


import unittest

class AgentTest_mean(unittest.TestCase):

    def test_mean_1(self):
        ds = DataStatistics()
        result = ds.mean([1, 2, 3, 4, 5])
        self.assertAlmostEqual(result, 3.00, places=2)

    def test_mean_2(self):
        ds = DataStatistics()
        result = ds.mean([1, 2, 2])
        self.assertAlmostEqual(result, 1.67, places=2)

    def test_mean_3(self):
        ds = DataStatistics()
        result = ds.mean([-1, -2, -3, -4])
        self.assertAlmostEqual(result, -2.50, places=2)

    def test_mean_4(self):
        ds = DataStatistics()
        result = ds.mean([7])
        self.assertAlmostEqual(result, 7.00, places=2)

    def test_mean_5(self):
        ds = DataStatistics()
        result = ds.mean([1.5, 2.5, 3.5])
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, 2.50, places=2)

import unittest

class AgentTest_median(unittest.TestCase):

    def test_median_1(self):
        ds = DataStatistics()
        result = ds.median([2, 5, 1, 3, 4])
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, 3.00, places=2)

    def test_median_2(self):
        ds = DataStatistics()
        result = ds.median([1, 2, 3, 4])
        self.assertAlmostEqual(result, 2.50, places=2)

    def test_median_3(self):
        ds = DataStatistics()
        result = ds.median([7])
        self.assertAlmostEqual(result, 7.00, places=2)

    def test_median_4(self):
        ds = DataStatistics()
        result = ds.median([-5, -1, -3])
        self.assertAlmostEqual(result, -3.00, places=2)

    def test_median_5(self):
        ds = DataStatistics()
        result = ds.median([4.5, 1.5, 3.0, 2.0])
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, 2.50, places=2)

import unittest

class AgentTest_mode(unittest.TestCase):

    def test_mode_1(self):
        ds = DataStatistics()
        result = ds.mode([2, 2, 3, 3, 4])
        self.assertIsInstance(result, list)
        self.assertCountEqual(result, [2, 3])

    def test_mode_2(self):
        ds = DataStatistics()
        result = ds.mode([1, 2, 2, 3])
        self.assertIsInstance(result, list)
        self.assertCountEqual(result, [2])

    def test_mode_3(self):
        ds = DataStatistics()
        result = ds.mode([1, 2, 3, 4])
        self.assertIsInstance(result, list)
        self.assertCountEqual(result, [1, 2, 3, 4])

    def test_mode_4(self):
        ds = DataStatistics()
        result = ds.mode([7])
        self.assertIsInstance(result, list)
        self.assertCountEqual(result, [7])

    def test_mode_5(self):
        ds = DataStatistics()
        result = ds.mode([-1.5, -1.5, 2.0, 3, 2.0, 2.0])
        self.assertIsInstance(result, list)
        self.assertCountEqual(result, [2.0])