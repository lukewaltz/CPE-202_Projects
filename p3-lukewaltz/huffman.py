from ordered_list import *
from huffman_bit_writer import *
from huffman_bit_reader import *


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char  # stored as an integer - the ASCII character code value
        self.freq = freq  # the freqency associated with the node
        self.left = None  # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def __eq__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        return type(self) == type(other) and \
               self.char == other.char and \
               self.freq == other.freq

    def __lt__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        if self.freq == other.freq:  # self == other --> compare ASCII
            return self.char < other.char  # self.ASCII > other --> False
        return self.freq < other.freq  # self.freq > other --> False


def create_code_helper(cur, code, codes):
    if cur.right is None and cur.left is None:
        codes[cur.char] = code
    else:
        create_code_helper(cur.left, code + '0', codes)
        create_code_helper(cur.right, code + '1', codes)


def cnt_freq(filename):
    '''Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file'''
    try:
        file = open(filename, "r")  # opens file to read
    except FileNotFoundError:
        raise FileNotFoundError('does not exist')
    char_freq = [0] * 256

    for line in file:
        for item in line:
            val = ord(item)
            char_freq[val] += 1
    file.close()
    return char_freq


def create_huff_tree(char_freq):
    '''Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree'''
    ord_lst = OrderedList()
    n = 0
    for i in range(len(char_freq)):
        # puts frequency and ASCII values into leaf Node and into an ordered list
        if char_freq[i] > 0:
            new = HuffmanNode(i, char_freq[i])
            ord_lst.add(new)
            n += 1
    if ord_lst.size() < 1:
        return None
    while ord_lst.size() > 1:
        node1 = ord_lst.pop(0)
        node2 = ord_lst.pop(0)
        # finds parent char
        parent_char = min(node1.char, node2.char)

        # parent freq is the sum of the children
        parent_freq = node1.freq + node2.freq

        # defines new parent node
        parent = HuffmanNode(parent_char, parent_freq)

        # finds parent left and right
        if node1.freq != node2.freq:
            if node1.freq < node2.freq:
                parent.left = node1
                parent.right = node2
        else:
            if node1.char < node2.char:
                parent.left = node1
                parent.right = node2

        # adds new parent node to the ordered list
        ord_lst.add(parent)
    if ord_lst.size() == 1:
        hufftree = ord_lst.pop(0)
        return hufftree
    # when len ordered list == 1, the list is now a tree


def create_code(node):
    '''Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation 
    as the index into the array, with the resulting Huffman code for that character stored at that location'''
    codes = [''] * 256
    code = ''
    if node is None:
        return codes
    create_code_helper(node, code, codes)
    # after all values have been encoded, return the array.
    return codes


def create_header(freqs):
    '''Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” '''
    header = ''
    for i in range(len(freqs)):
        if freqs[i] > 0:
            header = header + str(i) + ' ' + str(freqs[i]) + ' '
    return header.rstrip()


def huffman_encode(in_file, out_file):
    '''Takes inout file name and output file name as parameters - both files will have .txt extensions
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Also creates a second output file which adds _compressed before the .txt extension to the name of the file.
    This second file is actually compressed by writing individual 0 and 1 bits to the file using the utility methods 
    provided in the huffman_bits_io module to write both the header and bits.
    Take not of special cases - empty file and file with only one unique character'''
    infile = open(in_file, "r")  # opens file to read
    outfile = open(out_file, "w")  # opens file to write
    data = infile.read()  # get chars from infile

    # edge case
    if len(data) == 0:
        infile.close()
        outfile.close()
        compress = out_file[0: len(out_file) - 4] + '_compressed.txt'
        hbw = HuffmanBitWriter(compress)
        hbw.close()
        return
    freq = cnt_freq(in_file)
    header = create_header(freq)  # creates header using established functions
    tree = create_huff_tree(freq)
    codelst = create_code(tree)  # creates code list
    encoded = ''  # initializes str to add established codes to

    for char in data:
        code = codelst[ord(char)]  # each character is written in code in the encoded str
        encoded += str(code)
    infile.close()  # closes input file
    outfile.write(str(header) + '\n')  # writes header and newline into output file
    outfile.write(encoded)  # adds encoded str to output file
    outfile.close()  # closes output file

    # compressed file with bit writer
    compress = out_file[0: len(out_file) - 4] + '_compressed.txt'
    hbw = HuffmanBitWriter(compress)
    hbw.write_str(str(header) + '\n')
    hbw.write_code(str(encoded))
    hbw.close()


def huffman_decode(encoded_file, decode_file):
    # edge case - file doesnt exist
    try:
        check = open(encoded_file, 'r')
        check.close()
    except FileNotFoundError:
        raise FileNotFoundError

    # initialize variables
    input_txt = HuffmanBitReader(encoded_file)
    header_string = input_txt.read_str()
    header_freqs = parse_header(header_string)
    huffTree = create_huff_tree(header_freqs)
    # returns a huffman tree popped from an ordered list

    # total of all freqs
    total = sum(header_freqs)
    # amount its been iterated
    count = 0
    root = huffTree  # root node
    output_txt = open(decode_file, 'w')
    while count < total:
        tf = input_txt.read_bit()  # true/false from huff bit reader

        if huffTree.right is None and huffTree.left is None:  # only time output file should be written to
            #  leaf node conditions
            write = chr(huffTree.char)
            output_txt.write(write)
            huffTree = root
            # prevents infinite iteration
            count += 1

        if tf is False:
            # bitreader read 0
            huffTree = huffTree.left
        if tf is True:
            # bitreader read 1
            huffTree = huffTree.right

    # close text files
    output_txt.close()
    input_txt.close()


def parse_header(header_string):
    # make empty ascii array
    freq_lst = [0] * 256
    # get header chars
    header = header_string.split()
    # traverse header chars by ascii val and add freq to right spot in lst
    for i in range(0, len(header), 2):
        index = int(header[i])
        val = int(header[i + 1])
        freq_lst[index] = val
    return freq_lst
