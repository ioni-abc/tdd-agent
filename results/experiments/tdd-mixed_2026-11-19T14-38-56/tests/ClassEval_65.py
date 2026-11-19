import unittest




class NumberWordFormatterTestTransTwo(unittest.TestCase):
    def test_trans_two_1(self):
        formatter = NumberWordFormatter()
        self.assertEqual(formatter.trans_two("23"), "TWENTY THREE")

    def test_trans_two_2(self):
        formatter = NumberWordFormatter()
        self.assertEqual(formatter.trans_two("10"), "TEN")

    def test_trans_two_3(self):
        formatter = NumberWordFormatter()
        self.assertEqual(formatter.trans_two("05"), "FIVE")

    def test_trans_two_4(self):
        formatter = NumberWordFormatter()
        self.assertEqual(formatter.trans_two("00"), "")

import unittest

class AgentTest_trans_two(unittest.TestCase):
    def test_trans_two_1(self):
        formatter = NumberWordFormatter()
        self.assertEqual(formatter.trans_two("15"), "FIFTEEN")

    def test_trans_two_2(self):
        formatter = NumberWordFormatter()
        self.assertEqual(formatter.trans_two("99"), "NINETY NINE")

class NumberWordFormatterTestTransThree(unittest.TestCase):
    def test_trans_three_1(self):
        formatter = NumberWordFormatter()
        self.assertEqual(formatter.trans_three("123"), "ONE HUNDRED AND TWENTY THREE")

    def test_trans_three_2(self):
        formatter = NumberWordFormatter()
        self.assertEqual(formatter.trans_three("900"), "NINE HUNDRED")

    def test_trans_three_3(self):
        formatter = NumberWordFormatter()
        self.assertEqual(formatter.trans_three("007"), "SEVEN")

import unittest

class AgentTest_trans_three(unittest.TestCase):
    def test_trans_three_1(self):
        formatter = NumberWordFormatter()
        self.assertEqual(formatter.trans_three("100"), "ONE HUNDRED")

    def test_trans_three_2(self):
        formatter = NumberWordFormatter()
        self.assertEqual(formatter.trans_three("720"), "SEVEN HUNDRED AND TWENTY")

class NumberWordFormatterTestParseMore(unittest.TestCase):
    def test_parse_more_1(self):
        formatter = NumberWordFormatter()
        self.assertEqual(formatter.parse_more(0), "")

    def test_parse_more_2(self):
        formatter = NumberWordFormatter()
        self.assertEqual(formatter.parse_more(1), "THOUSAND")

    def test_parse_more_3(self):
        formatter = NumberWordFormatter()
        self.assertEqual(formatter.parse_more(2), "MILLION")

import unittest

class AgentTest_parse_more(unittest.TestCase):
    def test_parse_more_1(self):
        formatter = NumberWordFormatter()
        self.assertEqual(formatter.parse_more(3), "BILLION")

class NumberWordFormatterTestFormatString(unittest.TestCase):
    def test_format_string_1(self):
        formatter = NumberWordFormatter()
        self.assertEqual(formatter.format_string('123456'),
                         "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY")

    def test_format_string_2(self):
        formatter = NumberWordFormatter()
        self.assertEqual(formatter.format_string('1000'), "ONE THOUSAND ONLY")

    def test_format_string_3(self):
        formatter = NumberWordFormatter()
        self.assertEqual(formatter.format_string('1000000'), "ONE MILLION ONLY")

    def test_format_string_4(self):
        formatter = NumberWordFormatter()
        self.assertEqual(formatter.format_string('1.23'), "ONE AND CENTS TWENTY THREE ONLY")

import unittest

class AgentTest_format_string(unittest.TestCase):
    def test_format_string_1(self):
        formatter = NumberWordFormatter()
        self.assertEqual(formatter.format_string('2.50'), "TWO AND CENTS FIFTY ONLY")

    def test_format_string_2(self):
        formatter = NumberWordFormatter()
        self.assertEqual(formatter.format_string('999'), "NINE HUNDRED AND NINETY NINE ONLY")

class NumberWordFormatterTestFormat(unittest.TestCase):
    def test_format_1(self):
        formatter = NumberWordFormatter()
        self.assertEqual(formatter.format(123456),
                         "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY")

    def test_format_2(self):
        formatter = NumberWordFormatter()
        self.assertEqual(formatter.format(1000), "ONE THOUSAND ONLY")

    def test_format_3(self):
        formatter = NumberWordFormatter()
        self.assertEqual(formatter.format(1000000), "ONE MILLION ONLY")

    def test_format_4(self):
        formatter = NumberWordFormatter()
        self.assertEqual(formatter.format(1.23), "ONE AND CENTS TWENTY THREE ONLY")

import unittest

class AgentTest_format(unittest.TestCase):
    def test_format_1(self):
        formatter = NumberWordFormatter()
        self.assertEqual(formatter.format(999),
                         "NINE HUNDRED AND NINETY NINE ONLY")

    def test_format_2(self):
        formatter = NumberWordFormatter()
        self.assertEqual(formatter.format(1000000000),
                         "ONE BILLION ONLY")