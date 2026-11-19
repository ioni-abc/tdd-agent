import unittest


import unittest

import itertools

class AgentTest_select(unittest.TestCase):

    def test_select_1(self):
        ac = ArrangementCalculator([1, 2, 3, 4])
        self.assertEqual(
            ac.select(2),
            [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4],
             [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]]
        )

    def test_select_2(self):
        ac = ArrangementCalculator([1, 2, 3])
        result = ac.select()
        expected = [list(p) for p in itertools.permutations([1, 2, 3])]
        self.assertEqual(len(result), 6)
        self.assertEqual(sorted(result), sorted(expected))

    def test_select_3(self):
        ac = ArrangementCalculator([1, 2, 3])
        self.assertEqual(sorted(ac.select(1)), [[1], [2], [3]])

    def test_select_4(self):
        ac = ArrangementCalculator([1, 2, 3])
        self.assertEqual(sorted(ac.select(3)), sorted(ac.select()))

    def test_select_5(self):
        datas = ['a', 'b', 'c', 'd', 'e']
        ac = ArrangementCalculator(datas)
        result = ac.select(3)
        self.assertEqual(len(result), ArrangementCalculator.count(5, 3))
        for arrangement in result:
            self.assertEqual(len(arrangement), 3)
            self.assertEqual(len(set(arrangement)), 3)
            for item in arrangement:
                self.assertIn(item, datas)
        self.assertEqual(len(set(tuple(a) for a in result)), len(result))

class AgentTest_select_all(unittest.TestCase):

    def test_select_all_1(self):
        ac = ArrangementCalculator([1, 2, 3])
        self.assertEqual(
            ac.select_all(),
            [[1], [2], [3], [1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2],
             [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        )

    def test_select_all_2(self):
        ac = ArrangementCalculator([1, 2, 3, 4])
        result = ac.select_all()
        self.assertEqual(len(result), 64)
        self.assertEqual(len(result), ArrangementCalculator.count_all(4))

    def test_select_all_3(self):
        datas = [1, 2, 3, 4]
        ac = ArrangementCalculator(datas)
        expected = []
        for r in range(1, len(datas) + 1):
            expected.extend([list(p) for p in itertools.permutations(datas, r)])
        result = ac.select_all()
        self.assertEqual(sorted(result), sorted(expected))

    def test_select_all_4(self):
        ac = ArrangementCalculator(['a'])
        self.assertEqual(ac.select_all(), [['a']])

    def test_select_all_5(self):
        datas = ['a', 'b', 'c', 'd']
        ac = ArrangementCalculator(datas)
        result = ac.select_all()
        for arrangement in result:
            self.assertGreaterEqual(len(arrangement), 1)
            self.assertLessEqual(len(arrangement), len(datas))
            self.assertEqual(len(set(arrangement)), len(arrangement))
            for item in arrangement:
                self.assertIn(item, datas)
        self.assertEqual(len(set(tuple(a) for a in result)), len(result))

import unittest

import math

class AgentTest_factorial(unittest.TestCase):

    def test_factorial_1(self):
        self.assertEqual(ArrangementCalculator.factorial(4), 24)

    def test_factorial_2(self):
        self.assertEqual(ArrangementCalculator.factorial(0), 1)
        self.assertEqual(ArrangementCalculator.factorial(1), 1)

    def test_factorial_3(self):
        self.assertEqual(ArrangementCalculator.factorial(3), 6)
        self.assertEqual(ArrangementCalculator.factorial(5), 120)

    def test_factorial_4(self):
        for n in range(0, 11):
            with self.subTest(n=n):
                self.assertEqual(ArrangementCalculator.factorial(n), math.factorial(n))

    def test_factorial_5(self):
        for n in range(1, 7):
            with self.subTest(n=n):
                self.assertEqual(ArrangementCalculator.count(n), ArrangementCalculator.factorial(n))
                self.assertIsInstance(ArrangementCalculator.factorial(n), int)

import math

import itertools

class AgentTest_count(unittest.TestCase):

    def test_count_1(self):
        self.assertEqual(ArrangementCalculator.count(5, 3), 60)

    def test_count_2(self):
        self.assertEqual(ArrangementCalculator.count(4), 24)
        self.assertEqual(ArrangementCalculator.count(4), ArrangementCalculator.factorial(4))

    def test_count_3(self):
        for n in range(1, 9):
            with self.subTest(n=n):
                self.assertEqual(ArrangementCalculator.count(n), math.factorial(n))
                self.assertEqual(ArrangementCalculator.count(n, n), math.factorial(n))

    def test_count_4(self):
        cases = [(6, 2, 30), (10, 4, 5040), (4, 1, 4), (7, 3, 210), (8, 5, 6720)]
        for n, m, expected in cases:
            with self.subTest(n=n, m=m):
                self.assertEqual(ArrangementCalculator.count(n, m), expected)

    def test_count_5(self):
        for n in range(1, 7):
            for m in range(1, n + 1):
                with self.subTest(n=n, m=m):
                    expected = len(list(itertools.permutations(range(n), m)))
                    self.assertEqual(ArrangementCalculator.count(n, m), expected)

import unittest

import itertools

import math

class AgentTest_count_all(unittest.TestCase):

    def test_count_all_1(self):
        self.assertEqual(ArrangementCalculator.count_all(4), 64)

    def test_count_all_2(self):
        self.assertEqual(ArrangementCalculator.count_all(1), 1)
        self.assertEqual(ArrangementCalculator.count_all(2), 4)
        self.assertEqual(ArrangementCalculator.count_all(3), 15)

    def test_count_all_3(self):
        for n in range(1, 7):
            with self.subTest(n=n):
                expected = sum(
                    len(list(itertools.permutations(range(n), r)))
                    for r in range(1, n + 1)
                )
                self.assertEqual(ArrangementCalculator.count_all(n), expected)

    def test_count_all_4(self):
        for n in range(1, 8):
            with self.subTest(n=n):
                expected = sum(ArrangementCalculator.count(n, r) for r in range(1, n + 1))
                self.assertEqual(ArrangementCalculator.count_all(n), expected)

    def test_count_all_5(self):
        result = ArrangementCalculator.count_all(5)
        self.assertEqual(result, 325)
        self.assertIsInstance(result, int)
        self.assertGreater(
            ArrangementCalculator.count_all(5),
            ArrangementCalculator.count_all(4)
        )