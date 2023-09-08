# Marco De Groskovskaja 08/02/23 - 15/02/23
# Ref: Introduction to Algorithms 3rd Ed., Chapter 11

from _HashTable import _HashTable
from _LinkedList import _LinkedList

class HashDivisionMethod(_HashTable):

    def __init__(self, m):
        self.m = m
        self.h = [_LinkedList() for e in range(m)]
        self.size = 0

    def h_ix(self, key):
        return key % self.m
