import unittest


import unittest

class AgentTest_caesar_cipher(unittest.TestCase):

    def setUp(self):
        self.e = EncryptionUtils("key")

    def test_caesar_cipher_1(self):
        # Example from the docstring
        self.assertEqual(self.e.caesar_cipher("abc", 1), 'bcd')

    def test_caesar_cipher_2(self):
        # Each character is shifted by the given number of positions
        self.assertEqual(self.e.caesar_cipher("hello", 3), 'khoor')

    def test_caesar_cipher_3(self):
        # A shift of zero leaves the plaintext unchanged
        self.assertEqual(self.e.caesar_cipher("hello", 0), 'hello')

    def test_caesar_cipher_4(self):
        # An empty plaintext gives an empty ciphertext
        self.assertEqual(self.e.caesar_cipher("", 5), '')

    def test_caesar_cipher_5(self):
        # The ciphertext is returned as a str
        result = self.e.caesar_cipher("abc", 2)
        self.assertIsInstance(result, str)
        self.assertEqual(result, 'cde')

import unittest

class AgentTest_vigenere_cipher(unittest.TestCase):

    def setUp(self):
        self.e = EncryptionUtils("key")

    def test_vigenere_cipher_1(self):
        # Example from the docstring
        self.assertEqual(self.e.vigenere_cipher("abc"), 'kfa')

    def test_vigenere_cipher_2(self):
        # An empty plaintext gives an empty ciphertext
        self.assertEqual(self.e.vigenere_cipher(""), '')

    def test_vigenere_cipher_3(self):
        # The key repeats when the plaintext is longer than the key
        self.assertEqual(self.e.vigenere_cipher("abcd"), 'kfan')

    def test_vigenere_cipher_4(self):
        # The ciphertext is returned as a str
        result = self.e.vigenere_cipher("abc")
        self.assertIsInstance(result, str)
        self.assertEqual(result, 'kfa')

    def test_vigenere_cipher_5(self):
        # The encryption uses the key given at initialisation and wraps past 'z'
        e = EncryptionUtils("b")
        self.assertEqual(e.vigenere_cipher("xyz"), 'yza')

import unittest

class AgentTest_rail_fence_cipher(unittest.TestCase):

    def setUp(self):
        self.e = EncryptionUtils("key")

    def test_rail_fence_cipher_1(self):
        # Example from the docstring
        self.assertEqual(self.e.rail_fence_cipher("abc", 2), 'acb')

    def test_rail_fence_cipher_2(self):
        # The ciphertext is returned as a str
        result = self.e.rail_fence_cipher("abc", 2)
        self.assertIsInstance(result, str)
        self.assertEqual(result, 'acb')

    def test_rail_fence_cipher_3(self):
        # An empty plaintext gives an empty ciphertext
        self.assertEqual(self.e.rail_fence_cipher("", 2), '')

    def test_rail_fence_cipher_4(self):
        # The ciphertext is a rearrangement of the plaintext characters,
        # so it has the same length and the same characters
        plaintext = "rail fence"
        result = self.e.rail_fence_cipher(plaintext, 3)
        self.assertEqual(len(result), len(plaintext))
        self.assertEqual(sorted(result), sorted(plaintext))

    def test_rail_fence_cipher_5(self):
        # With three rails, characters are written in a zigzag across the rails
        # and then read rail by rail: rail 0 = a,e; rail 1 = b,d,f; rail 2 = c
        self.assertEqual(self.e.rail_fence_cipher("abcdef", 3), 'aebdfc')