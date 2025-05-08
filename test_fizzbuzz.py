import unittest
from fizzbuzz import fizz_buzz


class FizzBuzzTestsCases(unittest.TestCase):
    """Tests for fizz_buzz"""

    def test_multiples_three(self):
        """Test for definite multiples of three"""
        for i in (3, 6, 9, 12):
            self.assertEqual(fizz_buzz(i), "Three")

    def test_multiple_fives(self):
        """Test for definite multiples of five"""
        for i in (5, 10, 20):
            self.assertEqual(fizz_buzz(i), "Five")

    def test_multiple_five_three(self):
        """Test for definite multiples of five and three"""
        for i in (15, 45, 60, 75, 90):
            self.assertEqual(fizz_buzz(i), "ThreeFive")

    def test_non_three_five_multiples(self):
        """Test for numbers that are not divisible by three or 5"""
        for i in (1, 4, 7, 14, 17):
            self.assertEqual(fizz_buzz(i), i)

if __name__ == '__main__':
    unittest.main()