import unittest



class LemmatizationTestRemovePunctuation(unittest.TestCase):
    def test_remove_punctuation_1(self):
        lemmatization = Lemmatization()
        result = lemmatization.remove_punctuation("I am running in a race.")
        expected = "I am running in a race"
        self.assertEqual(result, expected)

    def test_remove_punctuation_2(self):
        lemmatization = Lemmatization()
        result = lemmatization.remove_punctuation("Until the beating, Cantanco's eyesight had been weak, but adequate.")
        expected = 'Until the beating Cantancos eyesight had been weak but adequate'
        self.assertEqual(result, expected)

    def test_remove_punctuation_3(self):
        lemmatization = Lemmatization()
        result = lemmatization.remove_punctuation("The dog's barked at the mailman!!!")
        expected = 'The dogs barked at the mailman'
        self.assertEqual(result, expected)

import unittest

import string

class AgentTest_remove_punctuation(unittest.TestCase):
    def test_remove_punctuation_1(self):
        lemmatization = Lemmatization()
        sentence = "I am running in a race"
        result = lemmatization.remove_punctuation(sentence)
        expected = "I am running in a race"
        self.assertEqual(result, expected)

    def test_remove_punctuation_2(self):
        lemmatization = Lemmatization()
        result = lemmatization.remove_punctuation("Hello, world; (really?) yes! \"Quoted\" and 'single' ok:")
        expected = "Hello world really yes Quoted and single ok"
        self.assertEqual(result, expected)

class LemmatizationTestLemmatizeSentence(unittest.TestCase):
    def test_lemmatize_sentence_1(self):
        lemmatization = Lemmatization()
        result = lemmatization.lemmatize_sentence("I am running in a race.")
        expected = ['I', 'be', 'run', 'in', 'a', 'race']
        self.assertEqual(result, expected)

    def test_lemmatize_sentence_2(self):
        lemmatization = Lemmatization()
        result = lemmatization.lemmatize_sentence("Until the beating, Cantanco's eyesight had been weak, but adequate.")
        expected = ['Until', 'the', 'beating', 'Cantancos', 'eyesight', 'have', 'be', 'weak', 'but', 'adequate']
        self.assertEqual(result, expected)

    def test_lammatize_sentence_3(self):
        lemmatization = Lemmatization()
        result = lemmatization.lemmatize_sentence("The dog's barked at the mailman.")
        expected = ['The', 'dog', 'bark', 'at', 'the', 'mailman']
        self.assertEqual(result, expected)

import unittest

class AgentTest_lemmatize_sentence(unittest.TestCase):
    def test_lemmatize_sentence_1(self):
        lemmatization = Lemmatization()
        result = lemmatization.lemmatize_sentence("The children played with the toys.")
        expected = ['The', 'child', 'play', 'with', 'the', 'toy']
        self.assertEqual(result, expected)

    def test_lemmatize_sentence_2(self):
        lemmatization = Lemmatization()
        result = lemmatization.lemmatize_sentence("Hello, world!")
        expected = ['Hello', 'world']
        self.assertEqual(result, expected)

class LemmatizationTestGetPosTag(unittest.TestCase):
    def test_get_pos_tag_1(self):
        lemmatization = Lemmatization()
        result = lemmatization.get_pos_tag("I am running in a race.")
        expected = ['PRP', 'VBP', 'VBG', 'IN', 'DT', 'NN']
        self.assertEqual(result, expected)

    def test_get_pos_tag_2(self):
        lemmatization = Lemmatization()
        result = lemmatization.get_pos_tag("Cantanco's eyesight had been weak, but adequate.")
        expected = ['NNP', 'NN', 'VBD', 'VBN', 'JJ', 'CC', 'JJ']
        self.assertEqual(result, expected)

    def test_get_pos_tag_3(self):
        lemmatization = Lemmatization()
        result = lemmatization.get_pos_tag("The dog's barked at the mailman.")
        expected = ['DT', 'NNS', 'VBD', 'IN', 'DT', 'NN']
        self.assertEqual(result, expected)

import string

class AgentTest_get_pos_tag(unittest.TestCase):
    def test_get_pos_tag_1(self):
        lemmatization = Lemmatization()
        result = lemmatization.get_pos_tag("Hello, world!")
        self.assertEqual(len(result), 2)
        for tag in result:
            self.assertTrue(tag.isalpha(), f"Punctuation tag found: {tag}")

    def test_get_pos_tag_2(self):
        lemmatization = Lemmatization()
        result = lemmatization.get_pos_tag("The cat sat on the mat; the dog slept.")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        for tag in result:
            self.assertIsInstance(tag, str)
            self.assertTrue(tag.isalpha(), f"Punctuation tag found: {tag}")