import unittest




class NumericEntityUnescaperTestIsHexChar(unittest.TestCase):
    def test_is_hex_char_1(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.is_hex_char('0')
        self.assertEqual(res, True)

    def test_is_hex_char_2(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.is_hex_char('F')
        self.assertEqual(res, True)

    def test_is_hex_char_3(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.is_hex_char('G')
        self.assertEqual(res, False)

import unittest

class AgentTest_is_hex_char(unittest.TestCase):
    def test_is_hex_char_1(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.is_hex_char('a')
        self.assertEqual(res, True)

    def test_is_hex_char_2(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.is_hex_char('z')
        self.assertEqual(res, False)

class NumericEntityUnescaperTestReplace(unittest.TestCase):
    def test_replace_1(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.replace("&#65;&#66;&#67;")
        self.assertEqual(res, "ABC")

    def test_replace_2(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.replace("&#65;&#65;&#65;")
        self.assertEqual(res, "AAA")

    def test_replace_3(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.replace("&#66;&#66;&#66;")
        self.assertEqual(res, "BBB")

    def test_replace_4(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.replace("&#67;&#67;&#67;")
        self.assertEqual(res, "CCC")

    def test_replace_5(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.replace("")
        self.assertEqual(res, "")

    def test_replace_6(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.replace("&#")
        self.assertEqual(res, "")

    def test_replace_7(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.replace("&#X65;&#66;&#67;")
        self.assertEqual(res, "eBC")

class AgentTest_replace(unittest.TestCase):
    def test_replace_1(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.replace("Hello, world!")
        self.assertEqual(res, "Hello, world!")

    def test_replace_2(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.replace("Hi &#65;!")
        self.assertEqual(res, "Hi A!")

    def test_replace_3(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.replace("&#8364;")
        self.assertEqual(res, "\u20ac")

    def test_replace_4(self):
        unescaper = NumericEntityUnescaper()
        res = unescaper.replace("&#x41;&#x42;")
        self.assertEqual(res, "AB")