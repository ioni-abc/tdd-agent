import unittest


import unittest

class AgentTest_check(unittest.TestCase):

    def test_check_1(self):
        self.assertIsNone(BitStatusUtil.check([2, 4, 6]))

    def test_check_2(self):
        with self.assertRaises(ValueError) as cm:
            BitStatusUtil.check([2, 3, 4])
        self.assertEqual(str(cm.exception), "3 not even")

    def test_check_3(self):
        self.assertIsNone(BitStatusUtil.check([0]))

    def test_check_4(self):
        with self.assertRaises(ValueError):
            BitStatusUtil.check([-2])

    def test_check_5(self):
        with self.assertRaises(ValueError):
            BitStatusUtil.check([7])

import unittest

class AgentTest_add(unittest.TestCase):

    def test_add_1(self):
        self.assertEqual(BitStatusUtil.add(2, 4), 6)

    def test_add_2(self):
        self.assertEqual(BitStatusUtil.add(0, 2), 2)

    def test_add_3(self):
        self.assertEqual(BitStatusUtil.add(6, 4), 6)

    def test_add_4(self):
        self.assertEqual(BitStatusUtil.add(8, 2), 10)

    def test_add_5(self):
        self.assertEqual(BitStatusUtil.add(0, 0), 0)

import unittest

class AgentTest_has(unittest.TestCase):

    def test_has_1(self):
        self.assertIs(BitStatusUtil.has(6, 2), True)

    def test_has_2(self):
        self.assertIs(BitStatusUtil.has(6, 4), True)

    def test_has_3(self):
        self.assertIs(BitStatusUtil.has(6, 8), False)

    def test_has_4(self):
        self.assertIs(BitStatusUtil.has(2, 6), False)

    def test_has_5(self):
        self.assertIs(BitStatusUtil.has(0, 2), False)

import unittest

class AgentTest_remove(unittest.TestCase):

    def test_remove_1(self):
        self.assertEqual(BitStatusUtil.remove(6, 2), 4)

    def test_remove_2(self):
        self.assertEqual(BitStatusUtil.remove(6, 4), 2)

    def test_remove_3(self):
        self.assertEqual(BitStatusUtil.remove(2, 2), 0)

    def test_remove_4(self):
        self.assertEqual(BitStatusUtil.remove(6, 6), 0)

    def test_remove_5(self):
        self.assertEqual(BitStatusUtil.remove(10, 2), 8)