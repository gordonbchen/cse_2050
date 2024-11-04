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
