import unittest


import unittest

from collections import Counter

import re

class AgentTest_calculate_word_frequency(unittest.TestCase):

    def setUp(self):
        self.processor = NLPDataProcessor2()

    def test_calculate_word_frequency_1(self):
        words_list = [['this', 'is', 'a', 'test'], ['this', 'is', 'another', 'test']]
        expected = {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        result = self.processor.calculate_word_frequency(words_list)
        self.assertEqual(result, expected)

    def test_calculate_word_frequency_2(self):
        words_list = [['a'] * 6 + ['b'] * 5 + ['c'] * 4 + ['d'] * 3 + ['e'] * 2 + ['f'] * 1]
        result = self.processor.calculate_word_frequency(words_list)
        expected = {'a': 6, 'b': 5, 'c': 4, 'd': 3, 'e': 2}
        self.assertEqual(len(result), 5)
        self.assertEqual(result, expected)
        self.assertNotIn('f', result)

    def test_calculate_word_frequency_3(self):
        words_list = [['x', 'y', 'y', 'z', 'z', 'z']]
        result = self.processor.calculate_word_frequency(words_list)
        self.assertEqual(list(result.keys()), ['z', 'y', 'x'])
        self.assertEqual(list(result.values()), [3, 2, 1])

    def test_calculate_word_frequency_4(self):
        result = self.processor.calculate_word_frequency([])
        self.assertEqual(result, {})

    def test_calculate_word_frequency_5(self):
        words_list = [['hello', 'hello', 'hello']]
        result = self.processor.calculate_word_frequency(words_list)
        self.assertEqual(result, {'hello': 3})

import unittest

from collections import Counter

import re

class AgentTest_process_data(unittest.TestCase):

    def setUp(self):
        self.processor = NLPDataProcessor2()

    def test_process_data_1(self):
        string_list = ['This is a test.']
        expected = [['this', 'is', 'a', 'test']]
        result = self.processor.process_data(string_list)
        self.assertEqual(result, expected)

    def test_process_data_2(self):
        string_list = ['This is a test.', 'This is another test.']
        expected = [['this', 'is', 'a', 'test'], ['this', 'is', 'another', 'test']]
        result = self.processor.process_data(string_list)
        self.assertEqual(result, expected)

    def test_process_data_3(self):
        result = self.processor.process_data([])
        self.assertEqual(result, [])

    def test_process_data_4(self):
        string_list = ['Hello, World! 123']
        expected = [['hello', 'world']]
        result = self.processor.process_data(string_list)
        self.assertEqual(result, expected)

    def test_process_data_5(self):
        string_list = ['NLP Data 2024 Rocks!']
        expected = [['nlp', 'data', 'rocks']]
        result = self.processor.process_data(string_list)
        self.assertEqual(result, expected)

class AgentTest_process(unittest.TestCase):

    def setUp(self):
        self.processor = NLPDataProcessor2()

    def test_process_1(self):
        string_list = ['This is a test.', 'This is another test.']
        expected = {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        result = self.processor.process(string_list)
        self.assertEqual(result, expected)

    def test_process_2(self):
        string_list = ['a a a a a a b b b b b c c c c d d d e e f']
        result = self.processor.process(string_list)
        self.assertEqual(len(result), 5)
        self.assertEqual(result, {'a': 6, 'b': 5, 'c': 4, 'd': 3, 'e': 2})
        self.assertNotIn('f', result)

    def test_process_3(self):
        string_list = ['x y y z z z']
        result = self.processor.process(string_list)
        self.assertEqual(list(result.keys()), ['z', 'y', 'x'])
        self.assertEqual(list(result.values()), [3, 2, 1])

    def test_process_4(self):
        string_list = ['Hello, World! 123', 'hello again.']
        result = self.processor.process(string_list)
        self.assertEqual(result, {'hello': 2, 'world': 1, 'again': 1})

    def test_process_5(self):
        string_list = ['NLP nlp Nlp']
        result = self.processor.process(string_list)
        self.assertEqual(result, {'nlp': 3})