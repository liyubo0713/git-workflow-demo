"""Tests for division, including the boundary case requested in review."""

import unittest

from calculator import divide


class DivisionTests(unittest.TestCase):
    def test_divide_positive_numbers(self):
        self.assertAlmostEqual(divide(6, 2), 3.0)

    def test_divide_negative_numbers(self):
        self.assertAlmostEqual(divide(-6, 2), -3.0)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            divide(6, 0)


if __name__ == "__main__":
    unittest.main()
