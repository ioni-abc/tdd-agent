import unittest


import unittest

class AgentTest_decimal_to_binary(unittest.TestCase):

    def test_decimal_to_binary_1(self):
        self.assertEqual(NumberConverter.decimal_to_binary(42423), '1010010110110111')

    def test_decimal_to_binary_2(self):
        self.assertEqual(NumberConverter.decimal_to_binary(0), '0')

    def test_decimal_to_binary_3(self):
        self.assertEqual(NumberConverter.decimal_to_binary(1), '1')

    def test_decimal_to_binary_4(self):
        self.assertEqual(NumberConverter.decimal_to_binary(10), '1010')

    def test_decimal_to_binary_5(self):
        result = NumberConverter.decimal_to_binary(255)
        self.assertIsInstance(result, str)
        self.assertEqual(result, '11111111')

class AgentTest_binary_to_decimal(unittest.TestCase):

    def test_binary_to_decimal_1(self):
        self.assertEqual(NumberConverter.binary_to_decimal('1010010110110111'), 42423)

    def test_binary_to_decimal_2(self):
        self.assertEqual(NumberConverter.binary_to_decimal('0'), 0)

    def test_binary_to_decimal_3(self):
        self.assertEqual(NumberConverter.binary_to_decimal('1'), 1)

    def test_binary_to_decimal_4(self):
        self.assertEqual(NumberConverter.binary_to_decimal('1010'), 10)

    def test_binary_to_decimal_5(self):
        result = NumberConverter.binary_to_decimal('11111111')
        self.assertIsInstance(result, int)
        self.assertEqual(result, 255)

class AgentTest_decimal_to_octal(unittest.TestCase):

    def test_decimal_to_octal_1(self):
        self.assertEqual(NumberConverter.decimal_to_octal(42423), '122667')

    def test_decimal_to_octal_2(self):
        self.assertEqual(NumberConverter.decimal_to_octal(0), '0')

    def test_decimal_to_octal_3(self):
        self.assertEqual(NumberConverter.decimal_to_octal(1), '1')

    def test_decimal_to_octal_4(self):
        self.assertEqual(NumberConverter.decimal_to_octal(8), '10')

    def test_decimal_to_octal_5(self):
        result = NumberConverter.decimal_to_octal(255)
        self.assertIsInstance(result, str)
        self.assertEqual(result, '377')

import unittest

class AgentTest_octal_to_decimal(unittest.TestCase):

    def test_octal_to_decimal_1(self):
        self.assertEqual(NumberConverter.octal_to_decimal('122667'), 42423)

    def test_octal_to_decimal_2(self):
        self.assertEqual(NumberConverter.octal_to_decimal('0'), 0)

    def test_octal_to_decimal_3(self):
        self.assertEqual(NumberConverter.octal_to_decimal('1'), 1)

    def test_octal_to_decimal_4(self):
        self.assertEqual(NumberConverter.octal_to_decimal('10'), 8)

    def test_octal_to_decimal_5(self):
        result = NumberConverter.octal_to_decimal('377')
        self.assertIsInstance(result, int)
        self.assertEqual(result, 255)

import unittest

class AgentTest_decimal_to_hex(unittest.TestCase):

    def test_decimal_to_hex_1(self):
        self.assertEqual(NumberConverter.decimal_to_hex(42423), 'a5b7')

    def test_decimal_to_hex_2(self):
        self.assertEqual(NumberConverter.decimal_to_hex(0), '0')

    def test_decimal_to_hex_3(self):
        self.assertEqual(NumberConverter.decimal_to_hex(10), 'a')

    def test_decimal_to_hex_4(self):
        self.assertEqual(NumberConverter.decimal_to_hex(16), '10')

    def test_decimal_to_hex_5(self):
        result = NumberConverter.decimal_to_hex(255)
        self.assertIsInstance(result, str)
        self.assertEqual(result, 'ff')

import unittest

class AgentTest_hex_to_decimal(unittest.TestCase):

    def test_hex_to_decimal_1(self):
        self.assertEqual(NumberConverter.hex_to_decimal('a5b7'), 42423)

    def test_hex_to_decimal_2(self):
        self.assertEqual(NumberConverter.hex_to_decimal('0'), 0)

    def test_hex_to_decimal_3(self):
        self.assertEqual(NumberConverter.hex_to_decimal('a'), 10)

    def test_hex_to_decimal_4(self):
        self.assertEqual(NumberConverter.hex_to_decimal('10'), 16)

    def test_hex_to_decimal_5(self):
        result = NumberConverter.hex_to_decimal('ff')
        self.assertIsInstance(result, int)
        self.assertEqual(result, 255)