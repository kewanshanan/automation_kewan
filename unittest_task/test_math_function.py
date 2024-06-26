import unittest
from math_function import modulo_func, is_even, is_odd, sum_function, sub_function, mul_function, div_function

class TestMathFunctions(unittest.TestCase):
    def test_modulo_func_zero(self):
        self.assertEqual(modulo_func(0), 0)

    def test_modulo_func_even(self):
        self.assertEqual(modulo_func(4), 0)

    def test_modulo_func_odd(self):
        self.assertEqual(modulo_func(5), 1)

    def test_func_is_even_true(self):
        self.assertTrue(is_even(4))

    def test_func_is_even_false(self):
        self.assertFalse(is_even(3))

    def test_func_is_odd_true(self):
        self.assertTrue(is_odd(3))

    def test_func_is_odd_false(self):
        self.assertFalse(is_odd(4))

    def test_sum_function_positive(self):
        self.assertEqual(sum_function(3, 5), 8)

    def test_sum_function_negative(self):
        self.assertEqual(sum_function(-3, -5), -8)

    def test_sub_function_positive(self):
        self.assertEqual(sub_function(10, 5), 5)

    def test_sub_function_negative(self):
        self.assertEqual(sub_function(-3, -5), 2)

    def test_mul_function_positive(self):
        self.assertEqual(mul_function(3, 5), 15)

    def test_mul_function_negative(self):
        self.assertEqual(mul_function(-3, -5), -15)

    def test_mul_function_zero(self):
        self.assertEqual(mul_function(0, 5), 0)

    def test_div_function_positive(self):
        self.assertEqual(div_function(10, 2), 5)

    def test_div_function_float(self):
        self.assertEqual(div_function(5, 2), 2.5)

    def test_div_function_negative(self):
        self.assertEqual(div_function(-5, -2), 2.5)

    def test_div_function_zero_divisor(self):
        with self.assertRaises(ZeroDivisionError):
            div_function(5, 0, "cant dividing by zero")


