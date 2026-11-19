import unittest




class BitStatusUtilTestCheck(unittest.TestCase):
    def test_check(self):
        bit_status_util = BitStatusUtil()
        bit_status_util.check([2])

    def test_check_2(self):
        bit_status_util = BitStatusUtil()
        with self.assertRaises(ValueError):
            bit_status_util.check([3])

    def test_check_3(self):
        bit_status_util = BitStatusUtil()
        with self.assertRaises(ValueError):
            bit_status_util.check([-1])

import unittest

class AgentTest_check(unittest.TestCase):
    def test_check_1(self):
        bit_status_util = BitStatusUtil()
        with self.assertRaises(ValueError) as cm:
            bit_status_util.check([2, 3, 4])
        self.assertEqual(str(cm.exception), "3 not even")

    def test_check_2(self):
        bit_status_util = BitStatusUtil()
        self.assertIsNone(bit_status_util.check([0, 2, 4]))

class BitStatusUtilTestAdd(unittest.TestCase):
    def test_add(self):
        bit_status_util = BitStatusUtil()
        self.assertEqual(bit_status_util.add(2, 4), 6)

    def test_add_2(self):
        bit_status_util = BitStatusUtil()
        self.assertEqual(bit_status_util.add(2, 0), 2)

    def test_add_3(self):
        bit_status_util = BitStatusUtil()
        self.assertEqual(bit_status_util.add(0, 0), 0)

import unittest

class AgentTest_add(unittest.TestCase):
    def test_add_1(self):
        bit_status_util = BitStatusUtil()
        self.assertEqual(bit_status_util.add(6, 2), 6)

    def test_add_2(self):
        bit_status_util = BitStatusUtil()
        with self.assertRaises(ValueError):
            bit_status_util.add(2, 3)

class BitStatusUtilTestHas(unittest.TestCase):
    def test_has(self):
        bit_status_util = BitStatusUtil()
        self.assertTrue(bit_status_util.has(6, 2))

    def test_has_2(self):
        bit_status_util = BitStatusUtil()
        self.assertFalse(bit_status_util.has(8, 2))

    def test_has_3(self):
        bit_status_util = BitStatusUtil()
        self.assertTrue(bit_status_util.has(6, 4))

import unittest

class AgentTest_has(unittest.TestCase):
    def test_has_1(self):
        bit_status_util = BitStatusUtil()
        self.assertFalse(bit_status_util.has(4, 6))

    def test_has_2(self):
        bit_status_util = BitStatusUtil()
        self.assertTrue(bit_status_util.has(14, 6))

class BitStatusUtilTestRemove(unittest.TestCase):
    def test_remove(self):
        bit_status_util = BitStatusUtil()
        self.assertEqual(bit_status_util.remove(6, 2), 4)

    def test_remove_2(self):
        bit_status_util = BitStatusUtil()
        self.assertEqual(bit_status_util.remove(8, 2), 8)

    def test_remove_3(self):
        bit_status_util = BitStatusUtil()
        self.assertEqual(bit_status_util.remove(6, 4), 2)

class AgentTest_remove(unittest.TestCase):
    def test_remove_1(self):
        bit_status_util = BitStatusUtil()
        self.assertEqual(bit_status_util.remove(14, 6), 8)

    def test_remove_2(self):
        bit_status_util = BitStatusUtil()
        self.assertEqual(bit_status_util.remove(6, 6), 0)