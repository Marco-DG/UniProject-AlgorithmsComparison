# Marco De Groskovskaja 24/01/23 - 30/01/23
#
# Classes:
#       
#   Node:
#
#       Attributes:
#
#           [str]  color
#               
#           Inherited:
#
#               [Node]  parent
#               [Node]  left
#               [Node]  right
#               [T]     data
#
# Attributes:
#
#   Inherited:
#
#         [Node]  null
#         [Node]  root
#
# Methods:
#
#   [void]  left_rotate([Node] node)                                        Slide 283
#   [void]  right_rotate([Node] node)
#
#   Overriden:
#
#       [void]  _insert([Node] node)
#       [void]  _remove([T] data)
#
#   Inherited:
#
#       [void]  inorder_walk()                                              Slide 249
#       [void]  preorder_walk()
#       [void]  post_order_walk()
#       [void]  transplant([Node] rm_tree_root, [Node] ins_tree_root)       Slide 260
#       [Node]  search([T] data)                                            Slide 253
#       [Node]  min()                                                       Slide 254
#       [Node]  max()                                                       Slide 254
#       [Node]  successor([Node] node)                                      Slide 256
#       [Node]  predecessor([Node] node)

from BinarySearchTree import BinarySearchTree
from _RedBlackTree import _RedBlackTree

class RedBlackTree(BinarySearchTree, _RedBlackTree):

    class Node(BinarySearchTree.Node):
        
        color = None

    def left_rotate(self, node):
        self._left_rotate(node)

    def right_rotate(self, node):
        self._left_rotate(node)
