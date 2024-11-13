### 11/11/2024
* Queue: first in, first out, enqueue --items--> dequeue
* Priority queue: ADT
    * Enqueue elements
    * Dequeue elements with priority
    * Higher priority is served first
    * If same priority: serve based on order in queue
    * insert(item, priority): add an item with a priority
    * find_min(): find the item with the minimum priority
    * remove_min(): remove and return the item with the minimum priority
* Priority queue implementations
    * List
        * insert: append O(1)
        * find_min: iterate through list to find min O(n)
        * remove_min: find min and pop O(n)
    * Reverse-sorted list
        * each append: sort the list backwwards
        * insert: O(n) for inserting the item in the correct place
        * find_min: O(1), end of list
        * remove_min: O(1), pop from end of list
* Heap: complete binary tree
    * Complete: every level but bottom is full, filled from left to right
    * Min heap: each root is smallest
        * O(1) to find min, at root
    * Max heap: each root is largest
    * Heap-ordered: every child has a priority at least as large as self priority
    * No in-order traverse, check branches top to bottom 
    * Items may not be all unique (less than or equal)
    * Use list to implement heap, traverse top-to-bottom, left-to-right
    * Find parent: index = i, parent = (i - 1) // 2
    * Find left and right children: index = i, left = (i * 2) + 1, right = (i * 2) + 2
    * Insert: append to list, then recursively swap with parent if smaller (upheap)
        * O(logn), O(height of tree, always complete)

### 11/13/2024
* Heap (complete binary tree) represented as list
    * left child: (2 * i) + 1
    * right child: (2 * i) + 2
    * parent: (i - 1) // 2
    * insert (append, upheap): append to list, recursively swap with parent if less than parent, O(logn)
    * find_min: return root, O(1)
    * remove_min (swap, then downheap): swap root with last element, remove last element (old root), recursively swap with min child
