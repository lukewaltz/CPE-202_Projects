import unittest
import perm_lex


# Starter test cases - write more!

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex_1(self):  # str len 2
        self.assertEqual(perm_lex.perm_gen_lex('ab'), ['ab', 'ba'])

    def test_perm_gen_lex_2(self):  # str len 3
        self.assertEqual(perm_lex.perm_gen_lex('abc'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

    def test_perm_gen_lex_3(self):  # str len 1
        str_in = 'a'
        self.assertEqual(perm_lex.perm_gen_lex(str_in), ['a'])

    def test_perm_gen_lex_4(self):  # str len 0
        str_in = ''
        self.assertEqual(perm_lex.perm_gen_lex(str_in), [])

    def test_perm_gen_lex_5(self):  # str len 1
        str_in = 'abcd'
        self.assertEqual(perm_lex.perm_gen_lex(str_in), ['abcd', 'abdc', 'acbd',
                                                         'acdb', 'adbc', 'adcb',
                                                         'bacd', 'badc', 'bcad',
                                                         'bcda', 'bdac', 'bdca',
                                                         'cabd', 'cadb', 'cbad',
                                                         'cbda', 'cdab', 'cdba',
                                                         'dabc', 'dacb', 'dbac',
                                                         'dbca', 'dcab', 'dcba'])


if __name__ == "__main__":
    unittest.main()
