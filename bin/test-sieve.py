
import unittest
from sieve import primes

class SieveTest(unittest.TestCase):
    """Tests for 'sieve.py'."""

    def test_17(self):
        """Does test up to 17 get the expected results?"""
        sieved = primes(17)
        self.assertEqual(sieved[-1], 17)

unittest.main()

