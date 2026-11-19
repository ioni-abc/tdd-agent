import unittest


import unittest

class AgentTest_text2int(unittest.TestCase):

    def setUp(self):
        self.w2n = Words2Numbers()

    def test_text2int_1(self):
        # Docstring example: hyphenated compound number
        self.assertEqual(self.w2n.text2int("thirty-two"), "32")

    def test_text2int_2(self):
        # Single unit word converts to its digit string
        self.assertEqual(self.w2n.text2int("one"), "1")

    def test_text2int_3(self):
        # Teen number from the units list
        self.assertEqual(self.w2n.text2int("fifteen"), "15")

    def test_text2int_4(self):
        # Tens word on its own
        self.assertEqual(self.w2n.text2int("twenty"), "20")

    def test_text2int_5(self):
        # Result must be a string of the integer, combining hundreds and tens/units
        result = self.w2n.text2int("one hundred twenty-three")
        self.assertIsInstance(result, str)
        self.assertEqual(result, "123")

import unittest

class AgentTest_is_valid_input(unittest.TestCase):

    def setUp(self):
        self.w2n = Words2Numbers()

    def test_is_valid_input_1(self):
        # Docstring example: "thirty-two" is reported as invalid
        self.assertFalse(self.w2n.is_valid_input("thirty-two"))

    def test_is_valid_input_2(self):
        # A single unit word is composed only of valid number words
        self.assertTrue(self.w2n.is_valid_input("one"))

    def test_is_valid_input_3(self):
        # A tens word followed by a unit word, both valid number words
        self.assertTrue(self.w2n.is_valid_input("twenty three"))

    def test_is_valid_input_4(self):
        # Scale words and the "and" connector are part of the valid vocabulary
        self.assertTrue(self.w2n.is_valid_input("one hundred and five"))

    def test_is_valid_input_5(self):
        # Text containing a word that cannot be converted into a number is invalid
        self.assertFalse(self.w2n.is_valid_input("one banana"))