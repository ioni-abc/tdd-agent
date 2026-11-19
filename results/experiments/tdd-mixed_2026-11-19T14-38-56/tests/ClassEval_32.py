import unittest




class DecryptionUtilsTestCaesarDecipher(unittest.TestCase):
    def test_caesar_decipher(self):
        d = DecryptionUtils('key')
        self.assertEqual(d.caesar_decipher('ifmmp', 1), 'hello')

    def test_caesar_decipher_2(self):
        d = DecryptionUtils('key')
        self.assertEqual(d.caesar_decipher('bcdyza', 27), 'abcxyz')

    def test_caesar_decipher_3(self):
        d = DecryptionUtils('key')
        self.assertEqual(d.caesar_decipher('bcd', 0), 'bcd')

    def test_caesar_decipher_4(self):
        d = DecryptionUtils('key')
        self.assertEqual(d.caesar_decipher('bcd', 26), 'bcd')

    def test_caesar_decipher_5(self):
        d = DecryptionUtils('key')
        self.assertEqual(d.caesar_decipher('bcd', -26), 'bcd')

import unittest

class AgentTest_caesar_decipher(unittest.TestCase):
    def test_caesar_decipher_1(self):
        d = DecryptionUtils('key')
        self.assertEqual(d.caesar_decipher('ifmmp', -1), 'jgnnq')

    def test_caesar_decipher_2(self):
        d = DecryptionUtils('key')
        self.assertEqual(d.caesar_decipher('abc', 29), 'xyz')

class DecryptionUtilsTestVigenereDecipher(unittest.TestCase):
    def test_vigenere_decipher(self):
        d = DecryptionUtils('key')
        self.assertEqual(d.vigenere_decipher('ifmmp'), 'ybocl')

    def test_vigenere_decipher_2(self):
        d = DecryptionUtils('key')
        self.assertEqual(d.vigenere_decipher('rijvs'), 'hello')

    def test_vigenere_decipher_3(self):
        d = DecryptionUtils('longkey')
        self.assertEqual(d.vigenere_decipher('LpPjOjE'), 'AbCdEfG')

    def test_vigenere_decipher_4(self):
        d = DecryptionUtils('key')
        self.assertEqual(d.vigenere_decipher('bcd'), 'ryf')

import unittest

class AgentTest_vigenere_decipher(unittest.TestCase):
    def test_vigenere_decipher_1(self):
        d = DecryptionUtils('key')
        self.assertEqual(d.vigenere_decipher(''), '')

    def test_vigenere_decipher_2(self):
        d = DecryptionUtils('key')
        self.assertEqual(d.vigenere_decipher('IFMMP'), 'YBOCL')

class DecryptionUtilsTestRailFenceDecipher(unittest.TestCase):
    def test_rail_fence_decipher(self):
        d = DecryptionUtils('key')
        self.assertEqual(d.rail_fence_decipher('Hoo!el,Wrdl l', 3), 'Hello, World!')

    def test_rail_fence_decipher_2(self):
        d = DecryptionUtils('key')
        self.assertEqual(d.rail_fence_decipher('Hoo!el,Wrdl l', 4), 'H!W reoldll,o')

    def test_rail_fence_decipher_3(self):
        d = DecryptionUtils('key')
        self.assertEqual(d.rail_fence_decipher('Hoo!el,Wrdl l', 5), 'Holr d,!oeWll')

import unittest

class AgentTest_rail_fence_decipher(unittest.TestCase):
    def test_rail_fence_decipher_1(self):
        d = DecryptionUtils('key')
        self.assertEqual(d.rail_fence_decipher('Hlo ol!el,Wrd', 2), 'Hello, World!')

    def test_rail_fence_decipher_2(self):
        d = DecryptionUtils('key')
        self.assertEqual(d.rail_fence_decipher('AEIBDFHJCG', 3), 'ABCDEFGHIJ')