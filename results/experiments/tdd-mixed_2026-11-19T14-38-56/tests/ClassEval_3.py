import unittest




class ArrangementCalculatorTestSelect(unittest.TestCase):
    def test_select_1(self):
        ac = ArrangementCalculator([1, 2, 3, 4])
        res = ac.select(2)
        expected = [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]]
        self.assertEqual(res, expected)

    def test_select_2(self):
        ac = ArrangementCalculator([1, 2, 3])
        res = ac.select(2)
        expected = [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
        self.assertEqual(res, expected)

    def test_select_3(self):
        ac = ArrangementCalculator([2, 3, 4])
        res = ac.select(2)
        expected = [[2, 3], [2, 4], [3, 2], [3, 4], [4, 2], [4, 3]]
        self.assertEqual(res, expected)

    def test_select_4(self):
        ac = ArrangementCalculator([1, 2])
        res = ac.select(2)
        expected = [[1, 2], [2, 1]]
        self.assertEqual(res, expected)

import unittest

class AgentTest_select(unittest.TestCase):
    def test_select_1(self):
        ac = ArrangementCalculator([1, 2, 3])
        res = ac.select()
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertEqual(res, expected)

    def test_select_2(self):
        ac = ArrangementCalculator([1, 2, 3])
        res = ac.select(1)
        expected = [[1], [2], [3]]
        self.assertEqual(res, expected)

class ArrangementCalculatorTestSelectAll(unittest.TestCase):
    def test_select_all_1(self):
        ac = ArrangementCalculator([1, 2, 3])
        res = ac.select_all()
        expected = [[1], [2], [3], [1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2], [1, 2, 3], [1, 3, 2], [2, 1, 3],
                    [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertEqual(res, expected)

    def test_select_all_2(self):
        ac = ArrangementCalculator([1, 2, 4])
        res = ac.select_all()
        expected = [[1], [2], [4], [1, 2], [1, 4], [2, 1], [2, 4], [4, 1], [4, 2], [1, 2, 4], [1, 4, 2], [2, 1, 4],
                    [2, 4, 1], [4, 1, 2], [4, 2, 1]]
        self.assertEqual(res, expected)

    def test_select_all_3(self):
        ac = ArrangementCalculator([1, 2])
        res = ac.select_all()
        expected = [[1], [2], [1, 2], [2, 1]]
        self.assertEqual(res, expected)

import unittest

class AgentTest_select_all(unittest.TestCase):
    def test_select_all_1(self):
        ac = ArrangementCalculator([7])
        res = ac.select_all()
        expected = [[7]]
        self.assertEqual(res, expected)

    def test_select_all_2(self):
        ac = ArrangementCalculator(['a', 'b'])
        res = ac.select_all()
        expected = [['a'], ['b'], ['a', 'b'], ['b', 'a']]
        self.assertEqual(res, expected)

class ArrangementCalculatorTestFactorial(unittest.TestCase):
    def test_factorial_1(self):
        res = ArrangementCalculator.factorial(4)
        self.assertEqual(res, 24)

    def test_factorial_2(self):
        res = ArrangementCalculator.factorial(5)
        self.assertEqual(res, 120)

    def test_factorial_3(self):
        res = ArrangementCalculator.factorial(3)
        self.assertEqual(res, 6)

import unittest

class AgentTest_factorial(unittest.TestCase):
    def test_factorial_1(self):
        res = ArrangementCalculator.factorial(1)
        self.assertEqual(res, 1)

    def test_factorial_2(self):
        res = ArrangementCalculator.factorial(10)
        self.assertEqual(res, 3628800)

class ArrangementCalculatorTestCount(unittest.TestCase):
    def test_count_1(self):
        res = ArrangementCalculator.count(5, 3)
        self.assertEqual(res, 60)

    def test_count_2(self):
        res = ArrangementCalculator.count(4, 3)
        self.assertEqual(res, 24)

    def test_count_3(self):
        res = ArrangementCalculator.count(6, 3)
        self.assertEqual(res, 120)

import unittest

class AgentTest_count(unittest.TestCase):
    def test_count_1(self):
        res = ArrangementCalculator.count(5)
        self.assertEqual(res, 120)

    def test_count_2(self):
        res = ArrangementCalculator.count(4, 4)
        self.assertEqual(res, 24)

class ArrangementCalculatorTestCountAll(unittest.TestCase):
    def test_count_all_1(self):
        res = ArrangementCalculator.count_all(4)
        self.assertEqual(res, 64)

    def test_count_all_2(self):
        res = ArrangementCalculator.count_all(1)
        self.assertEqual(res, 1)

    def test_count_all_3(self):
        res = ArrangementCalculator.count_all(2)
        self.assertEqual(res, 4)

import unittest

class AgentTest_count_all(unittest.TestCase):
    def test_count_all_1(self):
        res = ArrangementCalculator.count_all(3)
        self.assertEqual(res, 15)

    def test_count_all_2(self):
        res = ArrangementCalculator.count_all(5)
        self.assertEqual(res, 325)