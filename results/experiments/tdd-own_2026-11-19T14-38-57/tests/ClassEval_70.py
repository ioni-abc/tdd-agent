import unittest


import unittest

class AgentTest__validate_name(unittest.TestCase):

    def setUp(self):
        # Valid sex and phone number so construction is not affected by other validators.
        self.person = PersonRequest("John Smith", "Man", "12345678901")

    def test__validate_name_1(self):
        # A valid, non-empty name within 33 characters is returned unchanged.
        self.assertEqual(self.person._validate_name("John Smith"), "John Smith")

    def test__validate_name_2(self):
        # An empty name is invalid and must be set to None.
        self.assertIsNone(self.person._validate_name(""))

    def test__validate_name_3(self):
        # A name of exactly 33 characters is the maximum allowed length and is returned unchanged.
        name = "A" * 33
        self.assertEqual(self.person._validate_name(name), name)

    def test__validate_name_4(self):
        # A name of 34 characters exceeds the 33-character limit and must be set to None.
        name = "A" * 34
        self.assertIsNone(self.person._validate_name(name))

    def test__validate_name_5(self):
        # A single-character non-empty name is valid and returned unchanged.
        self.assertEqual(self.person._validate_name("A"), "A")

import unittest

class AgentTest__validate_sex(unittest.TestCase):

    def setUp(self):
        # Valid name and phone number so construction is not affected by other validators.
        self.person = PersonRequest("John Smith", "Man", "12345678901")

    def test__validate_sex_1(self):
        # "Man" is one of the allowed sex values and is returned unchanged.
        self.assertEqual(self.person._validate_sex("Man"), "Man")

    def test__validate_sex_2(self):
        # "Woman" is one of the allowed sex values and is returned unchanged.
        self.assertEqual(self.person._validate_sex("Woman"), "Woman")

    def test__validate_sex_3(self):
        # "UGM" is one of the allowed sex values and is returned unchanged.
        self.assertEqual(self.person._validate_sex("UGM"), "UGM")

    def test__validate_sex_4(self):
        # A value that is not Man, Woman, or UGM is invalid and must be set to None.
        self.assertIsNone(self.person._validate_sex("Other"))

    def test__validate_sex_5(self):
        # An empty string is not Man, Woman, or UGM and must be set to None.
        self.assertIsNone(self.person._validate_sex(""))

import unittest

class AgentTest__validate_phoneNumber(unittest.TestCase):

    def setUp(self):
        # Valid name and sex so construction is not affected by other validators.
        self.person = PersonRequest("John Smith", "Man", "12345678901")

    def test__validate_phoneNumber_1(self):
        # A valid 11-digit phone number is returned unchanged.
        self.assertEqual(self.person._validate_phoneNumber("12345678901"), "12345678901")

    def test__validate_phoneNumber_2(self):
        # An empty phone number is invalid and must be set to None.
        self.assertIsNone(self.person._validate_phoneNumber(""))

    def test__validate_phoneNumber_3(self):
        # A 10-digit number is not an 11 digit number and must be set to None.
        self.assertIsNone(self.person._validate_phoneNumber("1234567890"))

    def test__validate_phoneNumber_4(self):
        # A 12-digit number is not an 11 digit number and must be set to None.
        self.assertIsNone(self.person._validate_phoneNumber("123456789012"))

    def test__validate_phoneNumber_5(self):
        # A string of 11 characters that contains non-digit characters is not an 11 digit number and must be set to None.
        self.assertIsNone(self.person._validate_phoneNumber("1234567890a"))