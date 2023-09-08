# Marco De Groskovskaja 24/01/23 - 30/01/23
#  
# Classes:
#       
#   Node:
#
#       Attributes:
#            
#           [Node]  parent
#           [Node]  left
#           [Node]  right
#           [T]     data
# 
# Attributes:
# 
#   [Node]  null
#   [Node]  root
# 
# Methods:
# 
#   [None]  inorder_walk()                                              Slide 249
#   [None]  preorder_walk()
#   [None]  post_order_walk()
#   [None]  insert([T] data)                                            Slide 257
#   [None]  transplant([Node] rm_tree_root, [Node] ins_tree_root)       Slide 260
#   [None]  remove([T] data)                                            Slide 261
#   [Node]  search([T] data)                                            Slide 253
#   [Node]  min()                                                       Slide 254
#   [Node]  max()                                                       Slide 254
#   [Node]  successor([Node] node)                                      Slide 256
#   [Node]  predecessor([Node] node)
   
from _BinarySearchTree import _BinarySearchTree


class BinarySearchTree(_BinarySearchTree):

    class Node:

        parent = None
        left = None
        right = None
        data = None

        def __init__(self, data):
            self.data = data

    null = Node(None)
    root = None

    def __init__(self):
        self.null = self.Node(None)
        self.null.parent = self.null
        self.null.right = self.null
        self.null.left = self.null
        self.root = self.null

    def inorder_walk(self):
        self._inorder_walk(self.root)

    def preorder_walk(self):
        self._preorder_walk(self.root)

    def postorder_walk(self):
        self._postorder_walk(self.root)

    def insert(self, data):
        node = self.Node(data)
        node.parent = self.null
        node.left = self.null
        node.right = self.null
        self._insert(node)

    def transplant(self, rm_tree_root, ins_tree_root):
        self._transplant(rm_tree_root, ins_tree_root)

    def remove(self, data):
        node = self.search(data)
        if node:
            self._remove(node)

    def search(self, data):
        return self._search(self.root, data)

    def min(self):
        return self._min(self.root)

    def max(self):
        return self._max(self.root)

    def successor(self, node):
        return self._successor(node)

    def predecessor(self, node):
        return self._predecessor(node)
