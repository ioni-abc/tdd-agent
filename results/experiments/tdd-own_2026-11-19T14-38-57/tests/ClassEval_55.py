import unittest


import unittest

class AgentTest_palindromic_length(unittest.TestCase):

    def test_palindromic_length_1(self):
        manacher = Manacher('ababa')
        self.assertEqual(manacher.palindromic_length(2, 1, 'a|b|a|b|a'), 2)

    def test_palindromic_length_2(self):
        manacher = Manacher('abc')
        self.assertEqual(manacher.palindromic_length(2, 1, 'a|b|c'), 1)

    def test_palindromic_length_3(self):
        manacher = Manacher('ababa')
        self.assertEqual(manacher.palindromic_length(4, 1, 'a|b|a|b|a'), 4)

    def test_palindromic_length_4(self):
        manacher = Manacher('a-b')
        self.assertEqual(manacher.palindromic_length(1, 1, 'a-b'), 0)

    def test_palindromic_length_5(self):
        manacher = Manacher('xababay')
        self.assertEqual(manacher.palindromic_length(4, 1, 'x|a|b|a|y'), 3)

class AgentTest_palindromic_string(unittest.TestCase):

    def test_palindromic_string_1(self):
        manacher = Manacher('ababaxse')
        self.assertEqual(manacher.palindromic_string(), 'ababa')

    def test_palindromic_string_2(self):
        manacher = Manacher('level')
        self.assertEqual(manacher.palindromic_string(), 'level')

    def test_palindromic_string_3(self):
        manacher = Manacher('xabbay')
        self.assertEqual(manacher.palindromic_string(), 'abba')

    def test_palindromic_string_4(self):
        manacher = Manacher('xyzracecarq')
        self.assertEqual(manacher.palindromic_string(), 'racecar')

    def test_palindromic_string_5(self):
        manacher = Manacher('z')
        self.assertEqual(manacher.palindromic_string(), 'z')