import unittest




class DataStatisticsTestMean(unittest.TestCase):
    def test_mean_1(self):
        ds = DataStatistics()
        res = ds.mean([1, 2, 3, 4, 5])
        self.assertEqual(res, 3.00)

    def test_mean_2(self):
        ds = DataStatistics()
        res = ds.mean([1, 2, 3, 4, 5, 6])
        self.assertEqual(res, 3.50)

    def test_mean_3(self):
        ds = DataStatistics()
        res = ds.mean([1, 2, 4, 5, 6, 7])
        self.assertEqual(res, 4.17)

import unittest

class AgentTest_mean(unittest.TestCase):
    def test_mean_1(self):
        ds = DataStatistics()
        res = ds.mean([-4, -1, 2.5, 3.5])
        self.assertEqual(res, 0.25)

    def test_mean_2(self):
        ds = DataStatistics()
        res = ds.mean([1, 1, 2])
        self.assertEqual(res, 1.33)

class DataStatisticsTestMedian(unittest.TestCase):
    def test_median_1(self):
        ds = DataStatistics()
        res = ds.median([2, 5, 1, 3, 4])
        self.assertEqual(res, 3)

    def test_median_2(self):
        ds = DataStatistics()
        res = ds.median([2, 5, 1, 3, 4, 6])
        self.assertEqual(res, 3.50)

    def test_median_3(self):
        ds = DataStatistics()
        res = ds.median([2, 5, 1, 4, 6, 7])
        self.assertEqual(res, 4.5)

import unittest

class AgentTest_median(unittest.TestCase):
    def test_median_1(self):
        ds = DataStatistics()
        res = ds.median([-7, -3, -10, 8, 5])
        self.assertEqual(res, -3.00)

    def test_median_2(self):
        ds = DataStatistics()
        res = ds.median([4, 4, 1, 9])
        self.assertEqual(res, 4.00)

class DataStatisticsTestMode(unittest.TestCase):
    def test_mode_1(self):
        ds = DataStatistics()
        res = ds.mode([2, 2, 3, 3, 4])
        self.assertEqual(res, [2, 3])

    def test_mode_2(self):
        ds = DataStatistics()
        res = ds.mode([2, 2, 2, 3, 3, 4])
        self.assertEqual(res, [2])

    def test_mode_3(self):
        ds = DataStatistics()
        res = ds.mode([2, 2, 3, 3, 4, 4])
        self.assertEqual(res, [2, 3, 4])

import unittest

from collections import Counter

class AgentTest_mode(unittest.TestCase):
    def test_mode_1(self):
        ds = DataStatistics()
        res = ds.mode([7])
        self.assertEqual(res, [7])

    def test_mode_2(self):
        ds = DataStatistics()
        res = ds.mode([-1, 2.5, -1, 2.5, 2.5, 0])
        self.assertEqual(res, [2.5])