import unittest


import unittest

import math

class AgentTest_count(unittest.TestCase):

    def test_count_1(self):
        self.assertEqual(CombinationCalculator.count(4, 2), 6)

    def test_count_2(self):
        self.assertEqual(CombinationCalculator.count(5, 2), 10)

    def test_count_3(self):
        self.assertEqual(CombinationCalculator.count(4, 4), 1)

    def test_count_4(self):
        self.assertEqual(CombinationCalculator.count(10, 3), 120)

    def test_count_5(self):
        result = CombinationCalculator.count(6, 3)
        self.assertIsInstance(result, int)
        self.assertEqual(result, 20)

import unittest

import unittest

import math

class AgentTest_count_all(unittest.TestCase):

    def test_count_all_1(self):
        self.assertEqual(CombinationCalculator.count_all(4), 15)

    def test_count_all_2(self):
        self.assertEqual(CombinationCalculator.count_all(1), 1)

    def test_count_all_3(self):
        result = CombinationCalculator.count_all(10)
        self.assertIsInstance(result, int)
        self.assertEqual(result, 1023)

    def test_count_all_4(self):
        # 2^63 - 1 is not greater than 2^63 - 1, so the exact integer is returned
        result = CombinationCalculator.count_all(63)
        self.assertIsInstance(result, int)
        self.assertEqual(result, 2 ** 63 - 1)

    def test_count_all_5(self):
        # Number of combinations exceeds 2^63 - 1, so float("inf") is returned
        self.assertEqual(CombinationCalculator.count_all(64), float("inf"))

import unittest

import math

class AgentTest_select(unittest.TestCase):

    def test_select_1(self):
        calc = CombinationCalculator(["A", "B", "C", "D"])
        self.assertEqual(
            calc.select(2),
            [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']]
        )

    def test_select_2(self):
        calc = CombinationCalculator(["A", "B", "C", "D"])
        self.assertEqual(calc.select(1), [['A'], ['B'], ['C'], ['D']])

    def test_select_3(self):
        calc = CombinationCalculator(["A", "B", "C", "D"])
        self.assertEqual(calc.select(4), [['A', 'B', 'C', 'D']])

    def test_select_4(self):
        datas = ["A", "B", "C", "D", "E"]
        calc = CombinationCalculator(datas)
        result = calc.select(3)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), math.comb(5, 3))
        for combination in result:
            self.assertIsInstance(combination, list)
            self.assertEqual(len(combination), 3)
            self.assertEqual(len(set(combination)), 3)
            for element in combination:
                self.assertIn(element, datas)

    def test_select_5(self):
        calc = CombinationCalculator(["A", "B", "C", "D", "E"])
        self.assertEqual(
            calc.select(3),
            [
                ['A', 'B', 'C'], ['A', 'B', 'D'], ['A', 'B', 'E'],
                ['A', 'C', 'D'], ['A', 'C', 'E'], ['A', 'D', 'E'],
                ['B', 'C', 'D'], ['B', 'C', 'E'], ['B', 'D', 'E'],
                ['C', 'D', 'E']
            ]
        )

import unittest

import math

class AgentTest_select_all(unittest.TestCase):

    def test_select_all_1(self):
        calc = CombinationCalculator(["A", "B", "C", "D"])
        self.assertEqual(
            calc.select_all(),
            [['A'], ['B'], ['C'], ['D'],
             ['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D'],
             ['A', 'B', 'C'], ['A', 'B', 'D'], ['A', 'C', 'D'], ['B', 'C', 'D'],
             ['A', 'B', 'C', 'D']]
        )

    def test_select_all_2(self):
        calc = CombinationCalculator(["X"])
        self.assertEqual(calc.select_all(), [['X']])

    def test_select_all_3(self):
        calc = CombinationCalculator(["A", "B"])
        self.assertEqual(
            calc.select_all(),
            [['A'], ['B'], ['A', 'B']]
        )

    def test_select_all_4(self):
        datas = ["A", "B", "C", "D", "E"]
        calc = CombinationCalculator(datas)
        result = calc.select_all()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2 ** 5 - 1)
        for combination in result:
            self.assertIsInstance(combination, list)
            self.assertGreaterEqual(len(combination), 1)
            self.assertLessEqual(len(combination), 5)
            self.assertEqual(len(set(combination)), len(combination))
            for element in combination:
                self.assertIn(element, datas)

    def test_select_all_5(self):
        datas = ["A", "B", "C", "D", "E"]
        calc = CombinationCalculator(datas)
        expected = []
        for m in range(1, len(datas) + 1):
            expected.extend(calc.select(m))
        self.assertEqual(calc.select_all(), expected)

import unittest

import math

class AgentTest__select(unittest.TestCase):

    def test__select_1(self):
        # Docstring example: generates all 2-element combinations from index 0
        calc = CombinationCalculator(["A", "B", "C", "D"])
        result = []
        calc._select(0, [None] * 2, 0, result)
        self.assertEqual(
            result,
            [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']]
        )

    def test__select_2(self):
        # Returns None and appends to the same list object that was passed in
        calc = CombinationCalculator(["A", "B", "C", "D"])
        result = []
        returned = calc._select(0, [None] * 2, 0, result)
        self.assertIsNone(returned)
        self.assertEqual(len(result), math.comb(4, 2))
        for combination in result:
            self.assertIsInstance(combination, list)
            self.assertEqual(len(combination), 2)

    def test__select_3(self):
        # Selecting from dataIndex 2 only uses the data from that index onward
        calc = CombinationCalculator(["A", "B", "C", "D"])
        result = []
        calc._select(2, [None] * 2, 0, result)
        self.assertEqual(result, [['C', 'D']])

    def test__select_4(self):
        # Selecting one element per combination yields each data item as its own combination
        calc = CombinationCalculator(["A", "B", "C"])
        result = []
        calc._select(0, [None] * 1, 0, result)
        self.assertEqual(result, [['A'], ['B'], ['C']])

    def test__select_5(self):
        # Combination size equal to the number of data items yields exactly one combination
        calc = CombinationCalculator(["A", "B", "C", "D"])
        result = []
        calc._select(0, [None] * 4, 0, result)
        self.assertEqual(result, [['A', 'B', 'C', 'D']])