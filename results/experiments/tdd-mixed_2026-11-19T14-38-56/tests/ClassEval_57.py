import unittest




class MetricsCalculator2TestMrr(unittest.TestCase):
    def test_mrr_1(self):
        mc2 = MetricsCalculator2()
        res1, res2 = MetricsCalculator2.mrr(([1, 0, 1, 0], 4))
        self.assertEqual(res1, 1.0)
        self.assertEqual(res2, [1.0])

    def test_mrr_2(self):
        res1, res2 = MetricsCalculator2.mrr(([0, 0, 0, 1], 4))
        self.assertEqual(res1, 0.25)
        self.assertEqual(res2, [0.25])

    def test_mrr_3(self):
        res1, res2 = MetricsCalculator2.mrr([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
        self.assertEqual(res1, 0.75)
        self.assertEqual(res2, [1.0, 0.5])

    def test_mrr_4(self):
        res1, res2 = MetricsCalculator2.mrr([([1, 1, 1, 0], 4), ([0, 0, 0, 1], 4)])
        self.assertEqual(res1, 0.625)
        self.assertEqual(res2, [1.0, 0.25])

    def test_mrr_5(self):
        res1, res2 = MetricsCalculator2.mrr([([1, 0, 1, 1], 4), ([0, 1, 0, 0], 4)])
        self.assertEqual(res1, 0.75)
        self.assertEqual(res2, [1.0, 0.5])

import unittest

class AgentTest_mrr(unittest.TestCase):
    def test_mrr_1(self):
        res1, res2 = MetricsCalculator2.mrr([([0, 1, 1, 1], 4)])
        self.assertAlmostEqual(res1, 0.5)
        self.assertEqual(len(res2), 1)
        self.assertAlmostEqual(res2[0], 0.5)

    def test_mrr_2(self):
        res1, res2 = MetricsCalculator2.mrr([([1, 0], 2), ([0, 1], 2), ([0, 0, 1], 2)])
        expected = [1.0, 0.5, 1.0 / 3]
        self.assertAlmostEqual(res1, sum(expected) / 3)
        self.assertEqual(len(res2), 3)
        for actual, exp in zip(res2, expected):
            self.assertAlmostEqual(actual, exp)

    def test_mrr_3(self):
        res1, res2 = MetricsCalculator2.mrr([([0, 0, 1, 0], 2), ([0, 0, 1, 0], 100)])
        self.assertAlmostEqual(res1, 1.0 / 3)
        self.assertEqual(len(res2), 2)
        self.assertAlmostEqual(res2[0], 1.0 / 3)
        self.assertAlmostEqual(res2[1], 1.0 / 3)

class MetricsCalculator2TestMap(unittest.TestCase):
    def test_map_1(self):
        res1, res2 = MetricsCalculator2.map(([1, 0, 1, 0], 4))
        self.assertEqual(res1, 0.41666666666666663)
        self.assertEqual(res2, [0.41666666666666663])

    def test_map_2(self):
        res1, res2 = MetricsCalculator2.map(([0, 0, 0, 1], 4))
        self.assertEqual(res1, 0.0625)
        self.assertEqual(res2, [0.0625])

    def test_map_3(self):
        res1, res2 = MetricsCalculator2.map([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
        self.assertEqual(res1, 0.3333333333333333)
        self.assertEqual(res2, [0.41666666666666663, 0.25])

    def test_map_4(self):
        res1, res2 = MetricsCalculator2.map([([1, 1, 1, 0], 4), ([0, 0, 0, 1], 4)])
        self.assertEqual(res1, 0.40625)
        self.assertEqual(res2, [0.75, 0.0625])

    def test_map_5(self):
        res1, res2 = MetricsCalculator2.map([([1, 0, 1, 1], 4), ([0, 1, 0, 0], 4)])
        self.assertEqual(res1, 0.3645833333333333)
        self.assertEqual(res2, [0.6041666666666666, 0.125])

import unittest

class AgentTest_map(unittest.TestCase):
    def test_map_1(self):
        res1, res2 = MetricsCalculator2.map(([0, 0, 0], 3))
        self.assertAlmostEqual(res1, 0.0)
        self.assertEqual(len(res2), 1)
        self.assertAlmostEqual(res2[0], 0.0)

    def test_map_2(self):
        res1, res2 = MetricsCalculator2.map(([1, 0, 0, 1, 0, 1], 10))
        self.assertAlmostEqual(res1, 0.2)
        self.assertEqual(len(res2), 1)
        self.assertAlmostEqual(res2[0], 0.2)

    def test_map_3(self):
        res1, res2 = MetricsCalculator2.map([([1, 1], 2), ([1, 0, 0], 1), ([0, 1], 2)])
        expected = [1.0, 1.0, 0.25]
        self.assertAlmostEqual(res1, 0.75)
        self.assertEqual(len(res2), 3)
        for actual, exp in zip(res2, expected):
            self.assertAlmostEqual(actual, exp)