# https://github.com/lukasgoofus/lab11-LV-PP.git
# Partner 1: Lukas Vicovan

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
######## Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 4), 6)
        self.assertEqual(add(-1, -2), -3)
        self.assertEqual(add(0, 0),0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract (2, 3), -1)
        self.assertEqual(subtract(4, 3), 1)
        self.assertEqual(subtract(0, 0), 0)

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(1, 0), 0)
        self.assertEqual(mul(0, 1), 0)
        self.assertEqual(mul(2, 10), 20)
        self.assertEqual(mul(-1, 40), -40)
        self.assertEqual(mul(-2, -5), 10)

    def test_divide(self):  # 3 assertions
        with self.assertRaises(ZeroDivisionError):
            div(0, 7)
        self.assertAlmostEqual(div(5, 10), 10 / 5)
        self.assertAlmostEqual(div(-2, 10), 10 / (-2))
        self.assertAlmostEqual(div(5, 0), 0)
    ################

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0, -1)
        with self.assertRaises(ZeroDivisionError):
            div(0, 0)

    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(logarithm (2, 8), 3)
        self.assertAlmostEqual(logarithm (3, 9), 2)
        self.assertAlmostEqual(logarithm (10, 1000), 3)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 1)
        with self.assertRaises(ValueError):
            logarithm(1, 1)
    ###################

    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(-1, 5)
        with self.assertRaises(ValueError):
            logarithm(1,5)
        with self.assertRaises(ValueError):
            logarithm(2, -5)

    def test_hypotenuse(self):  # 3 assertions
        self.assertAlmostEqual(hypotenuse(0, 5), math.hypot(0, 5))
        self.assertAlmostEqual(hypotenuse(2, 5), math.hypot(2, 5))
        self.assertAlmostEqual(hypotenuse(-1, 5), math.hypot(-1, 5))
        self.assertAlmostEqual(hypotenuse(-5, -10), math.hypot(-5, -10))

    def test_sqrt(self):  # 3 assertions
        # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root(-5)
        with self.assertRaises(ValueError):
            square_root(-10)
        # Test basic function
        self.assertAlmostEqual(square_root(25), 5)
        self.assertAlmostEqual(square_root(49), 7)
        self.assertAlmostEqual(square_root(1), 1)
        self.assertAlmostEqual(square_root(4), 2)
##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
