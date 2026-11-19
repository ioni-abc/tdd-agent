import unittest


import unittest

class AgentTest_update(unittest.TestCase):

    def test_update_1(self):
        mc = MetricsCalculator()
        mc.update([1, 1, 0, 0], [1, 0, 0, 1])
        self.assertEqual(mc.true_positives, 1)
        self.assertEqual(mc.false_positives, 1)
        self.assertEqual(mc.false_negatives, 1)
        self.assertEqual(mc.true_negatives, 1)

    def test_update_2(self):
        mc = MetricsCalculator()
        mc.update([1, 1, 1], [1, 1, 1])
        self.assertEqual(mc.true_positives, 3)
        self.assertEqual(mc.false_positives, 0)
        self.assertEqual(mc.false_negatives, 0)
        self.assertEqual(mc.true_negatives, 0)

    def test_update_3(self):
        mc = MetricsCalculator()
        mc.update([0, 0], [0, 0])
        self.assertEqual(mc.true_positives, 0)
        self.assertEqual(mc.false_positives, 0)
        self.assertEqual(mc.false_negatives, 0)
        self.assertEqual(mc.true_negatives, 2)

    def test_update_4(self):
        mc = MetricsCalculator()
        mc.update([1, 0, 1, 0, 0, 1], [1, 1, 0, 0, 0, 0])
        self.assertEqual(mc.true_positives, 1)
        self.assertEqual(mc.false_positives, 2)
        self.assertEqual(mc.false_negatives, 1)
        self.assertEqual(mc.true_negatives, 2)

    def test_update_5(self):
        mc = MetricsCalculator()
        mc.update([1, 1, 0, 0], [1, 0, 0, 1])
        mc.update([1, 1, 0, 0], [1, 0, 0, 1])
        self.assertEqual(mc.true_positives, 2)
        self.assertEqual(mc.false_positives, 2)
        self.assertEqual(mc.false_negatives, 2)
        self.assertEqual(mc.true_negatives, 2)

import unittest

class AgentTest_precision(unittest.TestCase):

    def test_precision_1(self):
        mc = MetricsCalculator()
        self.assertEqual(mc.precision([1, 1, 0, 0], [1, 0, 0, 1]), 0.5)

    def test_precision_2(self):
        mc = MetricsCalculator()
        self.assertEqual(mc.precision([1, 1, 1], [1, 1, 1]), 1.0)

    def test_precision_3(self):
        mc = MetricsCalculator()
        self.assertEqual(mc.precision([1, 1], [0, 0]), 0.0)

    def test_precision_4(self):
        mc = MetricsCalculator()
        self.assertAlmostEqual(mc.precision([1, 0, 1, 0, 0, 1], [1, 1, 0, 0, 0, 0]), 1 / 3)

    def test_precision_5(self):
        mc = MetricsCalculator()
        self.assertAlmostEqual(mc.precision([1, 1, 1, 0, 0, 0], [1, 1, 0, 0, 0, 1]), 2 / 3)

import unittest

class AgentTest_recall(unittest.TestCase):

    def test_recall_1(self):
        mc = MetricsCalculator()
        self.assertEqual(mc.recall([1, 1, 0, 0], [1, 0, 0, 1]), 0.5)

    def test_recall_2(self):
        mc = MetricsCalculator()
        self.assertEqual(mc.recall([1, 1, 1], [1, 1, 1]), 1.0)

    def test_recall_3(self):
        mc = MetricsCalculator()
        self.assertAlmostEqual(mc.recall([0, 0, 1], [1, 1, 1]), 1 / 3)

    def test_recall_4(self):
        mc = MetricsCalculator()
        self.assertAlmostEqual(mc.recall([1, 1, 1, 0, 0, 0], [1, 1, 0, 0, 0, 1]), 2 / 3)

    def test_recall_5(self):
        mc = MetricsCalculator()
        self.assertAlmostEqual(mc.recall([1, 1, 1, 1, 0, 0, 0], [1, 1, 0, 0, 1, 1, 0]), 0.5)

import unittest

class AgentTest_f1_score(unittest.TestCase):

    def test_f1_score_1(self):
        mc = MetricsCalculator()
        self.assertAlmostEqual(mc.f1_score([1, 1, 0, 0], [1, 0, 0, 1]), 0.5)

    def test_f1_score_2(self):
        mc = MetricsCalculator()
        self.assertAlmostEqual(mc.f1_score([1, 1, 1], [1, 1, 1]), 1.0)

    def test_f1_score_3(self):
        mc = MetricsCalculator()
        self.assertAlmostEqual(mc.f1_score([0, 0, 1], [1, 1, 1]), 0.5)

    def test_f1_score_4(self):
        mc = MetricsCalculator()
        self.assertAlmostEqual(mc.f1_score([1, 0, 1, 0, 0, 1], [1, 1, 0, 0, 0, 0]), 2 / 5)

    def test_f1_score_5(self):
        mc = MetricsCalculator()
        self.assertAlmostEqual(mc.f1_score([1, 1, 1, 0, 0, 0], [1, 1, 0, 0, 0, 1]), 2 / 3)

import unittest

class AgentTest_accuracy(unittest.TestCase):

    def test_accuracy_1(self):
        mc = MetricsCalculator()
        self.assertAlmostEqual(mc.accuracy([1, 1, 0, 0], [1, 0, 0, 1]), 0.5)

    def test_accuracy_2(self):
        mc = MetricsCalculator()
        self.assertAlmostEqual(mc.accuracy([1, 1, 1], [1, 1, 1]), 1.0)

    def test_accuracy_3(self):
        mc = MetricsCalculator()
        self.assertAlmostEqual(mc.accuracy([1, 1], [0, 0]), 0.0)

    def test_accuracy_4(self):
        mc = MetricsCalculator()
        self.assertAlmostEqual(mc.accuracy([1, 1, 1, 0, 0, 0], [1, 1, 0, 0, 0, 1]), 2 / 3)

    def test_accuracy_5(self):
        mc = MetricsCalculator()
        self.assertAlmostEqual(mc.accuracy([0, 0, 0, 1, 1], [0, 1, 0, 1, 0]), 3 / 5)