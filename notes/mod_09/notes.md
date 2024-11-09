### 11/4/2024
* Tree: heirarchical collection of nodes
    * Root: top node, 1st ancestor, no parents
    * Children, parents
    * Internal nodes: nodes w/ children (includes node)
    * Leaf nodes: end of tree, no children
* Relations
    * Siblings: nodes with same parent
    * Edge: connection b/t nodes
    * Path: series of edges connecting nodes, path length = # edges
    * Subtree: part of the tree
    * Ancestor, descendant
* Depth and height
    * Depth: # of edges from node to root
    * Height: # of edges on longest path from node to leaf
    * Depth of deepest node = height
* Binary tree
    * Each node has at most 2 children
    * Children are left and right child
    * Full: nodes as 2 or 0 children
    * Complete: every level except deepest is completely filled
    * Perfect: all leaf nodes are the same depth, all internal nodes have 2 children, full
* Tree traversal
    * Visit each node 1 time
    * Pre-order: root, left, right
    * In-order: left, root, right
    * Post-order: left, right, root
    * Level order: top to bottom, left to right

### 11/6/2024
* Iterators
    * __iter__: called with iter()
    * __next__: called with next(), produces next item, raises StopIteration when done
    * For is a while loop
    * Generator: yield values
* Binary search tree
    * left node is less, right node is greater
    * Tree sort algorithm: in order traverse on BST
    * ADT: put, get, floor, ceil, remove
    * Time complexity based on height of tree: best case log2n, worst case n

## 11/8/2024
* Removal
    * Search for node from root
    * If leaf node: parent.left = None
    * If 1 child: replace node with child
    * If 2 children: swap with largest key in left subtree (left, then right recursively), then call remove again on the lelft subtree.
        * Or the smallest key in the right subtree (right once, then left recursively)
* Floor: return None or greatest floor value
* In-order traverse: will always get elements in order (left, root, right)
* Time complexity always based on tree height (log2n best, n worst)
* Balancing: Left/right rotation, constant time

# 11/9/2024 (BST review)
* Left subtree only contains keys less than, right subtree only contains keys greater than
* In-order traverse: left, root, right
* get, put: O(length of longest path) = O(height of tree)
* remove:
    * leaf: simple deletion: parent.left = None
    * 1 child: move child up: parent.left = self.left
    * find greatest value in left subtree (or lowest value in right subtree), swap with node to be removed, and then call remove on the left subtree (will be leaf node)
    * O(tree height)
* floor: return node with matching key or next lowest (max less than)
    * return None if none are lower
* Worst case: O(tree height) = O(n), when keys are inserted in order.
* Rotations: weight balancing O(1)
    * Right rotation: self.right = self.parent, self.parent.left = self.old_right
    * Explanation: the parent will be greater than the node (node is in the left subtree when right rotating), so parent will be self.right. The old right was in the left subtree of the parent, so now make it the left node of the parent. 
    * Left rotation: self.left = self.parent, self.parent.right = self.old_left
* Height-balanced tree: AVL trees, self-balancing BST
    * O(logn) get, put, remove
