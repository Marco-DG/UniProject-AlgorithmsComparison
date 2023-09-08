# Marco De Groskovskaja 08/02/23 - 15/02/23
# Ref: Introduction to Algorithms 3rd Ed., Chapter 11

class _HashTable:
    m = None
    h = None
    size = None

    def is_full(self):
        if self.size < self.m:
            return False
        elif self.size == self.m:
            print("The table is full.")
            return True
        else:
            raise Exception("self.size = {} > self.m = {}".format(self.size, self.m))

    def insert(self, key, value):
        if not self.is_full():
            ix = self.h_ix(key)
            self.h[ix].push_back(key, value)
            self.size += 1

    def search(self, key):
        ix = self.h_ix(key)
        return self.h[ix].search(key)

    def remove(self, key):
        ix = self.h_ix(key)
        if self.h[ix].remove(key):
            self.size -= 1

    def load_factor(self):
        return self.size/self.m
