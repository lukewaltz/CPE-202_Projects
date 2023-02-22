import math


class HashTable:

    def __init__(self, table_size):  # add appropriate attributes, NO default size
        ''' Initializes an empty hash table with a size that is the smallest
            prime number that is >= table_size (i.e. if 10 is passed, 11 will
            be used, if 11 is passed, 11 will be used.)'''
        if self.is_prime(table_size):
            self.table_size = table_size
        else:
            self.table_size = self.next_prime(table_size)
        self.array = [None] * self.table_size
        self.num_items = 0

    def insert(self, key, value=None):
        ''' Inserts an entry into the hash table (using Horner hash function to determine index,
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is in the table, the new value replaces the existing value.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased
        to the next prime greater than 2*table_size.'''
        key_int = self.horner_hash(key)
        n = 0
        idx = key_int % self.table_size
        collision = idx
        while self.array[collision] is not None:
            # ---- quadratic probing -----
            if self.array[collision][0] == key:
                self.array[idx] = [key, value]
                pass
            collision = idx + n ** 2
            if idx + n**2 > self.table_size - 1:  # circular array
                collision = (idx + n**2) % self.table_size
            n += 1
        else:
            self.array[collision] = [key, value]
        self.num_items += 1

        # ---- load factor exceeded ----
        if self.get_load_factor() > 0.5:
            # insert items into new, larger array
            new = HashTable(self.table_size * 2)
            for tup in self.array:
                if tup is not None:
                    new.insert(tup[0], tup[1])
            self.array = new.array
            self.num_items = new.num_items
            self.table_size = new.table_size

    def horner_hash(self, key):
        ''' Compute the hash value by using Horner’s rule, as described in project specification.
            This method should not mod with the table size'''
        # ∑ 𝑜𝑟𝑑(𝑠𝑡𝑟[𝑖]) ∗ 31^(𝑛−1−𝑖) (just an algorithm)
        horn = []
        n = min(len(key), 8)
        for i in range(len(key[:n])):
            horn.append(ord(key[i]) * 31 ** (n - 1 - i))
        horn_final = sum(horn)
        # returns sum - should be a large integer
        return horn_final

    def in_table(self, key):
        ''' Returns True if key is in an entry of the hash table, False otherwise.'''
        horn = self.horner_hash(key) % self.table_size
        n = 0
        temp = self.array[horn]
        if temp is None:
            return False
        # ---- quadratic probing ----
        if temp is not None:
            while temp[0] != key:
                n += 1
                check = (horn + n**2) % self.table_size
                temp = self.array[check]
                if self.array[check] is None:
                    return False
            return True

    def get_index(self, key):
        ''' Returns the index of the hash table entry containing the provided key.
        If there is not an entry with the provided key, returns None.'''
        if not self.in_table(key):
            return None
        index = self.horner_hash(key) % self.table_size
        copy = index
        n = 0
        temp = self.array[index]
        # ---- quadratic probing ----
        while temp[0] != key:
            n += 1
            copy = (index + n**2) % self.table_size
            temp = self.array[copy]
        return copy

    def get_all_keys(self):
        ''' Returns a Python list of all keys in the hash table.'''
        # acceptable O(n)
        key_list = []
        for i in range(len(self.array)):
            tup = self.array[i]
            # tup = [key, value]
            if tup is not None:
                key = tup[0]
                key_list.append(key)
        return key_list

    def get_value(self, key):
        ''' Returns the value associated with the key.
        If key is not in hash table, returns None.'''
        # find an index based on the key and check that index in the hash table
        index = self.get_index(key)
        if index is None:
            return None
        item = self.array[index]
        val = item[1]
        return val

    def get_num_items(self):
        ''' Returns the number of entries in the table.'''
        return self.num_items

    def get_table_size(self):
        ''' Returns the size of the hash table.'''
        return self.table_size

    def get_load_factor(self):
        ''' Returns the load factor of the hash table (entries / table_size).'''
        lf = (self.get_num_items() / self.get_table_size())
        return lf

    def is_prime(self, n):
        # Corner cases
        if n <= 1:
            return False
        if n <= 3:
            return True

        if n % 2 == 0 or n % 3 == 0:
            return False

        for i in range(5, int(math.sqrt(n) + 1), 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False

        return True

    def next_prime(self, N):
        # Base case
        if N <= 1:
            return 2
        prime = N
        found = False
        # Loop continuously until isPrime returns true for a number greater than n
        while not found:
            prime = prime + 1
            if self.is_prime(prime):
                found = True
        return prime
