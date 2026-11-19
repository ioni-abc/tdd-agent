import unittest



class BigNumCalculatorTestAdd(unittest.TestCase):
    def test_add(self):
        bigNum = BigNumCalculator()
        self.assertEqual(bigNum.add("12345678901234567890", "98765432109876543210"), "111111111011111111100")

    def test_add_2(self):
        bigNum = BigNumCalculator()
        self.assertEqual(bigNum.add("123456789012345678922", "98765432109876543210"), "222222221122222222132")

    def test_add_3(self):
        bigNum = BigNumCalculator()
        self.assertEqual(bigNum.add("123456789012345678934", "98765432109876543210"), "222222221122222222144")

import unittest

class AgentTest_add(unittest.TestCase):
    def test_add_1(self):
        bigNum = BigNumCalculator()
        self.assertEqual(bigNum.add("0", "0"), "0")

    def test_add_2(self):
        bigNum = BigNumCalculator()
        self.assertEqual(bigNum.add("999999999999999999999", "1"), "1000000000000000000000")

class BigNumCalculatorTestSubtract(unittest.TestCase):
    def test_subtract(self):
        bigNum = BigNumCalculator()
        self.assertEqual(bigNum.subtract("12345678901234567890", "98765432109876543210"), "-86419753208641975320")

    def test_subtract_2(self):
        bigNum = BigNumCalculator()
        self.assertEqual(bigNum.subtract("123456789012345678922", "98765432109876543210"), "24691356902469135712")

    def test_subtract_3(self):
        bigNum = BigNumCalculator()
        self.assertEqual(bigNum.subtract("123456789012345678934", "98765432109876543"), "123358023580235802391")

class AgentTest_subtract(unittest.TestCase):
    def test_subtract_1(self):
        bigNum = BigNumCalculator()
        self.assertEqual(bigNum.subtract("12345678901234567890", "12345678901234567890"), "0")

    def test_subtract_2(self):
        bigNum = BigNumCalculator()
        self.assertEqual(bigNum.subtract("1000000000000000000000", "1"), "999999999999999999999")

class BigNumCalculatorTestMultiply(unittest.TestCase):
    def test_multiply(self):
        bigNum = BigNumCalculator()
        self.assertEqual(bigNum.multiply("12345678901234567890", "98765432109876543210"), "1219326311370217952237463801111263526900")

    def test_multiply_2(self):
        bigNum = BigNumCalculator()
        self.assertEqual(bigNum.multiply("123456789012345678922", "98765432109876543210"), "12193263113702179524547477517529919219620")

    def test_multiply_3(self):
        bigNum = BigNumCalculator()
        self.assertEqual(bigNum.multiply("123456789012345678934", "98765432109876543"), "12193263113702179499806737010255845162")

    def test_multiply_4(self):
        bigNum = BigNumCalculator()
        self.assertEqual(bigNum.multiply("12345678901234567", "98765432109876543210"), "1219326311370217864336229223321140070")

import unittest

class AgentTest_multiply(unittest.TestCase):
    def test_multiply_1(self):
        bigNum = BigNumCalculator()
        self.assertEqual(bigNum.multiply("0", "98765432109876543210"), "0")

    def test_multiply_2(self):
        bigNum = BigNumCalculator()
        self.assertEqual(bigNum.multiply("1000000000000000000000", "12345"), "12345" + "0" * 21)