# Mod 8: Hashmap
* Unique key -> value
* Mapping ADT:
    * put(key, value) -> None, O(1)
    * get(key) -> value, O(1)
* Hashtable:
    * Array of buckets
    * bucket_idx = hash(key) % n_buckets
* Hash collision: hash(k1) == hash(k2), and k1 != k2
    * Separate chaining: buckets are lists of values, iterate through bucket to find kv pair
    * load_factor = n_items / n_buckets
    * Rehash when load_factor too large, rehash every kv pair to new bucket
    * Rehash: O(n)
* Only immutable objects are hashable (don't want hash to change)

# Mod 9: BST
## Tree
* Height: max dist from node to leaf (leaf nodes have height 0)
* Depth: max dist from node to root (rooto has depth 0)
* Types of binary trees
    * Full binary tree: each node has 0 or 2 children
    * Complete binary tree: filled top to bottom, left to right
    * Perfect binary tree: has max nodes for height
* Traversals
    * Pre-order (pass left of node): root, left, right
    * In-order (pass bottom of node): left, root, right
    * Post-order (pass right of node): left, right, root

## Binary Search Tree
* BST: every left child is smaller, every right child is greater
* In-order traversal on BST will give nodes sorted by key
* ADT methods, all O(tree height), O(logn) when balanced else O(n)
    * get(key) -> value
    * put(key, value) -> None
    * remove(key) -> value
    * floor(key) -> value
    * ceil(key) -> value
* Rotation: O(1), keeps tree balanced, maintains O(logn) for funcs
    * Weight-balanced
    * Height-balanced

# Mod 10: Priority Queue (Heaps)
* Queue: first in, first out
* Priority queue: items have priority values, higher priority served first
* Priority Queue ADT:
    * put(item, priority) -> None
    * find_min() -> item with lowest priority
    * remove_min() -> find and remove item with lowest prirotiy
* List implementation: O(1) put (append), O(n) find_min, O(n) remove_min
* Reverse sorted list implementation: O(n) put, O(1) find_min, O(1) remove_min (pop)

## Heap
* Min heap (root is min), and max heap (root is max)
* Complete binary tree: top-down, left-right
* Heap ordered: root-to-leaf paths are sorted
* Implmented as list
    * left_child: 2i + 1
    * right_child: 2i + 2
    * parent: (i - 1) // 2
* put(item, priority): append item, upheap (recursively swap with greater parent), O(logn)
* find_min(): return root, O(1)
* remove_min() -> min priority item: swap root with last, pop new last, downheap new root (recursively swap with min child), O(logn)
* change_priority(): find node w/ dict of keys to inds (O(n) memory overhead), then change priority, upheap/downheap as needed, O(logn)
* Building a heap from scratch
    * Upheapify: iterate from 1 to n, upheap every node O(nlogn)
    * Downheapify: iterate reverse(range(n // 2)), downheap non-leaf nodes, O(n)
* Heapsort: build max heap, swap with last in heap, decrement heap size, call downheap on root, O(nlogn)

# Mod 11: Graphs
* Graph: set of vertices and set of edges
* Neighbors: vertices connected by edges
* Undirected graph: edges are bi-directional, set(u, v), degree = # edges
* Directed graph: edges are uni-directional, tuple(u, v), in-degree and out-degree
* Simple graph: no self-loops (edge that starts and ends at same vertex) or multiple edges (between the same nodes)

## Graph
* ADT:
    * init(V, E) -> None
    * add_vertex(v) -> None
    * remove_vertex(v) -> None
    * add_edge(u, v) -> None
    * remove_edge(u, v) -> None
    * get_neighbors(v) -> Iterable[v]
* Edge set implementation
    * Set of edges E
    * get_neighbors(v): O(E), iterate through every edge, see if v in edge
* Adjacency set implementation
    * Dict of vertex -> neighbors
    * get_neighbors(v): O(degree of v), iterate through only neighbors of v

## Graph properties
* Path length = # edges
* Cycle: path starting and ending at same vertex

* Disconnected: broken graph
* Strongly connected: path from vertex to every other vertex (directed)
* Complete / fully connected: edge from vertex to every other vertex


## Graph search
* Depth first search: stack implementation (last in, first out), explores deeply then backtracks
* Breadth first search: queue implementation (first in, first out), explores all neighbors, then neighbors of neighbors...
    * guarenteed to find shortest path
