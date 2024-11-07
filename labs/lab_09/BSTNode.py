from __future__ import annotations

from typing import Any, Iterator


class BSTNode:
    """A node in a binary search tree."""

    def __init__(self, key: Any, left: BSTNode | None = None, right: BSTNode | None = None) -> None:
        """Construct a node. By default, left and right children are None."""
        self.key = key
        self.left = left
        self.right = right

    # Classic iteration (correct but slow).
    def __iter__(self) -> BSTNode_Iterator:
        """
        Classical iteration. Creates a new iterator object, which takes O(n)
        to construct the in-order list then returns items one at a time.
        """
        return BSTNode_Iterator(self)

    # Generator based iteration (fast).
    def in_order(self) -> Iterator:
        """
        Generator based iteration. We can return items as soon as we find them,
        and the recursive stack we've built stays in memory until the next call
        due to the `yield` keyword. Left, root, right.
        """
        if self.left is not None:
            yield from self.left.in_order()  # recursively go left

        yield self.key  # return this key

        if self.right is not None:
            yield from self.right.in_order()  # recursively go right

    def __repr__(self) -> str:
        """Return a str representation of the BSTNode."""
        return f"BSTNode(key={self.key})"

    def put(self, key: Any) -> None:
        """Add the key to the BST. Ignore duplicate keys."""
        if self.key == key:
            return
        elif key < self.key:
            if self.left is not None:
                self.left.put(key)
            else:
                self.left = BSTNode(key)
        else:
            if self.right is not None:
                self.right.put(key)
            else:
                self.right = BSTNode(key)

    def pre_order(self) -> Iterator:
        """Iterate through the BST keys in pre-order (root, left, right)."""
        yield self.key

        if self.left is not None:
            yield from self.left.pre_order()

        if self.right is not None:
            yield from self.right.pre_order()

    def post_order(self) -> Iterator:
        """Iterate through the BST keys in post-order (left, right, root)."""
        if self.left is not None:
            yield from self.left.post_order()

        if self.right is not None:
            yield from self.right.post_order()

        yield self.key


# This technique is slow. We have to queue up the ENTIRE tree before we start
# returning nodes. See above BSTNode.in_order() for an example that yields
# nodes one at a time without queueing up the whole tree.
class BSTNode_Iterator:
    def __init__(self, node):
        self.queue = []
        self.in_order(node)  # Queues up the entire tree
        self.counter = 0

    # in_order traversal/queueing
    def in_order(self, node):
        if node.left is not None:
            self.in_order(node.left)
        self.queue.append(node)
        if node.right is not None:
            self.in_order(node.right)

    # Update counter, return item, repeat
    def __next__(self):
        if self.counter < len(self.queue):
            self.counter += 1
            return self.queue[self.counter - 1].key

        raise StopIteration
