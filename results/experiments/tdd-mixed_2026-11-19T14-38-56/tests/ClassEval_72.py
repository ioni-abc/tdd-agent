import unittest




class RegexUtilsTestMatch(unittest.TestCase):
    def test_match_1(self):
        ru = RegexUtils()
        res = ru.match(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-7890")
        self.assertEqual(res, True)

    def test_match_2(self):
        ru = RegexUtils()
        res = ru.match(r'\b\d{3}-\d{3}-\d{4}\b', "1234567890")
        self.assertEqual(res, False)

    def test_match_3(self):
        ru = RegexUtils()
        res = ru.match(r'\b\d{3}-\d{3}-\d{4}\b', "111-111-1111")
        self.assertEqual(res, True)

import unittest

class AgentTest_match(unittest.TestCase):
    def test_match_1(self):
        ru = RegexUtils()
        res = ru.match(r'[A-Za-z]+', "hello")
        self.assertEqual(res, True)

    def test_match_2(self):
        ru = RegexUtils()
        res = ru.match(r'\b\d{3}-\d{3}-\d{4}\b', "1234-456-7890")
        self.assertEqual(res, False)

class RegexUtilsTestFindall(unittest.TestCase):
    def test_findall_1(self):
        ru = RegexUtils()
        res = ru.findall(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
        self.assertEqual(res, ['123-456-7890', '876-286-9876', '987-762-9767'])

    def test_findall_2(self):
        ru = RegexUtils()
        res = ru.findall(r'\b\d{3}-\d{3}-\d{4}\b', "abiguygusu  kjgufwycs 987-762-9767")
        self.assertEqual(res, ['987-762-9767'])

    def test_findall_3(self):
        ru = RegexUtils()
        res = ru.findall(r'\b\d{3}-\d{3}-\d{4}\b', "abiguygusu  kjgufwycs ")
        self.assertEqual(res, [])

import unittest

class AgentTest_findall(unittest.TestCase):
    def test_findall_1(self):
        ru = RegexUtils()
        res = ru.findall(r'\d+', "a1b22c333")
        self.assertEqual(res, ['1', '22', '333'])

    def test_findall_2(self):
        ru = RegexUtils()
        res = ru.findall(r'[A-Za-z]+', "")
        self.assertEqual(res, [])

class RegexUtilsTestSplit(unittest.TestCase):
    def test_split_1(self):
        ru = RegexUtils()
        res = ru.split(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
        self.assertEqual(res, ['', ' abiguygusu ', ' kjgufwycs ', ''])

    def test_split_2(self):
        ru = RegexUtils()
        res = ru.split(r'\b\d{3}-\d{3}-\d{4}\b', "1234567890 abiguygusu 8762869876 kjgufwycs 9877629767")
        self.assertEqual(res, ['1234567890 abiguygusu 8762869876 kjgufwycs 9877629767'])

    def test_split_3(self):
        ru = RegexUtils()
        res = ru.split(r'\b\d{3}-\d{3}-\d{4}\b', "111-111-1111 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
        self.assertEqual(res, ['', ' abiguygusu ', ' kjgufwycs ', ''])

import unittest

class AgentTest_split(unittest.TestCase):
    def test_split_1(self):
        ru = RegexUtils()
        res = ru.split(r',\s*', "apple, banana,cherry")
        self.assertEqual(res, ['apple', 'banana', 'cherry'])

    def test_split_2(self):
        ru = RegexUtils()
        res = ru.split(r'\d', "a12b")
        self.assertEqual(res, ['a', '', 'b'])

class RegexUtilsTestSub(unittest.TestCase):
    def test_sub_1(self):
        ru = RegexUtils()
        res = ru.sub(r'\b\d{3}-\d{3}-\d{4}\b', 'phone num',
                     "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
        self.assertEqual(res, 'phone num abiguygusu phone num kjgufwycs phone num')

    def test_sub_2(self):
        ru = RegexUtils()
        res = ru.sub(r'\b\d{3}-\d{3}-\d{4}\b', 'phone num',
                     "1234567890 abiguygusu 8762869876 kjgufwycs 9877629767")
        self.assertEqual(res, "1234567890 abiguygusu 8762869876 kjgufwycs 9877629767")

    def test_sub_3(self):
        ru = RegexUtils()
        res = ru.sub(r'\b\d{3}-\d{3}-\d{4}\b', 'phone num',
                     "123456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
        self.assertEqual(res, '123456-7890 abiguygusu phone num kjgufwycs phone num')

import unittest

class AgentTest_sub(unittest.TestCase):
    def test_sub_1(self):
        ru = RegexUtils()
        res = ru.sub(r'\d+', '', "a1b22c333")
        self.assertEqual(res, 'abc')

    def test_sub_2(self):
        ru = RegexUtils()
        res = ru.sub(r'[aeiou]', '*', "education")
        self.assertEqual(res, '*d*c*t**n')

class RegexUtilsTestGenerateEmailPattern(unittest.TestCase):
    def test_generate_email_pattern_1(self):
        ru = RegexUtils()
        pat = ru.generate_email_pattern()
        res = ru.match(pat, 'iustd87t2euh@163.com')
        self.assertEqual(res, True)

    def test_generate_email_pattern_2(self):
        ru = RegexUtils()
        pat = ru.generate_email_pattern()
        res = ru.match(pat, 'iustd87t2euhifg.com')
        self.assertEqual(res, False)

    def test_generate_email_pattern_3(self):
        ru = RegexUtils()
        pat = ru.generate_email_pattern()
        res = ru.match(pat, 'iustd87t2euhifg@.com')
        self.assertEqual(res, False)

import unittest

class AgentTest_generate_email_pattern(unittest.TestCase):
    def test_generate_email_pattern_1(self):
        ru = RegexUtils()
        pat = ru.generate_email_pattern()
        self.assertIsInstance(pat, str)
        res = ru.match(pat, 'john.doe_x+tag@mail.example.co.uk')
        self.assertEqual(res, True)

    def test_generate_email_pattern_2(self):
        ru = RegexUtils()
        pat = ru.generate_email_pattern()
        res = ru.match(pat, 'user@example.c')
        self.assertEqual(res, False)

class RegexUtilsTestGeneratePhoneNumberPattern(unittest.TestCase):
    def test_generate_phone_number_pattern_1(self):
        ru = RegexUtils()
        pat = ru.generate_phone_number_pattern()
        res = ru.match(pat, '123-456-7890')
        self.assertEqual(res, True)

    def test_generate_phone_number_pattern_2(self):
        ru = RegexUtils()
        pat = ru.generate_phone_number_pattern()
        res = ru.match(pat, '1234567890')
        self.assertEqual(res, False)

    def test_generate_phone_number_pattern_3(self):
        ru = RegexUtils()
        pat = ru.generate_phone_number_pattern()
        res = ru.match(pat, '123-456-789')
        self.assertEqual(res, False)

import unittest

class AgentTest_generate_phone_number_pattern(unittest.TestCase):
    def test_generate_phone_number_pattern_1(self):
        ru = RegexUtils()
        pat = ru.generate_phone_number_pattern()
        self.assertIsInstance(pat, str)
        res = ru.findall(pat, "Call 123-456-7890 or 987-762-9767 today")
        self.assertEqual(res, ['123-456-7890', '987-762-9767'])

    def test_generate_phone_number_pattern_2(self):
        ru = RegexUtils()
        pat = ru.generate_phone_number_pattern()
        res = ru.findall(pat, "123-456-78901")
        self.assertEqual(res, [])

class RegexUtilsTestGenerateSplitSentencesPattern(unittest.TestCase):
    def test_generate_split_sentences_pattern_1(self):
        ru = RegexUtils()
        pat = ru.generate_split_sentences_pattern()
        res = ru.match(pat, '? Y')
        self.assertEqual(res, True)

    def test_generate_split_sentences_pattern_2(self):
        ru = RegexUtils()
        pat = ru.generate_split_sentences_pattern()
        res = ru.match(pat, '! Y')
        self.assertEqual(res, True)

    def test_generate_split_sentences_pattern_3(self):
        ru = RegexUtils()
        pat = ru.generate_split_sentences_pattern()
        res = ru.match(pat, '? ')
        self.assertEqual(res, False)

import unittest

class AgentTest_generate_split_sentences_pattern(unittest.TestCase):
    def test_generate_split_sentences_pattern_1(self):
        ru = RegexUtils()
        pat = ru.generate_split_sentences_pattern()
        self.assertIsInstance(pat, str)
        res = ru.split(pat, "Aaa. Bbbb? Ccc!")
        self.assertEqual(res, ['Aaa', 'Bbbb', 'Ccc!'])

    def test_generate_split_sentences_pattern_2(self):
        ru = RegexUtils()
        pat = ru.generate_split_sentences_pattern()
        res_two_spaces = ru.match(pat, '.  Y')
        self.assertEqual(res_two_spaces, True)
        res_lowercase = ru.match(pat, '. y')
        self.assertEqual(res_lowercase, False)

class RegexUtilsTestSplitSentences(unittest.TestCase):
    def test_split_sentences_1(self):
        ru = RegexUtils()
        res = ru.split_sentences("Aaa. Bbbb? Ccc!")
        self.assertEqual(res, ['Aaa', 'Bbbb', 'Ccc!'])

    def test_split_sentences_2(self):
        ru = RegexUtils()
        res = ru.split_sentences("Aaa.Bbbb? Ccc!")
        self.assertEqual(res, ['Aaa.Bbbb', 'Ccc!'])

    def test_split_sentences_3(self):
        ru = RegexUtils()
        res = ru.split_sentences("Aaa. bbbb? Ccc!")
        self.assertEqual(res, ['Aaa. bbbb', 'Ccc!'])

import unittest

class AgentTest_split_sentences(unittest.TestCase):
    def test_split_sentences_1(self):
        ru = RegexUtils()
        res = ru.split_sentences("Hello world!")
        self.assertEqual(res, ['Hello world!'])

    def test_split_sentences_2(self):
        ru = RegexUtils()
        res = ru.split_sentences("Aaa. Bbbb.")
        self.assertEqual(res, ['Aaa', 'Bbbb.'])

class RegexUtilsTestValidatePhoneNumber(unittest.TestCase):
    def test_validate_phone_number_1(self):
        ru = RegexUtils()
        res = ru.validate_phone_number("123-456-7890")
        self.assertEqual(res, True)

    def test_validate_phone_number_2(self):
        ru = RegexUtils()
        res = ru.validate_phone_number("1234567890")
        self.assertEqual(res, False)

    def test_validate_phone_number_3(self):
        ru = RegexUtils()
        res = ru.validate_phone_number("a23-456-7890")
        self.assertEqual(res, False)

class AgentTest_validate_phone_number(unittest.TestCase):
    def test_validate_phone_number_1(self):
        ru = RegexUtils()
        res = ru.validate_phone_number("123-456-789")
        self.assertEqual(res, False)

    def test_validate_phone_number_2(self):
        ru = RegexUtils()
        res = ru.validate_phone_number("123-456-78901")
        self.assertEqual(res, False)

class RegexUtilsTestExtractEmail(unittest.TestCase):
    def test_extract_email_1(self):
        ru = RegexUtils()
        res = ru.extract_email("abcdefg@163.com ygusyfysy@126.com wljduyuv@qq.com")
        self.assertEqual(res, ['abcdefg@163.com', 'ygusyfysy@126.com', 'wljduyuv@qq.com'])

    def test_extract_email_2(self):
        ru = RegexUtils()
        res = ru.extract_email("abcdefg@.com ygusyfysy@126.com wljduyuv@qq.com")
        self.assertEqual(res, ['ygusyfysy@126.com', 'wljduyuv@qq.com'])

    def test_extract_email_3(self):
        ru = RegexUtils()
        res = ru.extract_email("abcdefgiscom ygusyfysy@126.com wljduyuv@qq.com")
        self.assertEqual(res, ['ygusyfysy@126.com', 'wljduyuv@qq.com'])

class AgentTest_extract_email(unittest.TestCase):
    def test_extract_email_1(self):
        ru = RegexUtils()
        res = ru.extract_email("")
        self.assertEqual(res, [])

    def test_extract_email_2(self):
        ru = RegexUtils()
        res = ru.extract_email("Contact john.doe_x+tag@mail.example.co.uk for details.")
        self.assertEqual(res, ['john.doe_x+tag@mail.example.co.uk'])