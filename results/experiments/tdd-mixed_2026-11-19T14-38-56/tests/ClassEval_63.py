import unittest



class NLPDataProcessorTestCalculate(unittest.TestCase):

    def setUp(self):
        self.processor = NLPDataProcessor2()

    def test_calculate_word_frequency(self):
        words_list = [['hello', 'world'], ['this', 'is', 'a', 'test'], ['hello', 'world', 'this', 'is', 'another', 'test'],
                      ['hello', 'hello', 'world']]
        expected_output = {'hello': 4, 'world': 3, 'this': 2, 'is': 2, 'test': 2}
        self.assertEqual(self.processor.calculate_word_frequency(words_list), expected_output)

    def test_calculate_word_frequency2(self):
        words_list = [['hello', 'world'], ['this', 'is', 'a', 'test'], ['hello', 'world', 'this', 'is', 'another', 'test'],
                      ['hello', 'hello', 'world'], ['world', 'world', 'world']]
        expected_output = {'world': 6, 'hello': 4, 'this': 2, 'is': 2, 'test': 2}
        self.assertEqual(self.processor.calculate_word_frequency(words_list), expected_output)

    def test_calculate_word_frequency3(self):
        words_list = [['hello', 'world'], ['hello', 'hello', 'world'], ['world', 'world']]
        expected_output = {'world': 4, 'hello': 3}
        self.assertEqual(self.processor.calculate_word_frequency(words_list), expected_output)

import unittest

class AgentTest_calculate_word_frequency(unittest.TestCase):

    def setUp(self):
        self.processor = NLPDataProcessor2()

    def test_calculate_word_frequency_1(self):
        words_list = []
        expected_output = {}
        self.assertEqual(self.processor.calculate_word_frequency(words_list), expected_output)

    def test_calculate_word_frequency_2(self):
        words_list = [[], ['a', 'b', 'a'], []]
        result = self.processor.calculate_word_frequency(words_list)
        expected_output = {'a': 2, 'b': 1}
        self.assertEqual(result, expected_output)
        self.assertEqual(list(result.keys())[0], 'a')

class NLPDataProcessorTestProcessData(unittest.TestCase):

    def setUp(self):
        self.processor = NLPDataProcessor2()

    def test_process_data(self):
        string_list = ["Hello World!", "This is a test."]
        expected_output = [['hello', 'world'], ['this', 'is', 'a', 'test']]
        self.assertEqual(self.processor.process_data(string_list), expected_output)

    def test_process_data2(self):
        string_list = ["12345", "Special@Characters"]
        expected_output = [[], ['specialcharacters']]
        self.assertEqual(self.processor.process_data(string_list), expected_output)

    def test_process_data3(self):
        string_list = []
        expected_output = []
        self.assertEqual(self.processor.process_data(string_list), expected_output)

import unittest

class AgentTest_process_data(unittest.TestCase):

    def setUp(self):
        self.processor = NLPDataProcessor2()

    def test_process_data_1(self):
        string_list = ["tab\there\nnew"]
        expected_output = [['tabherenew']]
        self.assertEqual(self.processor.process_data(string_list), expected_output)

    def test_process_data_2(self):
        string_list = ["Don't STOP", "Rock'n'roll!"]
        expected_output = [['dont', 'stop'], ['rocknroll']]
        self.assertEqual(self.processor.process_data(string_list), expected_output)

class NLPDataProcessorTestProcess(unittest.TestCase):

    def setUp(self):
        self.processor = NLPDataProcessor2()

    def test_process(self):
        string_list = ["Hello World!", "This is a test.", "Hello World, this is a test."]
        expected_output = {'hello': 2, 'world': 2, 'this': 2, 'is': 2, 'a': 2}
        self.assertEqual(self.processor.process(string_list), expected_output)

    def test_process2(self):
        string_list = []
        expected_output = []
        self.assertEqual(self.processor.process_data(string_list), expected_output)

    def test_calculate3(self):
        words_list = []
        expected_output = {}
        self.assertEqual(self.processor.calculate_word_frequency(words_list), expected_output)

    def test_process4(self):
        string_list = ["@#$%^&*", "Special_Characters", "12345"]
        expected_output = [[], ['specialcharacters'], []]
        self.assertEqual(self.processor.process_data(string_list), expected_output)

import unittest

class AgentTest_process(unittest.TestCase):

    def setUp(self):
        self.processor = NLPDataProcessor2()

    def test_process_1(self):
        string_list = [
            "alpha alpha alpha alpha alpha alpha beta beta beta beta beta",
            "gamma gamma gamma gamma delta delta delta epsilon epsilon zeta",
        ]
        result = self.processor.process(string_list)
        expected_output = {'alpha': 6, 'beta': 5, 'gamma': 4, 'delta': 3, 'epsilon': 2}
        self.assertEqual(result, expected_output)
        self.assertEqual(len(result), 5)
        self.assertNotIn('zeta', result)

    def test_process_2(self):
        string_list = ["Red red RED!", "blue, Blue, green", "dog42 dog"]
        result = self.processor.process(string_list)
        expected_output = {'red': 3, 'blue': 2, 'dog': 2, 'green': 1}
        self.assertEqual(result, expected_output)
        self.assertEqual(list(result.values()), sorted(result.values(), reverse=True))