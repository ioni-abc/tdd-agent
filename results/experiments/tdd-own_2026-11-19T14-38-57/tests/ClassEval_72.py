import unittest


import unittest

class AgentTest_match(unittest.TestCase):

    def test_match_1(self):
        ru = RegexUtils()
        self.assertIs(ru.match(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-7890"), True)

    def test_match_2(self):
        ru = RegexUtils()
        self.assertIs(ru.match(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-789"), False)

    def test_match_3(self):
        ru = RegexUtils()
        self.assertIs(ru.match(r'\d+', "12345"), True)

    def test_match_4(self):
        ru = RegexUtils()
        self.assertIs(ru.match(r'[A-Z]{3}', "abc"), False)

    def test_match_5(self):
        ru = RegexUtils()
        result = ru.match(r'[a-z]+', "hello")
        self.assertIs(result, True)

import unittest

class AgentTest_findall(unittest.TestCase):

    def test_findall_1(self):
        ru = RegexUtils()
        result = ru.findall(r'\b\d{3}-\d{3}-\d{4}\b',
                            "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
        self.assertEqual(result, ['123-456-7890', '876-286-9876', '987-762-9767'])

    def test_findall_2(self):
        ru = RegexUtils()
        result = ru.findall(r'\b\d{3}-\d{3}-\d{4}\b', "no phone numbers here")
        self.assertEqual(result, [])

    def test_findall_3(self):
        ru = RegexUtils()
        result = ru.findall(r'\d+', "a1b22c333")
        self.assertEqual(result, ['1', '22', '333'])

    def test_findall_4(self):
        ru = RegexUtils()
        result = ru.findall(r'[A-Z]', "Hello World")
        self.assertEqual(result, ['H', 'W'])

    def test_findall_5(self):
        ru = RegexUtils()
        result = ru.findall(r'\b\d{3}-\d{3}-\d{4}\b', "Call 123-456-7890 now")
        self.assertEqual(result, ['123-456-7890'])

import unittest

class AgentTest_split(unittest.TestCase):

    def test_split_1(self):
        ru = RegexUtils()
        result = ru.split(r'\b\d{3}-\d{3}-\d{4}\b',
                          "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
        self.assertEqual(result, ['', ' abiguygusu ', ' kjgufwycs ', ''])

    def test_split_2(self):
        ru = RegexUtils()
        result = ru.split(r'\d+', "no digits here")
        self.assertEqual(result, ['no digits here'])

    def test_split_3(self):
        ru = RegexUtils()
        result = ru.split(r',', "a,b,c")
        self.assertEqual(result, ['a', 'b', 'c'])

    def test_split_4(self):
        ru = RegexUtils()
        result = ru.split(r'\s+', "one two  three")
        self.assertEqual(result, ['one', 'two', 'three'])

    def test_split_5(self):
        ru = RegexUtils()
        result = ru.split(r'\b\d{3}-\d{3}-\d{4}\b', "Call 123-456-7890 now")
        self.assertEqual(result, ['Call ', ' now'])

import unittest

class AgentTest_sub(unittest.TestCase):

    def test_sub_1(self):
        ru = RegexUtils()
        result = ru.sub(r'\b\d{3}-\d{3}-\d{4}\b', 'phone num',
                        "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
        self.assertEqual(result, 'phone num abiguygusu phone num kjgufwycs phone num')

    def test_sub_2(self):
        ru = RegexUtils()
        result = ru.sub(r'\b\d{3}-\d{3}-\d{4}\b', 'phone num', "no phone numbers here")
        self.assertEqual(result, "no phone numbers here")

    def test_sub_3(self):
        ru = RegexUtils()
        result = ru.sub(r'\d+', '#', "a1b22c333")
        self.assertEqual(result, 'a#b#c#')

    def test_sub_4(self):
        ru = RegexUtils()
        result = ru.sub(r'cat', 'dog', "cat and cat")
        self.assertEqual(result, 'dog and dog')

    def test_sub_5(self):
        ru = RegexUtils()
        result = ru.sub(r'\b\d{3}-\d{3}-\d{4}\b', 'phone num', "Call 123-456-7890 now")
        self.assertEqual(result, 'Call phone num now')

import re

import unittest

class AgentTest_generate_email_pattern(unittest.TestCase):

    def test_generate_email_pattern_1(self):
        ru = RegexUtils()
        result = ru.generate_email_pattern()
        self.assertEqual(result, r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    def test_generate_email_pattern_2(self):
        ru = RegexUtils()
        result = ru.generate_email_pattern()
        self.assertIsInstance(result, str)

    def test_generate_email_pattern_3(self):
        ru = RegexUtils()
        pattern = ru.generate_email_pattern()
        result = re.findall(pattern, "abcdefg@163.com ygusyfysy@126.com wljduyuv@qq.com")
        self.assertEqual(result, ['abcdefg@163.com', 'ygusyfysy@126.com', 'wljduyuv@qq.com'])

    def test_generate_email_pattern_4(self):
        ru = RegexUtils()
        pattern = ru.generate_email_pattern()
        self.assertIsNone(re.search(pattern, "user@domain"))
        self.assertIsNone(re.search(pattern, "abc@"))

    def test_generate_email_pattern_5(self):
        ru = RegexUtils()
        pattern = ru.generate_email_pattern()
        result = re.findall(pattern, "no email addresses in this sentence")
        self.assertEqual(result, [])

import re

import unittest

class AgentTest_generate_phone_number_pattern(unittest.TestCase):

    def test_generate_phone_number_pattern_1(self):
        ru = RegexUtils()
        result = ru.generate_phone_number_pattern()
        self.assertEqual(result, r'\b\d{3}-\d{3}-\d{4}\b')

    def test_generate_phone_number_pattern_2(self):
        ru = RegexUtils()
        result = ru.generate_phone_number_pattern()
        self.assertIsInstance(result, str)

    def test_generate_phone_number_pattern_3(self):
        ru = RegexUtils()
        pattern = ru.generate_phone_number_pattern()
        self.assertIsNotNone(re.search(pattern, "123-456-7890"))
        self.assertIsNone(re.search(pattern, "123-456-789"))

    def test_generate_phone_number_pattern_4(self):
        ru = RegexUtils()
        pattern = ru.generate_phone_number_pattern()
        self.assertIsNone(re.search(pattern, "phone number: abc-def-ghij"))
        self.assertIsNone(re.search(pattern, "1234-567-89012"))

    def test_generate_phone_number_pattern_5(self):
        ru = RegexUtils()
        pattern = ru.generate_phone_number_pattern()
        result = re.findall(pattern, "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
        self.assertEqual(result, ['123-456-7890', '876-286-9876', '987-762-9767'])

import re

import unittest

class AgentTest_generate_split_sentences_pattern(unittest.TestCase):

    def test_generate_split_sentences_pattern_1(self):
        ru = RegexUtils()
        result = ru.generate_split_sentences_pattern()
        self.assertEqual(result, r'[.!?][\s]{1,2}(?=[A-Z])')

    def test_generate_split_sentences_pattern_2(self):
        ru = RegexUtils()
        result = ru.generate_split_sentences_pattern()
        self.assertIsInstance(result, str)

    def test_generate_split_sentences_pattern_3(self):
        ru = RegexUtils()
        pattern = ru.generate_split_sentences_pattern()
        result = re.split(pattern, "Aaa. Bbbb? Ccc!")
        self.assertEqual(result, ['Aaa', 'Bbbb', 'Ccc!'])

    def test_generate_split_sentences_pattern_4(self):
        ru = RegexUtils()
        pattern = ru.generate_split_sentences_pattern()
        result = re.findall(pattern, "Hi! How are you? Fine.")
        self.assertEqual(result, ['! ', '? '])

    def test_generate_split_sentences_pattern_5(self):
        ru = RegexUtils()
        pattern = ru.generate_split_sentences_pattern()
        self.assertIsNotNone(re.search(pattern, "Stop.  Go"))
        self.assertIsNone(re.search(pattern, "e.g. this"))

import unittest

class AgentTest_split_sentences(unittest.TestCase):

    def test_split_sentences_1(self):
        ru = RegexUtils()
        result = ru.split_sentences("Aaa. Bbbb? Ccc!")
        self.assertEqual(result, ['Aaa', 'Bbbb', 'Ccc!'])

    def test_split_sentences_2(self):
        ru = RegexUtils()
        result = ru.split_sentences("Aaa. Bbbb? Ccc!")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)

    def test_split_sentences_3(self):
        ru = RegexUtils()
        result = ru.split_sentences("One. Two.")
        self.assertEqual(result, ['One', 'Two.'])

    def test_split_sentences_4(self):
        ru = RegexUtils()
        result = ru.split_sentences("Hello world")
        self.assertEqual(result, ['Hello world'])

    def test_split_sentences_5(self):
        ru = RegexUtils()
        result = ru.split_sentences("Stop! Go? Now")
        self.assertEqual(result, ['Stop', 'Go', 'Now'])

import unittest

class AgentTest_validate_phone_number(unittest.TestCase):

    def test_validate_phone_number_1(self):
        ru = RegexUtils()
        self.assertIs(ru.validate_phone_number("123-456-7890"), True)

    def test_validate_phone_number_2(self):
        ru = RegexUtils()
        self.assertIs(ru.validate_phone_number("123-456-789"), False)

    def test_validate_phone_number_3(self):
        ru = RegexUtils()
        self.assertIs(ru.validate_phone_number("abc-def-ghij"), False)

    def test_validate_phone_number_4(self):
        ru = RegexUtils()
        self.assertIs(ru.validate_phone_number("1234-567-89012"), False)

    def test_validate_phone_number_5(self):
        ru = RegexUtils()
        self.assertIs(ru.validate_phone_number("1234567890"), False)

import unittest

class AgentTest_extract_email(unittest.TestCase):

    def test_extract_email_1(self):
        ru = RegexUtils()
        result = ru.extract_email("abcdefg@163.com ygusyfysy@126.com wljduyuv@qq.com")
        self.assertEqual(result, ['abcdefg@163.com', 'ygusyfysy@126.com', 'wljduyuv@qq.com'])

    def test_extract_email_2(self):
        ru = RegexUtils()
        result = ru.extract_email("no email addresses in this sentence")
        self.assertEqual(result, [])

    def test_extract_email_3(self):
        ru = RegexUtils()
        result = ru.extract_email("Contact abcdefg@163.com for details")
        self.assertEqual(result, ['abcdefg@163.com'])

    def test_extract_email_4(self):
        ru = RegexUtils()
        result = ru.extract_email("abcdefg@163.com ygusyfysy@126.com")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)

    def test_extract_email_5(self):
        ru = RegexUtils()
        result = ru.extract_email("Call 123-456-7890 or write to test.user@example.org")
        self.assertEqual(result, ['test.user@example.org'])