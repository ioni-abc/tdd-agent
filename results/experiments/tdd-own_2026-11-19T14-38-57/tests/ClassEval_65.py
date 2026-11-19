import unittest


import unittest

class AgentTest_trans_two(unittest.TestCase):

    def setUp(self):
        self.formatter = NumberWordFormatter()

    def test_trans_two_1(self):
        # Docstring example: tens word followed by units word
        self.assertEqual(self.formatter.trans_two("23"), "TWENTY THREE")

    def test_trans_two_2(self):
        # Teen range (10-19) uses the dedicated teen words
        self.assertEqual(self.formatter.trans_two("11"), "ELEVEN")

    def test_trans_two_3(self):
        # Exact multiple of ten has no units word
        self.assertEqual(self.formatter.trans_two("20"), "TWENTY")

    def test_trans_two_4(self):
        # Largest two-digit number
        self.assertEqual(self.formatter.trans_two("99"), "NINETY NINE")

    def test_trans_two_5(self):
        # Lower boundary of the teen range
        self.assertEqual(self.formatter.trans_two("10"), "TEN")

import unittest

class AgentTest_trans_three(unittest.TestCase):

    def setUp(self):
        self.formatter = NumberWordFormatter()

    def test_trans_three_1(self):
        # Docstring example: hundreds word, connector, then tens and units
        self.assertEqual(self.formatter.trans_three("123"), "ONE HUNDRED AND TWENTY THREE")

    def test_trans_three_2(self):
        # Largest three-digit number
        self.assertEqual(self.formatter.trans_three("999"), "NINE HUNDRED AND NINETY NINE")

    def test_trans_three_3(self):
        # Hundreds followed by a units-only remainder, connector still applies
        self.assertEqual(self.formatter.trans_three("105"), "ONE HUNDRED AND FIVE")

    def test_trans_three_4(self):
        # Hundreds followed by a teen-range remainder uses the dedicated teen word
        self.assertEqual(self.formatter.trans_three("110"), "ONE HUNDRED AND TEN")

    def test_trans_three_5(self):
        # Different hundreds digit with a tens-and-units remainder
        self.assertEqual(self.formatter.trans_three("342"), "THREE HUNDRED AND FORTY TWO")

import unittest

class AgentTest_parse_more(unittest.TestCase):

    def setUp(self):
        self.formatter = NumberWordFormatter()

    def test_parse_more_1(self):
        # Docstring example: index 1 is the thousand magnitude
        self.assertEqual(self.formatter.parse_more(1), "THOUSAND")

    def test_parse_more_2(self):
        # Index 2 is the million magnitude
        self.assertEqual(self.formatter.parse_more(2), "MILLION")

    def test_parse_more_3(self):
        # Index 3 is the billion magnitude
        self.assertEqual(self.formatter.parse_more(3), "BILLION")

    def test_parse_more_4(self):
        # Index 0 is the base magnitude, which has no suffix word
        self.assertEqual(self.formatter.parse_more(0), "")

    def test_parse_more_5(self):
        # The suffix for a magnitude is returned as a string
        self.assertIsInstance(self.formatter.parse_more(1), str)

import unittest

class AgentTest_format_string(unittest.TestCase):

    def setUp(self):
        self.formatter = NumberWordFormatter()

    def test_format_string_1(self):
        # Docstring example: a digit string is converted to the same words as the number
        self.assertEqual(
            self.formatter.format_string("123456"),
            "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        )

    def test_format_string_2(self):
        # The result is returned as a string
        self.assertIsInstance(self.formatter.format_string("123456"), str)

    def test_format_string_3(self):
        # Two-digit string uses the tens word followed by the units word
        self.assertEqual(self.formatter.format_string("23"), "TWENTY THREE ONLY")

    def test_format_string_4(self):
        # Three-digit string with a units-only remainder keeps the hundreds connector
        self.assertEqual(self.formatter.format_string("105"), "ONE HUNDRED AND FIVE ONLY")

    def test_format_string_5(self):
        # Seven-digit string uses the million magnitude word
        self.assertEqual(self.formatter.format_string("1000000"), "ONE MILLION ONLY")

import unittest

class AgentTest_format(unittest.TestCase):

    def setUp(self):
        self.formatter = NumberWordFormatter()

    def test_format_1(self):
        # Docstring example: integer input is converted to words ending in ONLY
        self.assertEqual(
            self.formatter.format(123456),
            "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        )

    def test_format_2(self):
        # The result is returned as a string
        self.assertIsInstance(self.formatter.format(123456), str)

    def test_format_3(self):
        # Two-digit integer uses the tens word followed by the units word
        self.assertEqual(self.formatter.format(23), "TWENTY THREE ONLY")

    def test_format_4(self):
        # Three-digit integer with a units-only remainder keeps the hundreds connector
        self.assertEqual(self.formatter.format(105), "ONE HUNDRED AND FIVE ONLY")

    def test_format_5(self):
        # Float input: the integer part is converted to the same leading words
        result = self.formatter.format(123456.0)
        self.assertIsInstance(result, str)
        self.assertTrue(
            result.startswith("ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX")
        )