# Marco De Groskovskaja 24/01/23 - 30/01/23

class _BinarySearchTree:
    
    # Slide 249
    def _inorder_walk(self, node):
        if node != self.null:
            self._inorder_walk(node.left)
            print(node.data)
            self._inorder_walk(node.right)

    def _preorder_walk(self, node):
        if node != self.null:
            print(node.data)
            self._preorder_walk(node.left)
            self._preorder_walk(node.right)

    def _postorder_walk(self, node):
        if node != self.null:
            self._postorder_walk(node.left)
            self._postorder_walk(node.right)
            print(node.data)

    # Slide 257
    def _insert(self, node):
        # Traverse the tree looking for the parent
        parent = self.null
        curr = self.root
        while curr != self.null:
            parent = curr

            if node.data < curr.data:
                curr = curr.left
            else:
                curr = curr.right
            
        # Update the node.parent
        node.parent = parent

        # Insert node
        if parent == self.null:
            self.root = node

        elif node.data < parent.data:
            parent.left = node
        else:
            parent.right = node
    

    # Slide 260
    def _transplant(self, rm_tree_root, ins_tree_root):
        if rm_tree_root.parent == self.null:
            self.root = ins_tree_root
        else:

            if rm_tree_root == rm_tree_root.parent.left:
                rm_tree_root.parent.left = ins_tree_root
            else:
                rm_tree_root.parent.right = ins_tree_root

        ins_tree_root.parent = rm_tree_root.parent

    # Slide 261
    #
    # Case 1: The node to remove 'n' has no children
    # -> We remove the node 'n'
    #
    # Case 2: 'n' has one child
    # -> We remove the node 'n' and we reattach the children to the tree
    #
    # Case 3: 'n' has two children
    # -> We substitute 'n' with the maximum data of the left subtree
    #    or with the minimum data of the right subtree
    #

    def _remove(self, node):
        # Case 1 and Case 2:
        if node.left == self.null:
            self._transplant(node, node.right)
        
        elif node.right == self.null:
            self._transplant(node, node.left)

        # Case 3:
        else:
            successor = self._min(node.right)

            if successor.parent != self.null:
                self._transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            
            self._transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor

    # Slide 253
    def _search(self, node, data):
        while node != self.null and node.data != data:

            if data <= node.data:
                node = node.left
            else:
                node = node.right

        return node
    
    # Slide 254
    def _min(self, node):
        while node.left != self.null:
            node = node.left
        
        return node

    # Slide 254
    def _max(self, node):
        while node.right != self.null:
            node = node.right
        
        return node

    # Slide 256
    #
    # Case 1: The node 'n' has a non empty right subtree
    # -> The successor of 'n' is the min of such subtree
    #
    # Case 2: The node 'n' has an empty right subtree
    # -> The successor of 'n' is the first node 'f'
    #    such that 'n' is the left subtree of 'f'
    #
    def _successor(self, node):
        # Case 1:
        if node.right != self.null:
            return self._min(node.right)
        
        # Case 2:
        parent = node.parent
        while parent != self.null and node == parent.right:
            node = parent
            parent = parent.parent

        return parent
    
    def _predecessor(self, node):
        if node.left != self.null:
            return self._max(node.left)
        
        parent = node.parent
        while parent != self.null and node == parent.left:
            node = parent
            parent = parent.parent

        return parent     
