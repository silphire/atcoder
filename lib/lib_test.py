import unittest
import lib


class TestPrime(unittest.TestCase):
    def test_prime_sequence(self):
        self.assertRaises(AssertionError, lib.Prime().prime_sequence, 0)
        self.assertEqual([], lib.Prime().prime_sequence(1))
        self.assertEqual([2], lib.Prime().prime_sequence(2))
        self.assertEqual([2, 3], lib.Prime().prime_sequence(3))


if __name__ == '__main__':
    unittest.main()
