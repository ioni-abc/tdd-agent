import unittest



class CombinationCalculatorTestCount(unittest.TestCase):
    def test_count(self):
        self.assertEqual(CombinationCalculator.count(4, 2), 6)

    def test_count_2(self):
        self.assertEqual(CombinationCalculator.count(5, 3), 10)

    def test_count_3(self):
        self.assertEqual(CombinationCalculator.count(6, 6), 1)

import unittest

class AgentTest_count(unittest.TestCase):
    def test_count_1(self):
        self.assertEqual(CombinationCalculator.count(10, 5), 252)

    def test_count_2(self):
        self.assertEqual(CombinationCalculator.count(52, 5), 2598960)

class CombinationCalculatorTestCountAll(unittest.TestCase):
    def test_count_all(self):
        self.assertEqual(CombinationCalculator.count_all(4), 15)

    def test_count_all_2(self):
        self.assertEqual(CombinationCalculator.count_all(-1), False)

    def test_count_all_3(self):
        self.assertEqual(CombinationCalculator.count_all(65), False)

import unittest

class AgentTest_count_all(unittest.TestCase):
    def test_count_all_1(self):
        self.assertEqual(CombinationCalculator.count_all(63), 2 ** 63 - 1)

    def test_count_all_2(self):
        self.assertEqual(CombinationCalculator.count_all(64), float("inf"))

class CombinationCalculatorTestSelect(unittest.TestCase):
    def test_select(self):
        calc = CombinationCalculator(["A", "B", "C", "D"])
        self.assertEqual(calc.count(4, 2), 6)

    def test_select_2(self):
        calc = CombinationCalculator(["A", "B", "C", "D"])
        self.assertEqual(calc.count(5, 3), 10)

    def test_select_3(self):
        calc = CombinationCalculator(["A", "B", "C", "D"])
        self.assertEqual(calc.count(6, 6), 1)

import unittest

class AgentTest_select(unittest.TestCase):
    def test_select_1(self):
        calc = CombinationCalculator(["A", "B", "C", "D"])
        self.assertEqual(
            calc.select(3),
            [['A', 'B', 'C'], ['A', 'B', 'D'], ['A', 'C', 'D'], ['B', 'C', 'D']]
        )

    def test_select_2(self):
        calc = CombinationCalculator(["A", "B", "C", "D"])
        self.assertEqual(calc.select(1), [['A'], ['B'], ['C'], ['D']])

class CombinationCalculatorTestSelectAll(unittest.TestCase):
    def test_select_all(self):
        calc = CombinationCalculator(["A"])
        self.assertEqual(calc.select_all(), [['A']])

    def test_select_all_2(self):
        calc = CombinationCalculator(["A", "B"])
        self.assertEqual(calc.select_all(), [['A'], ['B'], ['A', 'B']])

    def test_select_all_3(self):
        calc = CombinationCalculator(["A", "B", "C"])
        self.assertEqual(calc.select_all(),[['A'], ['B'], ['C'], ['A', 'B'], ['A', 'C'], ['B', 'C'], ['A', 'B', 'C']])

import unittest

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
        data = ["A", "B", "C", "D", "E"]
        calc = CombinationCalculator(data)
        result = calc.select_all()
        self.assertEqual(len(result), CombinationCalculator.count_all(len(data)))
        self.assertEqual(len(result), 31)
        self.assertEqual(result[0], ['A'])
        self.assertEqual(result[-1], data)

class CombinationCalculatorTestSelect2(unittest.TestCase):
    def test_select2(self):
        calc = CombinationCalculator(["A", "B", "C", "D"])
        result = []
        calc._select(0, [None] * 2, 0, result)
        self.assertEqual(result, [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']])

    def test_select2_2(self):
        calc = CombinationCalculator(["A", "B", "C", "D"])
        result = []
        calc._select(0, [None] * 3, 0, result)
        self.assertEqual(result, [['A', 'B', 'C'], ['A', 'B', 'D'], ['A', 'C', 'D'], ['B', 'C', 'D']])

    def test_select2_3(self):
        calc = CombinationCalculator(["A", "B", "C", "D"])
        result = []
        calc._select(0, [None] * 1, 0, result)
        self.assertEqual(result, [['A'], ['B'], ['C'], ['D']])

import unittest

class AgentTest__select(unittest.TestCase):
    def test__select_1(self):
        calc = CombinationCalculator(["A", "B", "C", "D"])
        result = []
        calc._select(1, [None] * 2, 0, result)
        self.assertEqual(result, [['B', 'C'], ['B', 'D'], ['C', 'D']])

    def test__select_2(self):
        calc = CombinationCalculator(["A", "B", "C", "D"])
        result = []
        calc._select(0, ['X', None], 1, result)
        self.assertEqual(result, [['X', 'A'], ['X', 'B'], ['X', 'C'], ['X', 'D']])