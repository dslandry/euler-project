import unittest

from solution_problem4 import *


class TestProblem4(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(101))
        self.assertTrue(is_palindrome(990099))
        self.assertTrue(is_palindrome(3003))
        self.assertTrue(is_palindrome(12321))
        self.assertFalse(is_palindrome(1230))


if __name__ == "__main__":
    unittest.main()
