import unittest




class NumberConverterTestDecimalToBinary(unittest.TestCase):
    def test_decimal_to_binary(self):
        self.assertEqual('1010010110110111', NumberConverter.decimal_to_binary(42423))

    def test_decimal_to_binary_2(self):
        self.assertEqual('101001100010111', NumberConverter.decimal_to_binary(21271))

    def test_decimal_to_binary_3(self):
        self.assertEqual('1010010111010111', NumberConverter.decimal_to_binary(42455))

import unittest

class AgentTest_decimal_to_binary(unittest.TestCase):
    def test_decimal_to_binary_1(self):
        self.assertEqual('0', NumberConverter.decimal_to_binary(0))

    def test_decimal_to_binary_2(self):
        self.assertEqual('10000000000', NumberConverter.decimal_to_binary(1024))

class NumberConverterTestBinaryToDecimal(unittest.TestCase):
    def test_binary_to_decimal(self):
        self.assertEqual(42423, NumberConverter.binary_to_decimal('1010010110110111'))

    def test_binary_to_decimal_2(self):
        self.assertEqual(10615, NumberConverter.binary_to_decimal('10100101110111'))

    def test_binary_to_decimal_3(self):
        self.assertEqual(42455, NumberConverter.binary_to_decimal('1010010111010111'))

import unittest

class AgentTest_binary_to_decimal(unittest.TestCase):
    def test_binary_to_decimal_1(self):
        self.assertEqual(0, NumberConverter.binary_to_decimal('0'))

    def test_binary_to_decimal_2(self):
        self.assertEqual(1024, NumberConverter.binary_to_decimal('10000000000'))

class NumberConvertTestDecimalToOctal(unittest.TestCase):
    def test_decimal_to_octal(self):
        self.assertEqual('122667', NumberConverter.decimal_to_octal(42423))

    def test_decimal_to_octal_2(self):
        self.assertEqual('51427', NumberConverter.decimal_to_octal(21271))

    def test_decimal_to_octal_3(self):
        self.assertEqual('245653', NumberConverter.decimal_to_octal(84907))

import unittest

class AgentTest_decimal_to_octal(unittest.TestCase):
    def test_decimal_to_octal_1(self):
        self.assertEqual('0', NumberConverter.decimal_to_octal(0))

    def test_decimal_to_octal_2(self):
        self.assertEqual('10', NumberConverter.decimal_to_octal(8))

class NumberConvertTestOctalToDecimal(unittest.TestCase):
    def test_octal_to_decimal(self):
        self.assertEqual(42423, NumberConverter.octal_to_decimal('122667'))

    def test_octal_to_decimal_2(self):
        self.assertEqual(21271, NumberConverter.octal_to_decimal('51427'))

    def test_octal_to_decimal_3(self):
        self.assertEqual(84907, NumberConverter.octal_to_decimal('245653'))

import unittest

class AgentTest_octal_to_decimal(unittest.TestCase):
    def test_octal_to_decimal_1(self):
        self.assertEqual(0, NumberConverter.octal_to_decimal('0'))

    def test_octal_to_decimal_2(self):
        self.assertEqual(511, NumberConverter.octal_to_decimal('777'))

class NumberConvertTestDecimalToHex(unittest.TestCase):
    def test_decimal_to_hex(self):
        self.assertEqual('a5b7', NumberConverter.decimal_to_hex(42423))

    def test_decimal_to_hex_2(self):
        self.assertEqual('5317', NumberConverter.decimal_to_hex(21271))

    def test_decimal_to_hex_3(self):
        self.assertEqual('14bab', NumberConverter.decimal_to_hex(84907))

import unittest

class AgentTest_decimal_to_hex(unittest.TestCase):
    def test_decimal_to_hex_1(self):
        self.assertEqual('0', NumberConverter.decimal_to_hex(0))

    def test_decimal_to_hex_2(self):
        self.assertEqual('ff', NumberConverter.decimal_to_hex(255))

class NumberConvertTestHexToDecimal(unittest.TestCase):
    def test_hex_to_decimal(self):
        self.assertEqual(42423, NumberConverter.hex_to_decimal('a5b7'))

    def test_hex_to_decimal_2(self):
        self.assertEqual(21207, NumberConverter.hex_to_decimal('52d7'))

    def test_hex_to_decimal_3(self):
        self.assertEqual(84627, NumberConverter.hex_to_decimal('14a93'))

class AgentTest_hex_to_decimal(unittest.TestCase):
    def test_hex_to_decimal_1(self):
        self.assertEqual(0, NumberConverter.hex_to_decimal('0'))

    def test_hex_to_decimal_2(self):
        self.assertEqual(255, NumberConverter.hex_to_decimal('ff'))