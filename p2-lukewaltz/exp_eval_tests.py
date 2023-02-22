# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *


class test_expressions(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_05(self):
        self.assertAlmostEqual(postfix_eval("3 5 + 3 5 + +"), 16)

    def test_postfix_eval_06(self):
        self.assertAlmostEqual(postfix_eval("3 5 *"), 15)

    def test_postfix_eval_07(self):
        self.assertAlmostEqual(postfix_eval("3 5 * 3 5 * +"), 30)

    def test_postfix_eval_08(self):
        self.assertAlmostEqual(postfix_eval("3 5 - 3 5 - +"), -4)

    def test_postfix_eval_09(self):
        self.assertAlmostEqual(postfix_eval("-15 3 /"), -5)

    def test_postfix_eval_10(self):
        self.assertAlmostEqual(postfix_eval("3 3 **"), 27)

    def test_postfix_eval_11(self):
        self.assertAlmostEqual(postfix_eval("10 3 >>"), 1)

    def test_postfix_eval_12(self):
        self.assertAlmostEqual(postfix_eval("10 3 <<"), 80)

    def test_postfix_eval_13(self):
        input_str = ""
        with self.assertRaises(PostfixFormatException):
            postfix_eval(input_str)

    def test_postfix_eval_14(self):
        input_str = "*kwargs"
        with self.assertRaises(PostfixFormatException):
            postfix_eval(input_str)

    def test_postfix_eval_15(self):
        input_str = "5 5.5 <<"
        with self.assertRaises(PostfixFormatException):
            postfix_eval(input_str)

    def test_postfix_eval_16(self):
        input_str = "10 0 /"
        with self.assertRaises(ValueError):
            postfix_eval(input_str)

    def test_postfix_eval_17(self):
        self.assertEqual(postfix_eval("12.0 5 -"), 7)

    def test_postfix_eval_18(self):
        input_str = "3.0 5.0 *"
        self.assertEqual(postfix_eval(input_str), 15)

    def test_postfix_eval_19(self):
        input_str = "3 5 + h +"
        with self.assertRaises(PostfixFormatException):
            postfix_eval(input_str)

    def test_infix_to_postfix_right_ass(self):
        self.assertEqual(infix_to_postfix("2 ** 3 ** 2"), '2 3 2 ** **')
        self.assertEqual(postfix_eval("2 3 2 ** **"), 512)

    def test_postfix_eval_float_tolerance(self):
        self.assertEqual(postfix_eval("12.0 3 +"), 15.0)

    def test_postfix_eval_NONE(self):
        self.assertIsNone(postfix_eval(None))

    def test_postfix_eval_acceptance(self):
        self.assertAlmostEqual(postfix_eval("12"), 12.0)

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")

    def test_infix_to_postfix_02(self):
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")

    def test_infix_to_postfix_03(self):
        self.assertEqual(infix_to_postfix("8 + 3 * 4 + ( 6 - 2 + 2 * ( 6 / 3 - 1 ) - 3 )"),
                         "8 3 4 * + 6 2 - 2 6 3 / 1 - * + 3 - +")

    def test_infix_to_postfix_04(self):
        self.assertEqual(infix_to_postfix("( 30 << 3 ) + 2"), "30 3 << 2 +")

    def test_infix_to_postfix_05(self):
        self.assertEqual(infix_to_postfix("( 30 >> 3 ** 2 ) * 2"), "30 3 >> 2 ** 2 *")

    def test_infix_to_postfix_word(self):
        self.assertEqual(infix_to_postfix("blah"), "blah")

    def test_infix_to_postfix_00(self):
        self.assertEqual(infix_to_postfix("bing + bong"), "bing bong +")

    def test_infix_to_postfix_NONE(self):
        self.assertIsNone(infix_to_postfix(None))

    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

    def test_prefix_to_postfix_01(self):
        self.assertEqual(prefix_to_postfix("** 3 3"), "3 3 **")

    def test_prefix_to_postfix_02(self):
        self.assertEqual(prefix_to_postfix("- ** 3 3 * 3 3"), "3 3 ** 3 3 * -")

    def test_prefix_to_postfix_03(self):
        input_str = "bruh"
        self.assertEqual(prefix_to_postfix(input_str), "bruh")

    def test_prefix_to_postfix_NONE(self):
        self.assertIsNone(prefix_to_postfix(None))

    def test_illegal_eval_01(self):
        try:
            postfix_eval('6 2 / 3 >>')
        except PostfixFormatException as e:
            self.assertEqual(str(e), 'Illegal bit shift operand')

    def test_illegal_eval_02(self):
        try:
            postfix_eval('6 2 / 3 <<')
        except PostfixFormatException as e:
            self.assertEqual(str(e), 'Illegal bit shift operand')

    def test_illegal_eval_03(self):
        input_str = "3 3.0 <<"
        with self.assertRaises(PostfixFormatException):
            postfix_eval(input_str)

    def test_illegal_eval_04(self):
        input_str = "3 3.0 >>"
        with self.assertRaises(PostfixFormatException):
            postfix_eval(input_str)

    def test_empty_eval(self):
        try:
            postfix_eval("")
        except PostfixFormatException as e:
            self.assertEqual(str(e), 'Empty input')

    def test_empty_pre_to_post(self):
        try:
            prefix_to_postfix("")
        except PostfixFormatException as e:
            self.assertEqual(str(e), 'Empty input')

    def test_empty_in_to_post(self):
        try:
            infix_to_postfix("")
        except PostfixFormatException as e:
            self.assertEqual(str(e), 'Empty input')

    def test_in_to_post_multi_space(self):
        self.assertEqual(infix_to_postfix("1  +  1"), "1 1 +")

    def test_pre_to_post_multi_space(self):
        self.assertEqual(infix_to_postfix("+  1  1"), "1 1 +")

    def test_pre_to_post_basic(self):
        self.assertEqual(prefix_to_postfix("+ + + 5 -7.1 11 3"), "5 -7.1 + 11 + 3 +")


if __name__ == "__main__":
    unittest.main()
