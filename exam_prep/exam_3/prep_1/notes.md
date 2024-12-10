## Topics
* 8: Mappings and Hashing
    * Hashmap
* 9: Trees
    * Tree traversal
    * Binary search tree
    * Self-balancing BSTs
* 10: Priority Queues
    * Reverse sorted list implementation
    * Heap (complete binary tree): min and max
    * Heaps as lists
    * Heap priority queue
    * Heapify: building a heap from scratch
    * Changing priority
    * Heapsort
* 11: Graphs
    * Edge set
    * Adjacency set
    * Connectivity
    * Depth first search: stack
    * Breadth first search: queue

## Mod 8: Hashmap
* Think python dictionary: unordered, unique hashable keys, mutable
* Mapping: key -> value, keys must be unique
* Hashtable
    * Array of m buckets
    * hash(key) % n_buckets = bucket_idx
* Mapping ADT
    * put(key, value) -> None, O(1)
    * get(key) -> value, O(1)
* Hash collision: h(a) = h(b), a != b
    * Separate chaining (open hashing): all buckets are lists of kv pairs
    * Open addressing (closed hashing): storing colliding key in "next" bucket
* Rehashing
    * Maintain O(1) put and get when load_factor = n_items / n_buckets gets too large
    * Increase n_buckets, rehash every kv pair
    * Rehashing is an O(n) operation
* Hash function: immutable objects only (don't want hash to change)
* Mapping ADT implementation
    * KVPair: stores key and value, == compares keys
    * Bucket: stores list of KVPairs
    * Hashmap: stores array of Buckets

## Mod 9: Trees
* Tree definitions
    * Tree: hierarchical collection of nodes
    * Parent-children relationship
    * Root: top node
    * Leaf: no children
    * Edge: connection b/t 2 nodes
    * Depth: # edges from root to node (depth root = 0)
    * Height: max # edges to leaf (height leaf = 0)
    * Tree height: height of root

* Binary tree: parent has at most 2 children
    * Full: each parent has 2 or 0 children
    * Complete: every level except for deepest in completely full (top-down, left-right)
    * Perfect binary tree: complete and full, full for given height
* Binary tree traversals
    * pre-order: root, left, right
    * in-order: left, root, right
    * post-order: left, right, root

* Binary Search tree
    * Every left descendant is less, every right descendant is greater
    * In-order traversal gives the nodes arranged in order
    * get(key) -> value: O(tree height)
    * put(key, value) -> None: O(tree height)
    * remove(key) -> BSTNode to replace self with: O(tree height)
        * If no children: return None
        * If 1 child: return that child
        * If 2 children: find the max left child, swap key and value with max left child, then call remove on left subtree again
    * TODO: Floor and ceil functions
    * Problem: worst case unbalanced BST, tree height = n, all operations O(n) instead of O(logn)

* Self-Balancing BST Tree
    * Rotations: O(1)
    * Check a child is too heavy after put call, and rotate to balance
    * Draw out rotation, and implement
    
* Complicated functions:
    * put: because of self-balancing rotations
    * remove: because of having to find max in left subtree, swapping, and then calling remove on left subtree

## Mod 10: Priority Queue
* Queue: last in, first out
* Priority Queue ADT: items served with a priority
    * insert(item, priority)
    * find_min() -> returns the item with the minimum priority value
    * remove_min() -> remove and return the item with the minimum priority value

* List implementation
    * insert: append, O(1)
    * find_min: iterate through elements, find minimum elemenet O(n)
    * remove_min: iterate through elements, find minimum element, remove, O(n)
* Reverse sorted list implementation
    * insert: append, then bubble new item to correct position, O(n)
    * find_min: O(1), item will be at the end
    * remove_min: O(1), item will be at the end

* Heap
    * Binary heap
    * Min heap (root is min) or Max heap (root is max)
    * Complete binary tree: filled top to bottom, left to right, everything but bottom level is full
    * For min heap: priority of children are greater (not BST ordered)
    * Implemented as a list of items
    * Indexes
        * left child: (idx * 2) + 1
        * right child: (idx * 2) + 2
        * parent: (idx - 1) // 2
    * insert: append element, and upheap (recursively swap with parent if smaller), O(logn)
    * find_min: return root, O(1)
    * remove_min: swap with last node, remove new last node, and downheap (recursively swap with min child), O(logn)
    * TODO: change_priority: update priority, assume min heap, if higher priority, downheap, if lower priority, upheap

* Building a heap from scratch (heapify)
    * Upheapify: iterate from start to end, and upheap, O(nlogn)
    * Downheapify: don't have to downheap leaves, O(n)
        * iterate from (n // 2) to start (reverse-order), and downheap

* Heapsort: build a max heap, swap max with last, decrement heap size by 1, and downheap first
    * O(nlogn), in-place

# Mod 11: Graphs
* Graph defined as set of vertices V and edges E
* Undirected (doubly-directed) vs directed (edges point in 1 direction)
* Degree: # edges a vertex has
    * For directed: in-degree and out-degree
* Simple graph: no self-loops (start and end at same node), and no multiple edges (many edges b/t same pair of vertices)

* Graph ADT
    * init(V, E): create graph with vertices and edges
    * add_vertex(v)
    * remove_vertex(v)
    * add_edge(u, v): add edge connecting u, v
    * remove_edge(u, v)
    * neighbors(v): returns an iterable of all neighbors

* Edge set implementation
    * Store set of vertices V and edges E
    * Slow to enumerate neighbors, O(E): iterate through all edges, if v in edge tuple, return other edge
    * add / remove vertex: O(1)
    * add / remove edge: O(1)
    * neighbors: O(E)

* Adjacency set implementation
    * Store set of vertices V, and a dictionary of neighbors mapping v to set of neighbors
    * add / remove vertex: O(1)
    * add / remove edge: O(1)
    * neighbors: O(degree of V) to enumerate through neighbors

* Paths
    * Path: list of vertices connected by edge
    * Simple path: no repeated vertices
    * Path length = # edges
    * Cycle: path where start and end vertex are the same

* Connectivity
    * Directed graph
        * Strongly connected if path between any 2 vertices
        * Complete / fully connected if edge connects every pair of vertices
        * Disconnected graph: broken
    * Undirected graph
        * Connected if path between every pair of vertices
        * Complete: edge connects every pair of vertices
        * Disconnected graph: broken
    * check_connected(u, v): recursively check if neighbors are connected (base case if neighbor == target), keep track of visited to not get stuck in loop

* Graph Search
    * Depth first
        * stack implementation (last in, first out)
        * Explores deeply into neighbors, and then backtracks to explroe prev neighbors
        * Guarenteed to find __a__ path, not the shortest path
        * Runtime O(V + E)
    * Breadth first
        * queue implementation (first in, first out)
        * Explores all neighbors, then all neighbors of neighbors...
        * guarenteed to find shortest path
        * Runtime O(V + E), will visit at most every vertex and every edge.
