import unittest


import unittest

class AgentTest_generate_primes(unittest.TestCase):

    def test_generate_primes_1(self):
        cs = ChandrasekharSieve(20)
        self.assertEqual(cs.generate_primes(), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_generate_primes_2(self):
        cs = ChandrasekharSieve(20)
        self.assertIsInstance(cs.generate_primes(), list)

    def test_generate_primes_3(self):
        cs = ChandrasekharSieve(1)
        self.assertEqual(cs.generate_primes(), [])

    def test_generate_primes_4(self):
        def is_prime(k):
            if k < 2:
                return False
            d = 2
            while d * d <= k:
                if k % d == 0:
                    return False
                d += 1
            return True

        cs = ChandrasekharSieve(100)
        primes = cs.generate_primes()
        self.assertEqual(len(primes), 25)
        self.assertTrue(all(is_prime(p) for p in primes))
        self.assertEqual(primes[0], 2)
        self.assertEqual(primes[-1], 97)

    def test_generate_primes_5(self):
        cs = ChandrasekharSieve(50)
        self.assertEqual(
            cs.generate_primes(),
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],
        )

import unittest

class AgentTest_get_primes(unittest.TestCase):

    def test_get_primes_1(self):
        cs = ChandrasekharSieve(20)
        self.assertEqual(cs.get_primes(), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_get_primes_2(self):
        cs = ChandrasekharSieve(20)
        self.assertIsInstance(cs.get_primes(), list)

    def test_get_primes_3(self):
        cs = ChandrasekharSieve(1)
        self.assertEqual(cs.get_primes(), [])

    def test_get_primes_4(self):
        cs = ChandrasekharSieve(2)
        self.assertEqual(cs.get_primes(), [2])

    def test_get_primes_5(self):
        cs = ChandrasekharSieve(100)
        primes = cs.get_primes()
        self.assertEqual(len(primes), 25)
        self.assertEqual(primes[0], 2)
        self.assertEqual(primes[-1], 97)