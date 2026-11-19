import unittest


import unittest

class AgentTest_clean_non_binary_chars(unittest.TestCase):

    def test_clean_non_binary_chars_1(self):
        bdp = BinaryDataProcessor("01101000daf3e4r01100101011011000110110001101111")
        bdp.clean_non_binary_chars()
        self.assertEqual(bdp.binary_string, "0110100001100101011011000110110001101111")

    def test_clean_non_binary_chars_2(self):
        bdp = BinaryDataProcessor("01 10\n10\t00")
        bdp.clean_non_binary_chars()
        self.assertEqual(bdp.binary_string, "01101000")

    def test_clean_non_binary_chars_3(self):
        bdp = BinaryDataProcessor("0123456789")
        bdp.clean_non_binary_chars()
        self.assertEqual(bdp.binary_string, "01")

    def test_clean_non_binary_chars_4(self):
        bdp = BinaryDataProcessor("0110100001100101")
        bdp.clean_non_binary_chars()
        self.assertEqual(bdp.binary_string, "0110100001100101")

    def test_clean_non_binary_chars_5(self):
        bdp = BinaryDataProcessor("hello, world!")
        bdp.clean_non_binary_chars()
        self.assertEqual(bdp.binary_string, "")

import unittest

class AgentTest_calculate_binary_info(unittest.TestCase):

    def test_calculate_binary_info_1(self):
        bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        result = bdp.calculate_binary_info()
        self.assertEqual(set(result.keys()), {'Zeroes', 'Ones', 'Bit length'})
        self.assertAlmostEqual(result['Zeroes'], 0.475)
        self.assertAlmostEqual(result['Ones'], 0.525)
        self.assertEqual(result['Bit length'], 40)

    def test_calculate_binary_info_2(self):
        bdp = BinaryDataProcessor("0000")
        result = bdp.calculate_binary_info()
        self.assertAlmostEqual(result['Zeroes'], 1.0)
        self.assertAlmostEqual(result['Ones'], 0.0)
        self.assertEqual(result['Bit length'], 4)

    def test_calculate_binary_info_3(self):
        bdp = BinaryDataProcessor("111")
        result = bdp.calculate_binary_info()
        self.assertAlmostEqual(result['Zeroes'], 0.0)
        self.assertAlmostEqual(result['Ones'], 1.0)
        self.assertEqual(result['Bit length'], 3)

    def test_calculate_binary_info_4(self):
        bdp = BinaryDataProcessor("0101")
        result = bdp.calculate_binary_info()
        self.assertAlmostEqual(result['Zeroes'], 0.5)
        self.assertAlmostEqual(result['Ones'], 0.5)
        self.assertEqual(result['Bit length'], 4)

    def test_calculate_binary_info_5(self):
        bdp = BinaryDataProcessor("0a1b0")
        result = bdp.calculate_binary_info()
        self.assertAlmostEqual(result['Zeroes'], 2 / 3)
        self.assertAlmostEqual(result['Ones'], 1 / 3)
        self.assertEqual(result['Bit length'], 3)

import unittest

class AgentTest_convert_to_ascii(unittest.TestCase):

    def test_convert_to_ascii_1(self):
        bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        self.assertEqual(bdp.convert_to_ascii(), "hello")

    def test_convert_to_ascii_2(self):
        bdp = BinaryDataProcessor("01000001")
        self.assertEqual(bdp.convert_to_ascii(), "A")

    def test_convert_to_ascii_3(self):
        bdp = BinaryDataProcessor("0100100001101001")
        self.assertEqual(bdp.convert_to_ascii(), "Hi")

    def test_convert_to_ascii_4(self):
        bdp = BinaryDataProcessor("00110001 00110010 00110011")
        self.assertEqual(bdp.convert_to_ascii(), "123")

    def test_convert_to_ascii_5(self):
        bdp = BinaryDataProcessor(
            "01101000 01100101 01101100 01101100 01101111 "
            "00100000 01110111 01101111 01110010 01101100 01100100"
        )
        self.assertEqual(bdp.convert_to_ascii(), "hello world")

import unittest

class AgentTest_convert_to_utf8(unittest.TestCase):

    def test_convert_to_utf8_1(self):
        bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        self.assertEqual(bdp.convert_to_utf8(), "hello")

    def test_convert_to_utf8_2(self):
        bdp = BinaryDataProcessor("01000001")
        self.assertEqual(bdp.convert_to_utf8(), "A")

    def test_convert_to_utf8_3(self):
        # "é" (U+00E9) is encoded in UTF-8 as 0xC3 0xA9
        bdp = BinaryDataProcessor("11000011 10101001")
        self.assertEqual(bdp.convert_to_utf8(), "é")

    def test_convert_to_utf8_4(self):
        # "€" (U+20AC) is encoded in UTF-8 as 0xE2 0x82 0xAC
        bdp = BinaryDataProcessor("11100010 10000010 10101100")
        self.assertEqual(bdp.convert_to_utf8(), "€")

    def test_convert_to_utf8_5(self):
        # Non 0/1 characters are cleaned from the input before conversion
        bdp = BinaryDataProcessor("01101000xyz 01100101 0110110001101100 01101111!")
        self.assertEqual(bdp.convert_to_utf8(), "hello")