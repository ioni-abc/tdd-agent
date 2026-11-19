import unittest


import unittest

class AgentTest_construct_stop_word_list(unittest.TestCase):

    def setUp(self):
        self.processor = NLPDataProcessor()

    def test_construct_stop_word_list_1(self):
        result = self.processor.construct_stop_word_list()
        self.assertIsInstance(result, list)

    def test_construct_stop_word_list_2(self):
        result = self.processor.construct_stop_word_list()
        self.assertEqual(result, ['a', 'an', 'the'])

    def test_construct_stop_word_list_3(self):
        result = self.processor.construct_stop_word_list()
        self.assertEqual(len(result), 3)

    def test_construct_stop_word_list_4(self):
        result = self.processor.construct_stop_word_list()
        for word in result:
            self.assertIsInstance(word, str)

    def test_construct_stop_word_list_5(self):
        first = self.processor.construct_stop_word_list()
        second = self.processor.construct_stop_word_list()
        self.assertEqual(first, second)

import unittest

class AgentTest_remove_stop_words(unittest.TestCase):

    def setUp(self):
        self.processor = NLPDataProcessor()
        self.stop_words = ['a', 'an', 'the']

    def test_remove_stop_words_1(self):
        result = self.processor.remove_stop_words(['This is a test.'], self.stop_words)
        self.assertEqual(result, [['This', 'is', 'test.']])

    def test_remove_stop_words_2(self):
        result = self.processor.remove_stop_words(['This is a test.'], self.stop_words)
        self.assertIsInstance(result, list)

    def test_remove_stop_words_3(self):
        result = self.processor.remove_stop_words(['This is a test.'], ['is'])
        self.assertEqual(result, [['This', 'a', 'test.']])

    def test_remove_stop_words_4(self):
        result = self.processor.remove_stop_words(['a cat', 'the dog'], self.stop_words)
        self.assertEqual(result, [['cat'], ['dog']])

    def test_remove_stop_words_5(self):
        result = self.processor.remove_stop_words(['This is a test.'], [])
        self.assertEqual(result, [['This', 'is', 'a', 'test.']])

import unittest

class AgentTest_process(unittest.TestCase):

    def setUp(self):
        self.processor = NLPDataProcessor()

    def test_process_1(self):
        result = self.processor.process(['This is a test.'])
        self.assertEqual(result, [['This', 'is', 'test.']])

    def test_process_2(self):
        result = self.processor.process(['This is a test.'])
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], list)

    def test_process_3(self):
        result = self.processor.process(['a cat', 'the dog'])
        self.assertEqual(result, [['cat'], ['dog']])

    def test_process_4(self):
        result = self.processor.process(['a cat', 'the dog', 'an apple'])
        self.assertEqual(len(result), 3)
        self.assertEqual(result, [['cat'], ['dog'], ['apple']])

    def test_process_5(self):
        result = self.processor.process(['the cat and a dog'])
        self.assertEqual(result, [['cat', 'and', 'dog']])