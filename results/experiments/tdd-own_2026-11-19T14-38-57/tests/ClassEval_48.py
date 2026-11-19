import unittest


import unittest

class AgentTest_is_valid_ipv4(unittest.TestCase):

    def test_is_valid_ipv4_1(self):
        # Example from the docstring: a valid IPv4 address returns True
        self.assertIs(IpUtil.is_valid_ipv4('192.168.0.123'), True)

    def test_is_valid_ipv4_2(self):
        # Example from the docstring: an octet above 255 returns False
        self.assertIs(IpUtil.is_valid_ipv4('256.0.0.0'), False)

    def test_is_valid_ipv4_3(self):
        # Boundary values of the IPv4 range are valid
        self.assertIs(IpUtil.is_valid_ipv4('0.0.0.0'), True)
        self.assertIs(IpUtil.is_valid_ipv4('255.255.255.255'), True)

    def test_is_valid_ipv4_4(self):
        # An IPv6 address is not a valid IPv4 address
        self.assertIs(IpUtil.is_valid_ipv4('2001:0db8:85a3:0000:0000:8a2e:0370:7334'), False)

    def test_is_valid_ipv4_5(self):
        # Strings that are not IPv4 addresses (too few octets, non-numeric) return False
        self.assertIs(IpUtil.is_valid_ipv4('192.168.0'), False)
        self.assertIs(IpUtil.is_valid_ipv4('abc'), False)

import unittest

class AgentTest_is_valid_ipv6(unittest.TestCase):

    def test_is_valid_ipv6_1(self):
        # Example from the docstring: a valid full-form IPv6 address returns True
        self.assertIs(IpUtil.is_valid_ipv6('2001:0db8:85a3:0000:0000:8a2e:0370:7334'), True)

    def test_is_valid_ipv6_2(self):
        # Example from the docstring: malformed colon sequence (':::') returns False
        self.assertIs(IpUtil.is_valid_ipv6('2001:0db8:85a3:::8a2e:0370:7334'), False)

    def test_is_valid_ipv6_3(self):
        # An IPv4 address is not a valid IPv6 address
        self.assertIs(IpUtil.is_valid_ipv6('192.168.0.123'), False)

    def test_is_valid_ipv6_4(self):
        # Strings that are not IP addresses at all return False
        self.assertIs(IpUtil.is_valid_ipv6('abc'), False)
        self.assertIs(IpUtil.is_valid_ipv6(''), False)

    def test_is_valid_ipv6_5(self):
        # Invalid content: a non-hexadecimal character, or too many groups, returns False
        self.assertIs(IpUtil.is_valid_ipv6('2001:0db8:85a3:0000:0000:8a2e:0370:733g'), False)
        self.assertIs(IpUtil.is_valid_ipv6('2001:0db8:85a3:0000:0000:8a2e:0370:7334:1234'), False)

import unittest

class AgentTest_get_hostname(unittest.TestCase):

    def test_get_hostname_1(self):
        # Example from the docstring: 110.242.68.3 resolves to 'www.baidu.com'
        self.assertEqual(IpUtil.get_hostname('110.242.68.3'), 'www.baidu.com')

    def test_get_hostname_2(self):
        # The return value is documented as a string
        self.assertIsInstance(IpUtil.get_hostname('110.242.68.3'), str)

    def test_get_hostname_3(self):
        # The hostname for a known IP address is non-empty
        self.assertGreater(len(IpUtil.get_hostname('110.242.68.3')), 0)

    def test_get_hostname_4(self):
        # Repeated lookups of the same IP address return the same hostname
        first = IpUtil.get_hostname('110.242.68.3')
        second = IpUtil.get_hostname('110.242.68.3')
        self.assertEqual(first, second)

    def test_get_hostname_5(self):
        # A hostname is a single name, so the returned string contains no whitespace
        hostname = IpUtil.get_hostname('110.242.68.3')
        self.assertNotIn(' ', hostname)
        self.assertNotIn('\t', hostname)
        self.assertNotIn('\n', hostname)