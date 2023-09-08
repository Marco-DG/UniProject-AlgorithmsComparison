# Marco De Groskovskaja 24/01/23 - 07/02/23

from _BinarySearchTree import _BinarySearchTree

class _RedBlackTree(_BinarySearchTree):

    # Slide 283
    def _left_rotate(self, node):

        right_child = node.right
        node.right = right_child.left

        if right_child.left != self.null:
            right_child.left.parent = node
        
        right_child.parent = node.parent

        if node.parent == self.null:
            self.root = right_child

        elif node == node.parent.left:
            node.parent.left = right_child

        else:
            node.parent.right = right_child

        right_child.left = node
        node.parent = right_child

    def _right_rotate(self, node):

        left_child = node.left
        node.left = left_child.right

        if left_child.right != self.null:
            left_child.right.parent = node
        
        left_child.parent = node.parent

        if node.parent == self.null:
            self.root = left_child

        elif node == node.parent.right:
            node.parent.right = left_child

        else:
            node.parent.left = left_child

        left_child.right = node
        node.parent = left_child
    
    # Slide 284
    def _insert(self, node):
        # Call to _BinarySearchTree._insert(node)
        super()._insert(node)

        node.left = self.null
        node.right = self.null
        node.color = "Red"

        while node.parent.color == "Red":
            if node.parent == node.parent.parent.left:

                uncle = node.parent.parent.right

                if uncle.color == "Red":

                    node.parent.color = "Black"
                    uncle.color = "Black"
                    node.parent.parent.color = "Red"
                    node = node.parent.parent
                
                else:

                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)

                    node.parent.color = "Black"
                    node.parent.parent.color = "Red"
                    self._right_rotate(node.parent.parent)

            else:
                uncle = node.parent.parent.left

                if uncle.color == "Red":

                    node.parent.color = "Black"
                    uncle.color = "Black"
                    node.parent.parent.color = "Red"
                    node = node.parent.parent
                
                else:

                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)

                    node.parent.color = "Black"
                    node.parent.parent.color = "Red"
                    self._left_rotate(node.parent.parent)

        self.root.color = "Black"

    # Introduction to Algorithms 3rd Ed., Chapter 13
    def _remove(self, node):

        min_node = node
        original_color = node.color

        if node.left is self.null:
            to_move = node.right
            self._transplant( node, node.right )
        
        elif node.right is self.null:
            to_move = node.left
            self._transplant( node, node.left )

        else:
            min_node = self._min( node.right )
            original_color = min_node.color
            to_move = min_node.right

            if min_node.parent is node:
                to_move.parent = min_node

            else:
                self._transplant( min_node, min_node.right )
                min_node.right = node.right
                min_node.right.parent = min_node

            self._transplant( node, min_node )
            min_node.left = node.left
            min_node.left.parent = min_node
            min_node = node.color 


        if original_color == "black":
            print("FIIIIX")
            ### Remove Fixup
            node = to_move
            while ( not node is self.root ) and node.color == "black":

                if node is node.parent.left:

                    brother = node.parent.right

                    if brother.color == "red":

                        brother = "black"

                        node.parent = "red"

                        self.left_rotate( node.parent )

                        brother = node.parent.right

                    if brother.left.color == "black" and brother.right.color == "black":

                        brother = "red"

                        node = node.parent

                    else:
                        if brother.right.color == "black":

                            brother.left = "black"

                            brother = "red"

                            self.right_rotate( brother )

                            brother = node.parent.right

                        brother.set_color( node.parent.color )

                        node.parent = "black"

                        brother.right = "black"

                        self.left_rotate( node.parent )

                        node = self.root

                else: # node is node.parent.right:

                    brother = node.parent.left

                    if brother.color == "red":

                        brother = "black"

                        node.parent = "red"

                        self.right_rotate( node.parent )

                        brother = node.parent.left

                    if brother.left.color == "black" and brother.right.color == "black":

                        brother = "red"

                        node = node.parent

                    else:
                        if brother.left.color == "black":

                            brother.right = "black"

                            brother = "red"

                            self.left_rotate( brother )

                            brother = node.parent.left

                        brother.set_color( node.parent.color )

                        node.parent = "black"

                        brother.left = "black"

                        self.right_rotate( node.parent )

                        node = self.root

            node = "black"
