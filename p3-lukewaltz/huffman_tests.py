import unittest
import filecmp
import subprocess
from ordered_list import *
from huffman import *


class TestList(unittest.TestCase):
    def test_cnt_freq(self):
        freqlist = cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0]
        self.assertListEqual(freqlist[97:104], anslist)

    def test_lt_and_eq(self):
        freqlist = cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0]
        ascii = 97
        lst = OrderedList()
        for freq in anslist:
            node = HuffmanNode(ascii, freq)
            lst.add(node)
            ascii += 1
        self.assertEqual(lst.index(HuffmanNode(101, 0)), 0)
        self.assertEqual(lst.index(HuffmanNode(100, 16)), 6)
        self.assertEqual(lst.index(HuffmanNode(97, 2)), 2)
        self.assertFalse(HuffmanNode(97, 2) == None)

    def test_create_huff_tree_00(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char, 97)
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char, 97)
        right = hufftree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char, 100)
        left2 = left.left
        self.assertEqual(left2.freq, 8)
        self.assertEqual(left2.char, 97)
        left3 = left2.left
        self.assertEqual(left3.freq, 4)
        self.assertEqual(left3.char, 97)
        left4 = left3.left
        self.assertEqual(left4.freq, 2)
        self.assertEqual(left4.char, 97)
        leftr1 = left.right
        self.assertEqual(leftr1.freq, 8)
        self.assertEqual(leftr1.char, 99)
        leftr2 = left2.right
        self.assertEqual(leftr2.freq, 4)
        self.assertEqual(leftr2.char, 98)
        leftr3 = left3.right
        self.assertEqual(leftr3.freq, 2)
        self.assertEqual(leftr3.char, 102)

    def test_create_header(self):
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")

    def test_create_code_00(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')

    def test_create_code_01(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        right = hufftree.right
        self.assertEqual(right.char, 100)
        self.assertEqual(codes[ord('d')], '1')

    def test_create_code_02(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        left = hufftree.left
        self.assertEqual(left.char, 97)
        self.assertEqual(codes[ord('a')], '0000')

    def test_create_code_03(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('f')], '0001')

    def test_01_textfile(self):
        huffman_encode("file1.txt", "file1_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file1_out.txt file1_soln.txt", shell=True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb file1_out_compressed.txt file1_compressed_soln.txt", shell=True)
        self.assertEqual(err, 0)

    def test_02_textfile(self):
        huffman_encode("file2.txt", "file2_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file2_out.txt file2_soln.txt", shell=True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb file2_out_compressed.txt file2_compressed_soln.txt", shell=True)
        self.assertEqual(err, 0)

    def test_empty_textfile(self):
        huffman_encode("empty.txt", "empty_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb empty_out.txt empty_soln.txt", shell=True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb empty_out_compressed.txt empty_out_compressed-soln.txt", shell=True)
        self.assertEqual(err, 0)

    def test_no_textfile(self):
        with self.assertRaises(FileNotFoundError):
            cnt_freq("whee.txt")
            huffman_encode("wheee.txt", "wheee_out.txt")

    def test_declaration(self):
        huffman_encode("declaration.txt", "declaration_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb declaration_out.txt declaration_soln.txt", shell=True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb declaration_out_compressed.txt declaration_compressed_soln.txt", shell=True)
        self.assertEqual(err, 0)

    def test_03_textfile(self):
        huffman_encode("file3.txt", "file3_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file3_out.txt file3_soln.txt", shell=True)
        self.assertEqual(err, 0)

    def test_unique_textfile(self):
        huffman_encode("unique.txt", "unique_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb unique_out.txt unique_soln.txt", shell=True)
        self.assertEqual(err, 0)

    def test_cc_helper_00(self):
        freqlist = cnt_freq("empty.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '')
        self.assertEqual(codes[ord('a')], '')
        self.assertEqual(codes[ord('f')], '')

    def test_cc_helper_01(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')

    def test_header_reader_00(self):
        hbr = HuffmanBitReader("file1_compressed_soln.txt")
        header_str = hbr.read_str()
        freq_lst = parse_header(header_str)
        sample = freq_lst[97: 101]
        self.assertListEqual(sample, [4, 3, 2, 1])

    def test_01a_test_file1_parse_header(self):
        f = open('file1_compressed_soln.txt', 'rb')
        header = f.readline()
        f.close()
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 2, 1, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0]
        self.compare_freq_counts(parse_header(header), expected)

    def test_01_test_file1_decode(self):
        huffman_decode("file1_compressed_soln.txt", "file1_decoded.txt")
        err = subprocess.call("diff -wb file1.txt file1_decoded.txt", shell=True)
        self.assertEqual(err, 0)

    def compare_freq_counts(self, freq, exp):
        for i in range(256):
            stu = 'Frequency for ASCII ' + str(i) + ': ' + str(freq[i])
            ins = 'Frequency for ASCII ' + str(i) + ': ' + str(exp[i])
            self.assertEqual(stu, ins)

    def test_no_textfile_decode(self):
        with self.assertRaises(FileNotFoundError):
            huffman_decode("wheee.txt", "wheee_out.txt")

    def test_decode_empty_textfile(self):
        huffman_decode("empty.txt", "empty_out.txt")
        err = subprocess.call("diff -wb empty_out.txt empty.txt", shell=True)
        self.assertEqual(err, 0)


if __name__ == '__main__':
    unittest.main()