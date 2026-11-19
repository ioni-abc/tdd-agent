import unittest


import unittest

class AgentTest_caesar_decipher(unittest.TestCase):

    def setUp(self):
        self.d = DecryptionUtils('key')

    def test_caesar_decipher_1(self):
        self.assertEqual(self.d.caesar_decipher('ifmmp', 1), 'hello')

    def test_caesar_decipher_2(self):
        self.assertEqual(self.d.caesar_decipher('abc', 0), 'abc')

    def test_caesar_decipher_3(self):
        self.assertEqual(self.d.caesar_decipher('a', 1), 'z')

    def test_caesar_decipher_4(self):
        self.assertEqual(self.d.caesar_decipher('khoor', 3), 'hello')

    def test_caesar_decipher_5(self):
        self.assertEqual(self.d.caesar_decipher('xyz', 3), 'uvw')

import unittest

class AgentTest_vigenere_decipher(unittest.TestCase):

    def setUp(self):
        self.d = DecryptionUtils('key')

    def test_vigenere_decipher_1(self):
        self.assertEqual(self.d.vigenere_decipher('ifmmp'), 'ybocl')

    def test_vigenere_decipher_2(self):
        d = DecryptionUtils('a')
        self.assertEqual(d.vigenere_decipher('abc'), 'abc')

    def test_vigenere_decipher_3(self):
        d = DecryptionUtils('b')
        self.assertEqual(d.vigenere_decipher('bcd'), 'abc')

    def test_vigenere_decipher_4(self):
        d = DecryptionUtils('abc')
        self.assertEqual(d.vigenere_decipher('bcd'), 'bbb')

    def test_vigenere_decipher_5(self):
        self.assertEqual(self.d.vigenere_decipher('rijvs'), 'hello')

import unittest

class AgentTest_rail_fence_decipher(unittest.TestCase):

    def setUp(self):
        self.d = DecryptionUtils('key')

    def test_rail_fence_decipher_1(self):
        self.assertEqual(self.d.rail_fence_decipher('Hoo!el,Wrdl l', 3), 'Hello, World!')

    def test_rail_fence_decipher_2(self):
        self.assertEqual(self.d.rail_fence_decipher('Hloel', 2), 'Hello')

    def test_rail_fence_decipher_3(self):
        self.assertEqual(self.d.rail_fence_decipher('aebdfc', 3), 'abcdef')

    def test_rail_fence_decipher_4(self):
        self.assertEqual(self.d.rail_fence_decipher('abcd', 4), 'abcd')

    def test_rail_fence_decipher_5(self):
        self.assertEqual(self.d.rail_fence_decipher('', 3), '')