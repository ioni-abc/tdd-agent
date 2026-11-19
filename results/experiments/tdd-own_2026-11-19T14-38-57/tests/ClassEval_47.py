import unittest


import unittest

class AgentTest_is_valid(unittest.TestCase):

    def test_is_valid_1(self):
        ipaddress = IPAddress("10.10.10.10")
        self.assertTrue(ipaddress.is_valid())

    def test_is_valid_2(self):
        self.assertTrue(IPAddress("0.0.0.0").is_valid())
        self.assertTrue(IPAddress("255.255.255.255").is_valid())

    def test_is_valid_3(self):
        self.assertFalse(IPAddress("256.10.10.10").is_valid())
        self.assertFalse(IPAddress("10.10.10.256").is_valid())

    def test_is_valid_4(self):
        self.assertFalse(IPAddress("10.10.10").is_valid())
        self.assertFalse(IPAddress("10.10.10.10.10").is_valid())

    def test_is_valid_5(self):
        self.assertFalse(IPAddress("10.10.10.a").is_valid())
        self.assertFalse(IPAddress("10,10,10,10").is_valid())

import unittest

class AgentTest_get_octets(unittest.TestCase):

    def test_get_octets_1(self):
        ipaddress = IPAddress("10.10.10.10")
        self.assertEqual(ipaddress.get_octets(), ["10", "10", "10", "10"])

    def test_get_octets_2(self):
        self.assertEqual(IPAddress("0.0.0.0").get_octets(), ["0", "0", "0", "0"])
        self.assertEqual(IPAddress("255.255.255.255").get_octets(), ["255", "255", "255", "255"])

    def test_get_octets_3(self):
        self.assertEqual(IPAddress("192.168.1.254").get_octets(), ["192", "168", "1", "254"])

    def test_get_octets_4(self):
        self.assertEqual(IPAddress("256.10.10.10").get_octets(), [])
        self.assertEqual(IPAddress("10.10.10.256").get_octets(), [])

    def test_get_octets_5(self):
        self.assertEqual(IPAddress("10.10.10").get_octets(), [])
        self.assertEqual(IPAddress("10.10.10.a").get_octets(), [])
        self.assertEqual(IPAddress("10,10,10,10").get_octets(), [])

import unittest

class AgentTest_get_binary(unittest.TestCase):

    def test_get_binary_1(self):
        ipaddress = IPAddress("10.10.10.10")
        self.assertEqual(ipaddress.get_binary(), "00001010.00001010.00001010.00001010")

    def test_get_binary_2(self):
        self.assertEqual(IPAddress("0.0.0.0").get_binary(), "00000000.00000000.00000000.00000000")
        self.assertEqual(IPAddress("255.255.255.255").get_binary(), "11111111.11111111.11111111.11111111")

    def test_get_binary_3(self):
        self.assertEqual(IPAddress("192.168.1.254").get_binary(), "11000000.10101000.00000001.11111110")

    def test_get_binary_4(self):
        self.assertEqual(IPAddress("256.10.10.10").get_binary(), "")
        self.assertEqual(IPAddress("10.10.10.256").get_binary(), "")

    def test_get_binary_5(self):
        self.assertEqual(IPAddress("10.10.10").get_binary(), "")
        self.assertEqual(IPAddress("10.10.10.10.10").get_binary(), "")
        self.assertEqual(IPAddress("10.10.10.a").get_binary(), "")
        self.assertEqual(IPAddress("10,10,10,10").get_binary(), "")