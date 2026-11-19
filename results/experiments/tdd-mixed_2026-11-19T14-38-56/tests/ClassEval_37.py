import unittest




class EncryptionUtilsTestCaesarCipher(unittest.TestCase):
    def test_caesar_cipher(self):
        encryption_utils = EncryptionUtils("key")
        self.assertEqual(encryption_utils.caesar_cipher("abc", 1), "bcd")

    def test_caesar_cipher_2(self):
        encryption_utils = EncryptionUtils("key")
        self.assertEqual(encryption_utils.caesar_cipher("WORLD", -2), "UMPJB")

    def test_caesar_cipher_3(self):
        encryption_utils = EncryptionUtils("key")
        self.assertEqual(encryption_utils.caesar_cipher("", 4), "")

    def test_caesar_cipher_4(self):
        encryption_utils = EncryptionUtils("key")
        self.assertEqual(encryption_utils.caesar_cipher("abcxyz", 26), "abcxyz")

import unittest

class AgentTest_caesar_cipher(unittest.TestCase):
    def test_caesar_cipher_1(self):
        encryption_utils = EncryptionUtils("key")
        self.assertEqual(encryption_utils.caesar_cipher("xyz", 3), "abc")

    def test_caesar_cipher_2(self):
        encryption_utils = EncryptionUtils("key")
        self.assertEqual(encryption_utils.caesar_cipher("Hello", 3), "Khoor")

class EncryptionUtilsTestVigenereCipher(unittest.TestCase):
    def test_vigenere_cipher(self):
        encryption_utils = EncryptionUtils("key")
        self.assertEqual(encryption_utils.vigenere_cipher("abc"), "kfa")

    def test_vigenere_cipher_2(self):
        encryption_utils = EncryptionUtils("key")
        self.assertEqual(encryption_utils.vigenere_cipher("hello"), "rijvs")

    def test_vigenere_cipher_3(self):
        encryption_utils = EncryptionUtils("longkey")
        self.assertEqual(encryption_utils.vigenere_cipher("AbCdEfG"), "LpPjOjE")

import unittest

class AgentTest_vigenere_cipher(unittest.TestCase):
    def test_vigenere_cipher_1(self):
        encryption_utils = EncryptionUtils("key")
        self.assertEqual(encryption_utils.vigenere_cipher("zzz"), "jdx")

    def test_vigenere_cipher_2(self):
        encryption_utils = EncryptionUtils("a")
        self.assertEqual(encryption_utils.vigenere_cipher("Hello"), "Hello")

class EncryptionUtilsTestRailFenceCipher(unittest.TestCase):
    def test_rail_fence_cipher(self):
        encryption_utils = EncryptionUtils("key")
        self.assertEqual(encryption_utils.rail_fence_cipher("abc", 2), "acb")

    def test_rail_fence_cipher_2(self):
        encryption_utils = EncryptionUtils("key")
        self.assertEqual(encryption_utils.rail_fence_cipher("hello", 2), "hloel")

    def test_rail_fence_cipher_3(self):
        encryption_utils = EncryptionUtils("longkey")
        self.assertEqual(encryption_utils.rail_fence_cipher("AbCdEfG", 2), "ACEGbdf")

    def test_rail_fence_cipher_4(self):
        encryption_utils = EncryptionUtils("key")
        self.assertEqual(encryption_utils.rail_fence_cipher("Hello, World! 123", 2), "Hlo ol!13el,Wrd 2")

import unittest

class AgentTest_rail_fence_cipher(unittest.TestCase):
    def test_rail_fence_cipher_1(self):
        encryption_utils = EncryptionUtils("key")
        self.assertEqual(encryption_utils.rail_fence_cipher("ABCDEFGHIJ", 3), "AEIBDFHJCG")

    def test_rail_fence_cipher_2(self):
        encryption_utils = EncryptionUtils("key")
        self.assertEqual(encryption_utils.rail_fence_cipher("", 2), "")