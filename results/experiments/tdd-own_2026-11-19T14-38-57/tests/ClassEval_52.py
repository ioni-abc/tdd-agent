import unittest


import unittest

import string

class AgentTest_remove_punctuation(unittest.TestCase):

    def setUp(self):
        self.lemmatization = Lemmatization()

    def test_remove_punctuation_1(self):
        result = self.lemmatization.remove_punctuation("I am running in a race.")
        self.assertEqual(result, 'I am running in a race')

    def test_remove_punctuation_2(self):
        sentence = "I am running in a race"
        result = self.lemmatization.remove_punctuation(sentence)
        self.assertEqual(result, sentence)

    def test_remove_punctuation_3(self):
        result = self.lemmatization.remove_punctuation("Hello, world!")
        self.assertEqual(result, 'Hello world')

    def test_remove_punctuation_4(self):
        sentence = "Wait... what? (really); yes: 'no' \"maybe\" - ok/fine #1 & @home!"
        result = self.lemmatization.remove_punctuation(sentence)
        for ch in string.punctuation:
            with self.subTest(char=ch):
                self.assertNotIn(ch, result)

    def test_remove_punctuation_5(self):
        result = self.lemmatization.remove_punctuation("Room 101, floor 2.")
        self.assertEqual(result, 'Room 101 floor 2')
        self.assertIsInstance(result, str)

import unittest

import string

class AgentTest_lemmatize_sentence(unittest.TestCase):

    def setUp(self):
        self.lemmatization = Lemmatization()

    def test_lemmatize_sentence_1(self):
        result = self.lemmatization.lemmatize_sentence("I am running in a race.")
        self.assertEqual(result, ['I', 'be', 'run', 'in', 'a', 'race'])

    def test_lemmatize_sentence_2(self):
        result = self.lemmatization.lemmatize_sentence("Wait... what? (really); yes: 'no' \"maybe\" - ok/fine #1 & @home!")
        self.assertIsInstance(result, list)
        for word in result:
            self.assertIsInstance(word, str)
            for ch in string.punctuation:
                with self.subTest(word=word, char=ch):
                    self.assertNotIn(ch, word)

    def test_lemmatize_sentence_3(self):
        result = self.lemmatization.lemmatize_sentence("hello, world!")
        self.assertEqual(result, ['hello', 'world'])

    def test_lemmatize_sentence_4(self):
        result = self.lemmatization.lemmatize_sentence("the dogs were running quickly.")
        self.assertIn('dog', result)
        self.assertIn('be', result)
        self.assertIn('run', result)
        self.assertNotIn('dogs', result)
        self.assertNotIn('were', result)
        self.assertNotIn('running', result)

    def test_lemmatize_sentence_5(self):
        result = self.lemmatization.lemmatize_sentence("The cats sat on the mats.")
        self.assertEqual(result, ['The', 'cat', 'sit', 'on', 'the', 'mat'])

import unittest

import string

class AgentTest_get_pos_tag(unittest.TestCase):

    def setUp(self):
        self.lemmatization = Lemmatization()

    def test_get_pos_tag_1(self):
        result = self.lemmatization.get_pos_tag("I am running in a race.")
        self.assertEqual(result, ['PRP', 'VBP', 'VBG', 'IN', 'DT', 'NN'])

    def test_get_pos_tag_2(self):
        result = self.lemmatization.get_pos_tag("Hello, world!")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
        for tag in result:
            self.assertIsInstance(tag, str)

    def test_get_pos_tag_3(self):
        result = self.lemmatization.get_pos_tag("Room 101, floor 2.")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 4)
        for tag in result:
            self.assertIsInstance(tag, str)
            self.assertTrue(any(ch.isalpha() for ch in tag))

    def test_get_pos_tag_4(self):
        result = self.lemmatization.get_pos_tag("Wait... what? (really); yes: 'no' \"maybe\" - ok/fine #1 & @home!")
        self.assertIsInstance(result, list)
        for tag in result:
            self.assertIsInstance(tag, str)
            for ch in string.punctuation:
                with self.subTest(tag=tag, char=ch):
                    self.assertNotIn(ch, tag)

    def test_get_pos_tag_5(self):
        with_punct = self.lemmatization.get_pos_tag("I am running in a race.")
        without_punct = self.lemmatization.get_pos_tag("I am running in a race")
        self.assertEqual(with_punct, without_punct)