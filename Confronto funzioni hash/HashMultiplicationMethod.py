# Marco De Groskovskaja 08/02/23 - 15/02/23
# Ref: Introduction to Algorithms 3rd Ed., Chapter 11

import math

from _HashTable import _HashTable
from _LinkedList import _LinkedList

class HashMultiplicationMethod(_HashTable):
    
    A = None

    def __init__(self, m):
        self.m = m
        self.h = [_LinkedList() for e in range(m)]
        self.A = ((math.sqrt(5) - 1) / 2)  # (11.2) p. 264
        self.size = 0

    def h_ix(self, key):
        return math.floor(self.m * ((key * self.A) % 1))
