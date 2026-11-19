import unittest




class ChandrasekharSieveTestGeneratePrimes(unittest.TestCase):
    def test_generate_primes_1(self):
        cs = ChandrasekharSieve(20)
        res = cs.generate_primes()
        self.assertEqual(res, [2, 3, 5, 7, 11, 13, 17, 19])

    def test_generate_primes_2(self):
        cs = ChandrasekharSieve(18)
        res = cs.generate_primes()
        self.assertEqual(res, [2, 3, 5, 7, 11, 13, 17])

    def test_generate_primes_3(self):
        cs = ChandrasekharSieve(15)
        res = cs.generate_primes()
        self.assertEqual(res, [2, 3, 5, 7, 11, 13])

import unittest

class AgentTest_generate_primes(unittest.TestCase):
    def test_generate_primes_1(self):
        cs = ChandrasekharSieve(13)
        res = cs.generate_primes()
        self.assertEqual(res, [2, 3, 5, 7, 11, 13])

    def test_generate_primes_2(self):
        cs = ChandrasekharSieve(1)
        res = cs.generate_primes()
        self.assertEqual(res, [])

class ChandrasekharSieveTestGetPrimes(unittest.TestCase):
    def test_get_primes_1(self):
        cs = ChandrasekharSieve(20)
        cs.generate_primes()
        res = cs.get_primes()
        self.assertEqual(res, [2, 3, 5, 7, 11, 13, 17, 19])

    def test_get_primes_2(self):
        cs = ChandrasekharSieve(18)
        cs.generate_primes()
        res = cs.get_primes()
        self.assertEqual(res, [2, 3, 5, 7, 11, 13, 17])

    def test_get_primes_3(self):
        cs = ChandrasekharSieve(15)
        cs.generate_primes()
        res = cs.get_primes()
        self.assertEqual(res, [2, 3, 5, 7, 11, 13])

import unittest

class AgentTest_get_primes(unittest.TestCase):
    def test_get_primes_1(self):
        cs = ChandrasekharSieve(1)
        res = cs.get_primes()
        self.assertEqual(res, [])

    def test_get_primes_2(self):
        cs = ChandrasekharSieve(2)
        res = cs.get_primes()
        self.assertEqual(res, [2])