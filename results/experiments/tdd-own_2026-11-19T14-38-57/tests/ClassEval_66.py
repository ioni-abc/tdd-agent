import unittest


import unittest

class AgentTest_is_hex_char(unittest.TestCase):

    def test_is_hex_char_1(self):
        # Docstring example: 'a' is a hexadecimal digit.
        self.assertIs(NumericEntityUnescaper.is_hex_char('a'), True)

    def test_is_hex_char_2(self):
        # Every decimal digit is a hexadecimal digit.
        for char in "0123456789":
            with self.subTest(char=char):
                self.assertIs(NumericEntityUnescaper.is_hex_char(char), True)

    def test_is_hex_char_3(self):
        # Hexadecimal digits include the letters a-f in both cases.
        for char in "abcdefABCDEF":
            with self.subTest(char=char):
                self.assertIs(NumericEntityUnescaper.is_hex_char(char), True)

    def test_is_hex_char_4(self):
        # Letters outside a-f (in either case) are not hexadecimal digits.
        for char in "ghijklmnopqrstuvwxyzGHIJKLMNOPQRSTUVWXYZ":
            with self.subTest(char=char):
                self.assertIs(NumericEntityUnescaper.is_hex_char(char), False)

    def test_is_hex_char_5(self):
        # Non-alphanumeric characters, including those adjacent to the digit
        # and letter ranges, are not hexadecimal digits.
        for char in " /:@`[{;&#.-+":
            with self.subTest(char=char):
                self.assertIs(NumericEntityUnescaper.is_hex_char(char), False)

import unittest

class AgentTest_replace(unittest.TestCase):

    def test_replace_1(self):
        # Docstring example: decimal numeric references are replaced by their characters.
        unescaper = NumericEntityUnescaper()
        self.assertEqual(unescaper.replace("&#65;&#66;&#67;"), 'ABC')

    def test_replace_2(self):
        # A string containing no numeric character references is returned unchanged.
        unescaper = NumericEntityUnescaper()
        text = "Plain text with no references, just punctuation!"
        self.assertEqual(unescaper.replace(text), text)

    def test_replace_3(self):
        # References embedded within surrounding text are replaced in place,
        # and the surrounding text is preserved.
        unescaper = NumericEntityUnescaper()
        self.assertEqual(unescaper.replace("Hello &#87;orld"), 'Hello World')

    def test_replace_4(self):
        # Hexadecimal numeric character references are also replaced by their characters.
        unescaper = NumericEntityUnescaper()
        self.assertEqual(unescaper.replace("&#x41;&#x42;&#x43;"), 'ABC')

    def test_replace_5(self):
        # Code points beyond ASCII (e.g. 233 is 'é') are replaced by their Unicode characters.
        unescaper = NumericEntityUnescaper()
        self.assertEqual(unescaper.replace("caf&#233;"), 'caf\u00e9')