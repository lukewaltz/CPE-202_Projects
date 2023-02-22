from hash_quad import *
import string


class Concordance:

    def __init__(self):
        self.stop_table = HashTable(191)  # hash table for stop words
        self.concordance_table = HashTable(191)  # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            infile = open(filename, "r")
        except FileNotFoundError:
            raise FileNotFoundError

        for line in infile:
            line = line.strip()
            self.stop_table.insert(line, None)
        infile.close()

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        (The stop words hash table could possibly be None.)
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            infile = open(filename, "r")
        except FileNotFoundError:
            raise FileNotFoundError
        no_punc = ''
        line_cnt = 1
        for line in infile:
            # --- filters out capitalization ---
            for char in line:
                char = char.lower()
                if char in string.punctuation and char != "'":
                    char = ' '
                    no_punc += char
                if char == "'":
                    char = char.replace("'", "")
                    no_punc += char
                else:
                    no_punc += char

            words = no_punc.split()
            for word in words:
                if self.concordance_table.get_index(word) is not None:
                    # get index based on Horner hash & q probing
                    idx = self.concordance_table.get_index(word)
                    # assign array[idx] to word
                    key_val = self.concordance_table.array[idx]
                    # do not insert duplicate line numbers
                    if str(line_cnt) == key_val[1][-1]:
                        pass
                    else:
                        key_val[1].append(str(line_cnt))
                elif self.stop_table.get_index(word) is None and word.isalpha():
                    # insert to concordance-table if not in stop list and only contains letters
                    self.concordance_table.insert(word, [str(line_cnt)])
            no_punc = ''
            line_cnt += 1
            # repeat for all lines
        infile.close()

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        outfile = open(filename, "w")
        conc_array = self.concordance_table.array
        val_lst = []
        # append all pairs with keys and values to output list, sort it.
        for pair in conc_array:
            if pair is not None:
                val_lst.append(pair)
        val_lst = sorted(val_lst)
        # append related values to already inserted pairs; do not repeat key
        for pair in val_lst:
            val_str = ' '
            outfile.write(str(pair[0]) + ': ' + val_str.join(pair[1]))
            if pair != val_lst[-1]:
                outfile.write('\n')
        # file editing; no return necessary
        outfile.close()
