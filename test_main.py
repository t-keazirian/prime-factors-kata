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

    def test_4_contains_2_2(self):
        factors = PrimeFactors().factors_of
        self.assertEqual(factors(4), [2, 2])

    def test_5_contains_5(self):
        factors = PrimeFactors().factors_of
        self.assertEqual(factors(5), [5])

    def test_6_contains_2_3(self):
        factors = PrimeFactors().factors_of
        self.assertEqual(factors(6), [2, 3])

    def test_7_contains_7(self):
        factors = PrimeFactors().factors_of
        self.assertEqual(factors(7), [7])

    def test_8_contains_2_2_2(self):
        factors = PrimeFactors().factors_of
        self.assertEqual(factors(8), [2, 2, 2])

    def test_9_contains_3_3(self):
        factors = PrimeFactors().factors_of
        self.assertEqual(factors(9), [3, 3])

    def test_10_contains_5_2(self):
        factors = PrimeFactors().factors_of
        self.assertEqual(factors(10), [2, 5])

    def test_all_numbers(self):
        factors = PrimeFactors().factors_of
        self.assertEqual(factors(2 * 3 * 5 * 7 * 11 * 13), [2,  3,  5,  7, 11, 13])



