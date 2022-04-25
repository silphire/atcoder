import unittest
import lib


class TestPrime(unittest.TestCase):
    def test_prime_sequence(self):
        self.assertRaises(AssertionError, lib.Prime().prime_sequence, 0)
        self.assertEqual([], lib.Prime().prime_sequence(1))
        self.assertEqual([2], lib.Prime().prime_sequence(2))
        self.assertEqual([2, 3], lib.Prime().prime_sequence(3))

    def test_prime_factorize(self):
        self.assertCountEqual([], lib.Prime().prime_factorize(1))
        self.assertCountEqual([2, 2, 3], lib.Prime().prime_factorize(12))
        self.assertCountEqual([2, 2, 5, 5], lib.Prime().prime_factorize(100))


if __name__ == '__main__':
    unittest.main()
