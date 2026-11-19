import unittest




class MetricsCalculatorTestUpdate(unittest.TestCase):
    def test_update_1(self):
        mc = MetricsCalculator()
        self.assertEqual((mc.true_positives, mc.false_positives, mc.false_negatives, mc.true_negatives), (0, 0, 0, 0))
        mc.update([1, 1, 0, 0], [1, 0, 0, 1])
        self.assertEqual((mc.true_positives, mc.false_positives, mc.false_negatives, mc.true_negatives), (1, 1, 1, 1))

    def test_update_2(self):
        mc = MetricsCalculator()
        self.assertEqual((mc.true_positives, mc.false_positives, mc.false_negatives, mc.true_negatives), (0, 0, 0, 0))
        mc.update([1, 1, 1, 0], [1, 0, 0, 1])
        self.assertEqual((mc.true_positives, mc.false_positives, mc.false_negatives, mc.true_negatives), (1, 2, 1, 0))

    def test_update_3(self):
        mc = MetricsCalculator()
        self.assertEqual((mc.true_positives, mc.false_positives, mc.false_negatives, mc.true_negatives), (0, 0, 0, 0))
        mc.update([1, 1, 0, 1], [1, 0, 0, 1])
        self.assertEqual((mc.true_positives, mc.false_positives, mc.false_negatives, mc.true_negatives), (2, 1, 0, 1))

import unittest

class AgentTest_update(unittest.TestCase):
    def test_update_1(self):
        mc = MetricsCalculator()
        mc.update([0, 0, 0], [0, 0, 0])
        self.assertEqual((mc.true_positives, mc.false_positives, mc.false_negatives, mc.true_negatives), (0, 0, 0, 3))

    def test_update_2(self):
        mc = MetricsCalculator()
        mc.update([1, 0], [1, 0])
        self.assertEqual((mc.true_positives, mc.false_positives, mc.false_negatives, mc.true_negatives), (1, 0, 0, 1))
        mc.update([0, 1], [1, 1])
        self.assertEqual((mc.true_positives, mc.false_positives, mc.false_negatives, mc.true_negatives), (2, 0, 1, 1))

class MetricsCalculatorTestPrecision(unittest.TestCase):
    def test_precision_1(self):
        mc = MetricsCalculator()
        temp = mc.precision([1, 1, 0, 0], [1, 0, 0, 1])
        self.assertEqual(temp, 0.5)

    def test_precision_2(self):
        mc = MetricsCalculator()
        temp = mc.precision([1, 1, 1, 0], [1, 0, 0, 1])
        self.assertAlmostEqual(temp, 0.3333333333333333)

    def test_precision_3(self):
        mc = MetricsCalculator()
        temp = mc.precision([1, 1, 0, 1], [1, 0, 0, 1])
        self.assertAlmostEqual(temp, 0.6666666666666666)

    def test_precision_4(self):
        mc = MetricsCalculator()
        temp = mc.precision([1, 1, 0, 0], [1, 1, 0, 1])
        self.assertAlmostEqual(temp, 1.0)

import unittest

class AgentTest_precision(unittest.TestCase):
    def test_precision_1(self):
        mc = MetricsCalculator()
        temp = mc.precision([1, 0, 1, 1, 0, 1], [1, 1, 0, 1, 0, 1])
        self.assertAlmostEqual(temp, 0.75)

    def test_precision_2(self):
        mc = MetricsCalculator()
        temp = mc.precision([1, 1, 0, 0], [0, 0, 1, 1])
        self.assertAlmostEqual(temp, 0.0)

