import unittest



class ManacherTestPalindromicLength(unittest.TestCase):
    def test_palindromic_length(self):
        manacher = Manacher('ababa')
        self.assertEqual(manacher.palindromic_length(2, 1, 'a|b|a|b|a'), 2)

    def test_palindromic_length_2(self):
        manacher = Manacher('ababaxse')
        self.assertEqual(manacher.palindromic_length(2, 1, 'a|b|a|b|a|x|s|e'), 2)

    def test_palindromic_length_3(self):
        manacher = Manacher('ababax')
        self.assertEqual(manacher.palindromic_length(2, 3, 'a|b|a|b|a|x'), 0)

import unittest

class AgentTest_palindromic_length(unittest.TestCase):
    def test_palindromic_length_1(self):
        manacher = Manacher('abcba')
        self.assertEqual(manacher.palindromic_length(4, 1, 'a|b|c|b|a'), 4)

    def test_palindromic_length_2(self):
        manacher = Manacher('abcde')
        self.assertEqual(manacher.palindromic_length(4, 1, 'a|b|c|d|e'), 1)

class ManacherTestPalindromicString(unittest.TestCase):
    def test_palindromic_string(self):
        manacher = Manacher('ababaxse')
        self.assertEqual(manacher.palindromic_string(), 'ababa')

    def test_palindromic_string_2(self):
        manacher = Manacher('ababax')
        self.assertEqual(manacher.palindromic_string(), 'ababa')

    def test_palindromic_string_3(self):
        manacher = Manacher('ababax')
        self.assertEqual(manacher.palindromic_string(), 'ababa')

import unittest

class AgentTest_palindromic_string(unittest.TestCase):
    def test_palindromic_string_1(self):
        manacher = Manacher('abcba')
        self.assertEqual(manacher.palindromic_string(), 'abcba')

    def test_palindromic_string_2(self):
        manacher = Manacher('abcdcbxyx')
        self.assertEqual(manacher.palindromic_string(), 'bcdcb')