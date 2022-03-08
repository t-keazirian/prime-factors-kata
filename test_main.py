import unittest

from main import PrimeFactors

class PrimeFactorsTestClass(unittest.TestCase):
    def test_1_returns_1(self):
        factors = PrimeFactors().factors_of
        self.assertEqual(factors(1), [])

    def test_2_returns_2(self):
        factors = PrimeFactors().factors_of
        self.assertEqual(factors(2), [2])

    def test_3_returns_3(self):
        factors = PrimeFactors().factors_of
        self.assertEqual(factors(3), [3])


