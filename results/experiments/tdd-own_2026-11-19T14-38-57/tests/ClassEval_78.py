import unittest


import unittest

import re

class AgentTest_split_sentences(unittest.TestCase):

    def test_split_sentences_1(self):
        ss = SplitSentence()
        result = ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        self.assertEqual(result, ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?'])

    def test_split_sentences_2(self):
        ss = SplitSentence()
        result = ss.split_sentences("Hello world.")
        self.assertEqual(result, ['Hello world.'])

    def test_split_sentences_3(self):
        ss = SplitSentence()
        result = ss.split_sentences("Is it ok? Yes it is.")
        self.assertEqual(result, ['Is it ok?', 'Yes it is.'])

    def test_split_sentences_4(self):
        ss = SplitSentence()
        result = ss.split_sentences("Mr. Smith went home. He was tired.")
        self.assertEqual(result, ['Mr. Smith went home.', 'He was tired.'])

    def test_split_sentences_5(self):
        ss = SplitSentence()
        result = ss.split_sentences("First.Second sentence. Third one.")
        self.assertEqual(result, ['First.Second sentence.', 'Third one.'])

import unittest

import unittest

import re

class AgentTest_count_words(unittest.TestCase):

    def test_count_words_1(self):
        ss = SplitSentence()
        result = ss.count_words("abc def")
        self.assertEqual(result, 2)

    def test_count_words_2(self):
        ss = SplitSentence()
        result = ss.count_words("bb bbbb bbb?")
        self.assertEqual(result, 3)

    def test_count_words_3(self):
        ss = SplitSentence()
        result = ss.count_words("aaa aaaa.")
        self.assertEqual(result, 2)

    def test_count_words_4(self):
        ss = SplitSentence()
        result = ss.count_words("abc 123 def")
        self.assertEqual(result, 2)

    def test_count_words_5(self):
        ss = SplitSentence()
        result = ss.count_words("abc - def .")
        self.assertEqual(result, 2)

import unittest

class AgentTest_process_text_file(unittest.TestCase):

    def test_process_text_file_1(self):
        ss = SplitSentence()
        result = ss.process_text_file("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?")
        self.assertEqual(result, 4)

    def test_process_text_file_2(self):
        ss = SplitSentence()
        result = ss.process_text_file("Hello world.")
        self.assertEqual(result, 2)

    def test_process_text_file_3(self):
        ss = SplitSentence()
        result = ss.process_text_file("One. Two three four. Five six.")
        self.assertEqual(result, 3)

    def test_process_text_file_4(self):
        ss = SplitSentence()
        result = ss.process_text_file("Mr. Smith went home. He was tired.")
        self.assertEqual(result, 4)

    def test_process_text_file_5(self):
        ss = SplitSentence()
        result = ss.process_text_file("abc 123 def 456 ghi. ab.")
        self.assertEqual(result, 3)