class MetricsCalculatorTestRecall(unittest.TestCase):
    def test_recall_1(self):
        mc = MetricsCalculator()
        temp = mc.recall([1, 1, 0, 0], [1, 0, 0, 1])
        self.assertEqual(temp, 0.5)

    def test_recall_2(self):
        mc = MetricsCalculator()
        temp = mc.recall([1, 1, 1, 0], [1, 0, 0, 1])
        self.assertEqual(temp, 0.5)

    def test_recall_3(self):
        mc = MetricsCalculator()
        temp = mc.recall([1, 1, 0, 1], [1, 0, 0, 1])
        self.assertEqual(temp, 1.0)

    def test_recall_4(self):
        mc = MetricsCalculator()
        temp = mc.recall([1, 1, 0, 0], [1, 1, 0, 1])
        self.assertAlmostEqual(temp, 0.6666666666666666)

import unittest

class AgentTest_recall(unittest.TestCase):
    def test_recall_1(self):
        mc = MetricsCalculator()
        temp = mc.recall([0, 0, 0, 0], [1, 1, 0, 0])
        self.assertAlmostEqual(temp, 0.0)

    def test_recall_2(self):
        mc = MetricsCalculator()
        temp = mc.recall([1, 1, 1, 0, 0, 0, 1, 0], [1, 0, 1, 1, 0, 0, 1, 1])
        self.assertAlmostEqual(temp, 0.6)

class MetricsCalculatorTestF1Score(unittest.TestCase):
    def test_f1_score_1(self):
        mc = MetricsCalculator()
        temp = mc.f1_score([1, 1, 0, 0], [1, 0, 0, 1])
        self.assertEqual(temp, 0.5)

    def test_f1_score_2(self):
        mc = MetricsCalculator()
        temp = mc.f1_score([1, 1, 1, 0], [1, 0, 0, 1])
        self.assertEqual(temp, 0.4)

    def test_f1_score_3(self):
        mc = MetricsCalculator()
        temp = mc.f1_score([1, 1, 0, 1], [1, 0, 0, 1])
        self.assertEqual(temp, 0.8)

    def test_f1_score_4(self):
        mc = MetricsCalculator()
        temp = mc.f1_score([1, 1, 0, 0], [1, 1, 0, 1])
        self.assertEqual(temp, 0.8)

import unittest

class AgentTest_f1_score(unittest.TestCase):
    def test_f1_score_1(self):
        mc = MetricsCalculator()
        temp = mc.f1_score([1, 1, 1, 0, 0, 0, 1, 0], [1, 0, 1, 1, 0, 0, 1, 1])
        self.assertAlmostEqual(temp, 2 / 3)

    def test_f1_score_2(self):
        mc = MetricsCalculator()
        temp = mc.f1_score([1, 0, 1, 0], [1, 0, 1, 0])
        self.assertAlmostEqual(temp, 1.0)

class MetricsCalculatorTestAccuracy(unittest.TestCase):
    def test_accuracy_1(self):
        mc = MetricsCalculator()
        temp = mc.accuracy([1, 1, 0, 0], [1, 0, 0, 1])
        self.assertEqual(temp, 0.5)

    def test_accuracy_2(self):
        mc = MetricsCalculator()
        temp = mc.accuracy([1, 1, 2, 0], [1, 0, 0, 1])
        self.assertAlmostEqual(temp, 0.3333333333333333)

    def test_accuracy_3(self):
        mc = MetricsCalculator()
        temp = mc.accuracy([1, 1, 0, 1], [1, 0, 0, 1])
        self.assertEqual(temp, 0.75)

    def test_accuracy_4(self):
        mc = MetricsCalculator()
        temp = mc.accuracy([1, 1, 0, 0], [1, 1, 0, 1])
        self.assertEqual(temp, 0.75)

import unittest

class AgentTest_accuracy(unittest.TestCase):
    def test_accuracy_1(self):
        mc = MetricsCalculator()
        temp = mc.accuracy([1, 0, 1, 1], [1, 0, 1, 1])
        self.assertAlmostEqual(temp, 1.0)

    def test_accuracy_2(self):
        mc = MetricsCalculator()
        temp = mc.accuracy([1, 0, 1, 1, 0, 0, 1, 0], [1, 1, 1, 0, 0, 1, 1, 0])
        self.assertAlmostEqual(temp, 0.625)