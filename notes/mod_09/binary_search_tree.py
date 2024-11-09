from __future__ import annotations

from typing import Any, Iterator


class BSTNode:
    def __init__(self, key: Any, value: Any) -> None:
        """Initialize the node."""
        self.key = key
        self.value = value

        # Children.
        self.left = None
        self.right = None

        self.weight = 1

    def get(self, key: Any) -> Any:
        """
        Get the value associated with the key.
        Raise a KeyError if the key is not found.
        """
        if key == self.key:
            return self.value
        elif (key > self.key) and (self.right is not None):
            return self.right.get(key)
        elif (key < self.key) and (self.left is not None):
            return self.left.get(key)

        raise KeyError(f"Key {key} not found in tree.")

    def put(self, key: Any, value: Any, parent: BSTNode | None = None) -> BSTNode:
        """
        Add a key-value pair to the tree.
        Update the value of a key if the key is already in the BST.
        """
        if key == self.key:
            self.value = value
        elif key > self.key:
            if self.right is None:
                self.right = BSTNode(key, value)
            else:
                self.right.put(key, value, parent=self)
        else:
            if self.left is None:
                self.left = BSTNode(key, value)
            else:
                self.left.put(key, value, parent=self)

        # Rotate to keep tree balanced.
        left_weight, right_weight = self.update_weights()
        if ((max(left_weight, right_weight) + 1) / (min(left_weight, right_weight) + 1)) >= 4:
            if left_weight > right_weight:
                return self.rotate_right(parent)
            else:
                return self.rotate_left(parent)

        return self

    def update_weights(self) -> tuple[int, int]:
        """Update the node's weight, and return the updated left and right weights."""
        left_weight = 0 if self.left is None else self.left.weight
        right_weight = 0 if self.right is None else self.right.weight
        self.weight = left_weight + right_weight + 1
        return left_weight, right_weight

    def rotate_left(self, parent: BSTNode | None) -> BSTNode:
        """Rotate the BST left."""
        old, new = self, self.right
        old.right = new.left
        new.left = old

        old.update_weights()
        new.update_weights()

        if parent is not None:
            if self.key < parent.key:
                parent.left = new
            else:
                parent.right = new

        return new

    def rotate_right(self, parent: BSTNode | None) -> BSTNode:
        """Rotate the BST right."""
        old, new = self, self.left
        old.left = new.right
        new.right = old

        old.update_weights()
        new.update_weights()

        if parent is not None:
            if self.key < parent.key:
                parent.left = new
            else:
                parent.right = new

        return new

    def remove(self, key: Any) -> BSTNode | None:
        """Remove a key from the BST."""
        if key == self.key:
            # If there is 1 child, point to that child.
            # If there are 0 children, point to None.
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            # If there are 2 children, find the max node in the left subtree.
            # Copy key/value, and remove the copied node.
            max_node = self.left.get_max_node()
            self.key = max_node.key
            self.value = max_node.value
            self.left = self.left.remove(max_node.key)
        elif (key < self.key) and (self.left is not None):
            self.left = self.left.remove(key)
        elif (key > self.key) and (self.right is not None):
            self.right = self.right.remove(key)
        else:
            raise KeyError(f"Key {key} not found in BST. Could not be removed.")

        return self

    def get_max_node(self) -> BSTNode:
        """Return the max node in the BST subtree."""
        if self.right is None:
            return self
        return self.right.get_max_node()

    def floor(self, key) -> BSTNode | None:
        """
        If the key is in the BST, return the node.
        Otherwise, return the node with the next lowest key.
        If there are no keys lower, return None.
        """
        if self.key == key:
            return self
        elif key < self.key:
            if self.left is None:
                return None

            return self.left.floor(key)
        else:
            if self.right is None:
                return self

            right_floor = self.right.floor(key)
            if right_floor is None:
                return self
            return right_floor

    def in_order_traverse(self) -> Iterator[BSTNode]:
        """Traverse the BST in-order."""
        if self.left is not None:
            yield from self.left.in_order_traverse()

        yield self

        if self.right is not None:
            yield from self.right.in_order_traverse()

    def pre_order_traverse(self) -> Iterator[BSTNode]:
        """Traverse the BST pre-order."""
        yield self

        if self.left is not None:
            yield from self.left.pre_order_traverse()

        if self.right is not None:
            yield from self.right.pre_order_traverse()

    def __str__(self) -> str:
        """Return a str representation of the node."""
        return f"BSTNode({self.key}, {self.value})"


if __name__ == "__main__":
    root = BSTNode(8, 8)
    root = root.put(6, 6)
    root = root.put(4, 4)
    root = root.put(5, 5)
    root = root.put(7, 7)

    for node in root.pre_order_traverse():
        print(node)
    print(root.get(5))

    for node in root.pre_order_traverse():
        print(node)

    root.remove(6)
    for node in root.pre_order_traverse():
        print(node)

    for i in [0, 4, 4.5, 100]:
        print(root.floor(i))

    print("\n\n")
    root = BSTNode(0, 0)
    for i in range(10):
        root = root.put(i, i)

        print(i)
        for node in root.pre_order_traverse():
            print(node)
