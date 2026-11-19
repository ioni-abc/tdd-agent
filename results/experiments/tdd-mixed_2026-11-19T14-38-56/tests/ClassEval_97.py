import unittest




class Words2NumbersTestText2Int(unittest.TestCase):
    def test_text2int(self):
        w2n = Words2Numbers()
        self.assertEqual(w2n.text2int("thirty-two"), "32")

    def test_text2int2(self):
        w2n = Words2Numbers()
        self.assertEqual(w2n.text2int("one hundred and twenty-three"), "123")

    def test_text2int3(self):
        w2n = Words2Numbers()
        self.assertEqual(w2n.text2int("two thousand and nineteen"), "2019")

    def test_text2int4(self):
        w2n = Words2Numbers()
        self.assertEqual(w2n.text2int("one hundred and one"), "101")

import unittest

class AgentTest_text2int(unittest.TestCase):
    def test_text2int_1(self):
        w2n = Words2Numbers()
        self.assertEqual(w2n.text2int("zero"), "0")

    def test_text2int_2(self):
        w2n = Words2Numbers()
        self.assertEqual(w2n.text2int("one million"), "1000000")

class Words2NumbersTestIsValidInput(unittest.TestCase):
    def test_is_valid_input(self):
        w2n = Words2Numbers()
        self.assertTrue(w2n.is_valid_input("twenty-five thousand three hundred and forty-two"))

    def test_is_valid_input2(self):
        w2n = Words2Numbers()
        self.assertTrue(w2n.is_valid_input("second hundred and third"))

    def test_is_valid_input3(self):
        w2n = Words2Numbers()
        self.assertTrue(w2n.is_valid_input("twenty-fifth thousand three hundred and forty-second"))

    def test_is_valid_input4(self):
        w2n = Words2Numbers()
        self.assertFalse(w2n.is_valid_input("eleventy thousand and five"))

import unittest

class AgentTest_is_valid_input(unittest.TestCase):
    def test_is_valid_input_1(self):
        w2n = Words2Numbers()
        self.assertFalse(w2n.is_valid_input("thirty-two"))

    def test_is_valid_input_2(self):
        w2n = Words2Numbers()
        self.assertFalse(w2n.is_valid_input("one banana"))