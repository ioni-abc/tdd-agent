import unittest



class BinaryDataProcessorTestCleanNonBinaryChars(unittest.TestCase):
    def test_clean_non_binary_chars(self):
        bdp = BinaryDataProcessor("01101000daf3e4r01100101011011000110110001101111")
        self.assertEqual(bdp.binary_string, "0110100001100101011011000110110001101111")

    def test_clean_non_binary_chars_2(self):
        bdp = BinaryDataProcessor("01101000daf3e4r01100101011011addf0110001d1111")
        self.assertEqual(bdp.binary_string, "011010000110010101101101100011111")

    def test_clean_non_binary_chars_3(self):
        bdp = BinaryDataProcessor("0sd1000daf3e4r01100101011011addf0110001d1111")
        self.assertEqual(bdp.binary_string, "010000110010101101101100011111")

import unittest

class AgentTest_clean_non_binary_chars(unittest.TestCase):
    def test_clean_non_binary_chars_1(self):
        bdp = BinaryDataProcessor("Hello 0110 World\n1001!")
        self.assertEqual(bdp.binary_string, "01101001")

    def test_clean_non_binary_chars_2(self):
        bdp = BinaryDataProcessor("xyzABC?!")
        self.assertEqual(bdp.binary_string, "")

class BinaryDataProcessorTestCalculateBinaryInfo(unittest.TestCase):
    def test_calculate_binary_info(self):
        bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        self.assertEqual(bdp.calculate_binary_info(), {'Zeroes': 0.475, 'Ones': 0.525, 'Bit length': 40})

    def test_calculate_binary_info_2(self):
        bdp = BinaryDataProcessor("0110100001100101011010011111")
        self.assertEqual(bdp.calculate_binary_info(), {'Bit length': 28, 'Ones': 0.5357142857142857, 'Zeroes': 0.4642857142857143})

    def test_calculate_binary_info_3(self):
        bdp = BinaryDataProcessor("01101001111100101011010011111")
        self.assertEqual(bdp.calculate_binary_info(), {'Bit length': 29, 'Ones': 0.6206896551724138, 'Zeroes': 0.3793103448275862})

import unittest

class AgentTest_calculate_binary_info(unittest.TestCase):
    def test_calculate_binary_info_1(self):
        bdp = BinaryDataProcessor("0000")
        self.assertEqual(bdp.calculate_binary_info(), {'Zeroes': 1.0, 'Ones': 0.0, 'Bit length': 4})

    def test_calculate_binary_info_2(self):
        bdp = BinaryDataProcessor("ab1c1d1e0")
        self.assertEqual(bdp.calculate_binary_info(), {'Zeroes': 0.25, 'Ones': 0.75, 'Bit length': 4})

class BinaryDataProcessorTestConvertToAscii(unittest.TestCase):
    def test_convert_to_ascii(self):
        bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        self.assertEqual(bdp.convert_to_ascii(), "hello")

    def test_convert_to_ascii_2(self):
        bdp = BinaryDataProcessor("0110100000100101011011000110110001101111")
        self.assertEqual(bdp.convert_to_ascii(), "h%llo")

    def test_convert_to_ascii_3(self):
        bdp = BinaryDataProcessor("01101000011011010110001001101111")
        self.assertEqual(bdp.convert_to_ascii(), "hmbo")

import unittest

class AgentTest_convert_to_ascii(unittest.TestCase):
    def test_convert_to_ascii_1(self):
        bdp = BinaryDataProcessor("0100100001001001")
        self.assertEqual(bdp.convert_to_ascii(), "HI")

    def test_convert_to_ascii_2(self):
        bdp = BinaryDataProcessor("010100000111100101110100011010000110111101101110")
        self.assertEqual(bdp.convert_to_ascii(), "Python")

class BinaryDataProcessorTestConvertToUtf8(unittest.TestCase):
    def test_convert_to_utf8(self):
        bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        self.assertEqual(bdp.convert_to_utf8(), "hello")

    def test_convert_to_utf8_2(self):
        bdp = BinaryDataProcessor("0110100001100101011011000110110001101001")
        self.assertEqual(bdp.convert_to_utf8(), "helli")

    def test_convert_to_utf8_3(self):
        bdp = BinaryDataProcessor("0110000001100101011011000110110001101111")
        self.assertEqual(bdp.convert_to_utf8(), "`ello")

import unittest

class AgentTest_convert_to_utf8(unittest.TestCase):
    def test_convert_to_utf8_1(self):
        # "é" (U+00E9) is encoded in UTF-8 as two bytes: 0xC3 0xA9
        bdp = BinaryDataProcessor("1100001110101001")
        self.assertEqual(bdp.convert_to_utf8(), "é")

    def test_convert_to_utf8_2(self):
        # "h" followed by "€" (U+20AC), which is encoded in UTF-8 as three bytes: 0xE2 0x82 0xAC
        bdp = BinaryDataProcessor("01101000111000101000001010101100")
        self.assertEqual(bdp.convert_to_utf8(), "h€")