import unittest


import unittest

class AgentTest_mrr(unittest.TestCase):

    def test_mrr_1(self):
        # Single tuple input: first correct answer at rank 1 gives reciprocal rank 1.0
        value, per_input = MetricsCalculator2.mrr(([1, 0, 1, 0], 4))
        self.assertAlmostEqual(value, 1.0)
        self.assertEqual(len(per_input), 1)
        self.assertAlmostEqual(per_input[0], 1.0)

    def test_mrr_2(self):
        # List of two tuples: reciprocal ranks 1.0 and 0.5, averaged to 0.75
        value, per_input = MetricsCalculator2.mrr(
            [([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)]
        )
        self.assertAlmostEqual(value, 0.75)
        self.assertEqual(len(per_input), 2)
        self.assertAlmostEqual(per_input[0], 1.0)
        self.assertAlmostEqual(per_input[1], 0.5)

    def test_mrr_3(self):
        # Single tuple with first correct answer at rank 3 gives reciprocal rank 1/3
        value, per_input = MetricsCalculator2.mrr(([0, 0, 1, 0], 4))
        self.assertAlmostEqual(value, 1 / 3)
        self.assertEqual(len(per_input), 1)
        self.assertAlmostEqual(per_input[0], 1 / 3)

    def test_mrr_4(self):
        # Three tuples with different ground truth totals:
        # reciprocal ranks 1.0, 1/3 and 0.5; mean is 11/18
        value, per_input = MetricsCalculator2.mrr(
            [([1, 0], 2), ([0, 0, 1], 3), ([0, 1], 5)]
        )
        self.assertAlmostEqual(value, (1.0 + 1 / 3 + 0.5) / 3)
        self.assertEqual(len(per_input), 3)
        self.assertAlmostEqual(per_input[0], 1.0)
        self.assertAlmostEqual(per_input[1], 1 / 3)
        self.assertAlmostEqual(per_input[2], 0.5)

    def test_mrr_5(self):
        # List containing one tuple: first correct answer at rank 2 gives 0.5
        value, per_input = MetricsCalculator2.mrr([([0, 1, 0, 1], 4)])
        self.assertAlmostEqual(value, 0.5)
        self.assertEqual(len(per_input), 1)
        self.assertAlmostEqual(per_input[0], 0.5)

import unittest

class AgentTest_map(unittest.TestCase):

    def test_map_1(self):
        # Single tuple: hits at ranks 1 and 3 give precisions 1/1 and 2/3;
        # their sum divided by 4 ground truth items is 0.41666...
        value, per_input = MetricsCalculator2.map(([1, 0, 1, 0], 4))
        self.assertAlmostEqual(value, 0.41666666666666663)
        self.assertEqual(len(per_input), 1)
        self.assertAlmostEqual(per_input[0], 0.41666666666666663)

    def test_map_2(self):
        # List of two tuples: AP values 0.41666... and 0.25, averaged to 0.3333...
        value, per_input = MetricsCalculator2.map(
            [([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)]
        )
        self.assertAlmostEqual(value, 0.3333333333333333)
        self.assertEqual(len(per_input), 2)
        self.assertAlmostEqual(per_input[0], 0.41666666666666663)
        self.assertAlmostEqual(per_input[1], 0.25)

    def test_map_3(self):
        # Single tuple: hits at ranks 2 and 4 give precisions 1/2 and 2/4;
        # their sum 1.0 divided by 4 ground truth items is 0.25
        value, per_input = MetricsCalculator2.map(([0, 1, 0, 1], 4))
        self.assertAlmostEqual(value, 0.25)
        self.assertEqual(len(per_input), 1)
        self.assertAlmostEqual(per_input[0], 0.25)

    def test_map_4(self):
        # List containing one tuple: the average over one input equals that input's AP
        value, per_input = MetricsCalculator2.map([([1, 0, 1, 0], 4)])
        self.assertAlmostEqual(value, 0.41666666666666663)
        self.assertEqual(len(per_input), 1)
        self.assertAlmostEqual(per_input[0], 0.41666666666666663)

    def test_map_5(self):
        # No correct answers in the result list: average precision is 0
        value, per_input = MetricsCalculator2.map(([0, 0, 0], 3))
        self.assertAlmostEqual(value, 0.0)
        self.assertEqual(len(per_input), 1)
        self.assertAlmostEqual(per_input[0], 0.0)