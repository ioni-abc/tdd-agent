import unittest


import unittest

class AgentTest_add(unittest.TestCase):

    def test_add_1(self):
        result = BigNumCalculator.add("12345678901234567890", "98765432109876543210")
        self.assertEqual(result, "111111111011111111100")

    def test_add_2(self):
        result = BigNumCalculator.add("12345678901234567890", "98765432109876543210")
        self.assertIsInstance(result, str)

    def test_add_3(self):
        self.assertEqual(BigNumCalculator.add("2", "3"), "5")

    def test_add_4(self):
        self.assertEqual(BigNumCalculator.add("999", "1"), "1000")

    def test_add_5(self):
        self.assertEqual(
            BigNumCalculator.add("0", "12345678901234567890"),
            "12345678901234567890",
        )

import unittest

class AgentTest_subtract(unittest.TestCase):

    def test_subtract_1(self):
        result = BigNumCalculator.subtract("12345678901234567890", "98765432109876543210")
        self.assertEqual(result, "-86419753208641975320")

    def test_subtract_2(self):
        result = BigNumCalculator.subtract("12345678901234567890", "98765432109876543210")
        self.assertIsInstance(result, str)

    def test_subtract_3(self):
        self.assertEqual(BigNumCalculator.subtract("5", "3"), "2")

    def test_subtract_4(self):
        self.assertEqual(BigNumCalculator.subtract("1000", "1"), "999")

    def test_subtract_5(self):
        self.assertEqual(
            BigNumCalculator.subtract("12345678901234567890", "12345678901234567890"),
            "0",
        )

import unittest

class AgentTest_multiply(unittest.TestCase):

    def test_multiply_1(self):
        result = BigNumCalculator.multiply("12345678901234567890", "98765432109876543210")
        self.assertEqual(result, "1219326311370217952237463801111263526900")

    def test_multiply_2(self):
        result = BigNumCalculator.multiply("12345678901234567890", "98765432109876543210")
        self.assertIsInstance(result, str)

    def test_multiply_3(self):
        self.assertEqual(BigNumCalculator.multiply("2", "3"), "6")

    def test_multiply_4(self):
        self.assertEqual(
            BigNumCalculator.multiply("12345678901234567890", "1"),
            "12345678901234567890",
        )

    def test_multiply_5(self):
        num = "9" * 20
        expected = "9" * 19 + "8" + "0" * 19 + "1"
        self.assertEqual(BigNumCalculator.multiply(num, num), expected)