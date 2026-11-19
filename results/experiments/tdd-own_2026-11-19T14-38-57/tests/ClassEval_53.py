import unittest


import unittest

class AgentTest_add_word(unittest.TestCase):

    def test_add_word_1(self):
        longest_word = LongestWord()
        longest_word.add_word('A')
        self.assertEqual(longest_word.word_list, ['A'])

    def test_add_word_2(self):
        longest_word = LongestWord()
        longest_word.add_word('A')
        longest_word.add_word('aM')
        longest_word.add_word('student')
        self.assertEqual(longest_word.word_list, ['A', 'aM', 'student'])

    def test_add_word_3(self):
        longest_word = LongestWord()
        longest_word.add_word('aM')
        self.assertIn('aM', longest_word.word_list)
        self.assertNotIn('am', longest_word.word_list)

    def test_add_word_4(self):
        longest_word = LongestWord()
        longest_word.add_word('a')
        longest_word.add_word('a')
        self.assertEqual(longest_word.word_list, ['a', 'a'])

    def test_add_word_5(self):
        first = LongestWord()
        second = LongestWord()
        first.add_word('apple')
        self.assertEqual(first.word_list, ['apple'])
        self.assertEqual(second.word_list, [])

import unittest

class AgentTest_find_longest_word(unittest.TestCase):

    def test_find_longest_word_1(self):
        longest_word = LongestWord()
        self.assertEqual(longest_word.find_longest_word('I am a student.'), '')

    def test_find_longest_word_2(self):
        longest_word = LongestWord()
        longest_word.add_word('A')
        longest_word.add_word('aM')
        self.assertEqual(longest_word.find_longest_word('I am a student.'), 'a')

    def test_find_longest_word_3(self):
        longest_word = LongestWord()
        longest_word.add_word('hello')
        self.assertEqual(longest_word.find_longest_word('hello,'), 'hello')

    def test_find_longest_word_4(self):
        longest_word = LongestWord()
        longest_word.add_word('aM')
        longest_word.add_word('am')
        self.assertEqual(longest_word.find_longest_word('AM aM'), 'aM')

    def test_find_longest_word_5(self):
        longest_word = LongestWord()
        longest_word.add_word('cat')
        longest_word.add_word('student')
        longest_word.add_word('is')
        self.assertEqual(longest_word.find_longest_word('The student is a cat.'), 'student')