import unittest
from base_convert import *


class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45, 2), "101101")

    def test_base4(self):
        self.assertEqual(convert(30, 4), "132")

    def test_base10(self):
        self.assertEqual(convert(100, 10), "100")

    def test_base4_2(self):
        self.assertEqual(convert(8, 4), "20")

    def test_base4_3(self):
        self.assertEqual(convert(13, 4), "31")

    def test_base14_A(self):
        self.assertEqual(convert(318, 14), "18A")  # A

    def test_base12(self):
        self.assertEqual(convert(311, 12), "21B")  # B

    def test_base16_C(self):
        self.assertEqual(convert(316, 16), "13C")  # C

    def test_base14_D(self):
        self.assertEqual(convert(321, 14), "18D")  # D

    def test_base16_E(self):
        self.assertEqual(convert(318, 16), "13E")  # E

    def test_base16_F(self):
        self.assertEqual(convert(319, 16), "13F")  # F

    def test_base14_C_first(self):
        self.assertEqual(convert(169, 14), "C1")

    def test_base_acceptance(self):
        j = 'j'
        i = 'i'
        self.assertEqual(convert(j, i), str(j))

    def test_base_negative(self):
        self.assertEqual(convert(-64, 8), "-8")

    def test_negative_base(self):
        self.assertFalse(convert(64, -6))


if __name__ == "__main__":
    unittest.main()
