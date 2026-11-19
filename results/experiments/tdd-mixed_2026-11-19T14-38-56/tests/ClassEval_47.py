import unittest




class IPAddressTestIsValid(unittest.TestCase):
    def test_is_valid_1(self):
        ipaddress = IPAddress("10.10.10.10")
        self.assertEqual(ipaddress.is_valid(), True)

    def test_is_valid_2(self):
        ipaddress = IPAddress("-1.10.10.10")
        self.assertEqual(ipaddress.is_valid(), False)

    def test_is_valid_3(self):
        ipaddress = IPAddress("10.10.10")
        self.assertEqual(ipaddress.is_valid(), False)

import unittest

class AgentTest_is_valid(unittest.TestCase):
    def test_is_valid_1(self):
        ipaddress = IPAddress("256.10.10.10")
        self.assertEqual(ipaddress.is_valid(), False)

    def test_is_valid_2(self):
        self.assertEqual(IPAddress("0.0.0.0").is_valid(), True)
        self.assertEqual(IPAddress("255.255.255.255").is_valid(), True)

class IPAddressTestGetOctets(unittest.TestCase):
    def test_get_octets_1(self):
        ipaddress = IPAddress("10.10.10.10")
        self.assertEqual(ipaddress.get_octets(), ["10", "10", "10", "10"])

    def test_get_octets_2(self):
        ipaddress = IPAddress("a.10.10.10")
        self.assertEqual(ipaddress.get_octets(), [])

    def test_get_octets_3(self):
        ipaddress = IPAddress("-1.10.10.10")
        self.assertEqual(ipaddress.get_octets(), [])

class AgentTest_get_octets(unittest.TestCase):
    def test_get_octets_1(self):
        ipaddress = IPAddress("0.0.0.0")
        self.assertEqual(ipaddress.get_octets(), ["0", "0", "0", "0"])

    def test_get_octets_2(self):
        ipaddress = IPAddress("256.10.10.10")
        self.assertEqual(ipaddress.get_octets(), [])

class IPAddressTestGetBinary(unittest.TestCase):
    def test_get_binary_1(self):
        ipaddress = IPAddress("10.10.10.10")
        self.assertEqual(ipaddress.get_binary(), "00001010.00001010.00001010.00001010")

    def test_get_binary_2(self):
        ipaddress = IPAddress("a.10.10.10")
        self.assertEqual(ipaddress.get_binary(), '')

    def test_get_binary_3(self):
        ipaddress = IPAddress("-1.10.10.10")
        self.assertEqual(ipaddress.get_binary(), '')

import unittest

class AgentTest_get_binary(unittest.TestCase):
    def test_get_binary_1(self):
        ipaddress = IPAddress("255.255.255.255")
        self.assertEqual(ipaddress.get_binary(), "11111111.11111111.11111111.11111111")

    def test_get_binary_2(self):
        ipaddress = IPAddress("256.10.10.10")
        self.assertEqual(ipaddress.get_binary(), '')