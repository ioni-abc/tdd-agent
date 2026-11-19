import unittest




class SplitSentenceTestSplitSentences(unittest.TestCase):
    def test_split_sentences_1(self):
        ss = SplitSentence()
        lst = ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        self.assertEqual(lst, ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?'])

    def test_split_sentences_2(self):
        ss = SplitSentence()
        lst = ss.split_sentences("Who is Mr. Smith? He is a teacher.")
        self.assertEqual(lst, ['Who is Mr. Smith?', 'He is a teacher.'])

    def test_split_sentences_3(self):
        ss = SplitSentence()
        lst = ss.split_sentences("Who is A.B.C.? He is a teacher.")
        self.assertEqual(lst, ['Who is A.B.C.?', 'He is a teacher.'])

import unittest

class AgentTest_split_sentences(unittest.TestCase):
    def test_split_sentences_1(self):
        ss = SplitSentence()
        lst = ss.split_sentences("Just one sentence here.")
        self.assertEqual(lst, ['Just one sentence here.'])

    def test_split_sentences_2(self):
        ss = SplitSentence()
        lst = ss.split_sentences("The price is 3.50 dollars. It is cheap?")
        self.assertEqual(lst, ['The price is 3.50 dollars.', 'It is cheap?'])

class SplitSentenceTestCountWords(unittest.TestCase):
    def test_count_words_1(self):
        ss = SplitSentence()
        cnt = ss.count_words("abc def")
        self.assertEqual(cnt, 2)

    def test_count_words_2(self):
        ss = SplitSentence()
        cnt = ss.count_words("abc def 1")
        self.assertEqual(cnt, 2)

    def test_count_words_3(self):
        ss = SplitSentence()
        cnt = ss.count_words("abc 1")
        self.assertEqual(cnt, 1)

import unittest

class AgentTest_count_words(unittest.TestCase):
    def test_count_words_1(self):
        ss = SplitSentence()
        cnt = ss.count_words("abc . def ?")
        self.assertEqual(cnt, 2)

    def test_count_words_2(self):
        ss = SplitSentence()
        cnt = ss.count_words("abc 12 def 3.5 ghi")
        self.assertEqual(cnt, 3)

class SplitSentenceTestProcessTextFile(unittest.TestCase):
    def test_process_text_file_1(self):
        ss = SplitSentence()
        cnt = ss.process_text_file("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?")
        self.assertEqual(cnt, 4)

    def test_process_text_file_2(self):
        ss = SplitSentence()
        cnt = ss.process_text_file("Mr. Smith is a teacher. Yes.")
        self.assertEqual(cnt, 5)

    def test_process_text_file_3(self):
        ss = SplitSentence()
        cnt = ss.process_text_file("Mr. Smith is a teacher. Yes 1 2 3 4 5 6.")
        self.assertEqual(cnt, 5)

import unittest

class AgentTest_process_text_file(unittest.TestCase):
    def test_process_text_file_1(self):
        ss = SplitSentence()
        cnt = ss.process_text_file("a b c d e f g? h. i j.")
        self.assertEqual(cnt, 7)

    def test_process_text_file_2(self):
        ss = SplitSentence()
        cnt = ss.process_text_file("1 2 3 4 5 6 7 8 9 10. a b c.")
        self.assertEqual(cnt, 3)