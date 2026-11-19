import unittest



class LongestWordTestAddWord(unittest.TestCase):
    def test_add_word_1(self):
        longestWord = LongestWord()
        longestWord.add_word("hello")
        self.assertEqual(['hello'], longestWord.word_list)

    def test_add_word_2(self):
        longestWord = LongestWord()
        longestWord.add_word("hello")
        longestWord.add_word("world")
        self.assertEqual(['hello', 'world'], longestWord.word_list)

    def test_add_word_3(self):
        longestWord = LongestWord()
        longestWord.add_word("hello")
        longestWord.add_word("world")
        longestWord.add_word("!")
        self.assertEqual(['hello', 'world', '!'], longestWord.word_list)

import unittest

class AgentTest_add_word(unittest.TestCase):
    def test_add_word_1(self):
        longestWord = LongestWord()
        longestWord.add_word("A")
        longestWord.add_word("aM")
        self.assertEqual(['A', 'aM'], longestWord.word_list)

    def test_add_word_2(self):
        longestWord = LongestWord()
        longestWord.add_word("hello")
        longestWord.add_word("hello")
        self.assertEqual(['hello', 'hello'], longestWord.word_list)

class LongestWordTestFindLongestWord(unittest.TestCase):
    def test_find_longest_word_1(self):
        longestWord = LongestWord()
        longestWord.add_word("a")
        sentence = 'I am a student.'
        self.assertEqual('a', longestWord.find_longest_word(sentence))

    def test_find_longest_word_2(self):
        longestWord = LongestWord()
        sentence = 'I am a student.'
        self.assertEqual('', longestWord.find_longest_word(sentence))

    def test_find_longest_word_3(self):
        longestWord = LongestWord()
        longestWord.add_word("student")
        sentence = 'I am a student.'
        self.assertEqual('student', longestWord.find_longest_word(sentence))

import unittest

class AgentTest_find_longest_word(unittest.TestCase):
    def test_find_longest_word_1(self):
        longestWord = LongestWord()
        longestWord.add_word("Student")
        longestWord.add_word("I")
        sentence = 'I am a student.'
        self.assertEqual('I', longestWord.find_longest_word(sentence))

    def test_find_longest_word_2(self):
        longestWord = LongestWord()
        longestWord.add_word("hello")
        longestWord.add_word("wonderful")
        sentence = '(wonderful), hello!!!'
        self.assertEqual('wonderful', longestWord.find_longest_word(sentence))