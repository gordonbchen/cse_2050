from __future__ import annotations

from typing import Any, Iterator


class BSTNode:
    def __init__(self, key: Any, value: Any) -> None:
        self.key = key
        self.value = value

        self.left: BSTNode | None = None
        self.right: BSTNode | None = None

        self.weight = 1

    def get(self, key: Any) -> Any:
        if self.key == key:
            return self.value

        if (key < self.key) and self.left:
            return self.left.get(key)
        elif (key > self.key) and self.right:
            return self.right.get(key)

        raise KeyError(f"Key {key} not in BST.")

    def put(self, key: Any, value: Any, parent: BSTNode | None = None) -> BSTNode:
        """Returns the node this one should be replaced with (after rotations)."""
        if key == self.key:
            self.value = value

        elif key < self.key:
            if self.left:
                self.left.put(key, value, parent=self)
            else:
                self.left = BSTNode(key, value)

        else:
            if self.right:
                self.right.put(key, value, parent=self)
            else:
                self.right = BSTNode(key, value)

        # Rebalance.
        left_weight, right_weight = self.update_weight()
        if (right_weight / 4) > left_weight:
            return self.rotate_left(parent)
        elif (left_weight / 4) > right_weight:
            return self.rotate_right(parent)

        return self

    def rotate_left(self, parent: BSTNode | None = None) -> BSTNode:
        """Returns the node this one should be replaced with."""
        old_right = self.right
        self.right = old_right.left
        old_right.left = self

        self.update_weight()
        old_right.update_weight()

        if parent:
            if old_right.key < parent.key:
                parent.left = old_right
            else:
                parent.right = old_right

        return old_right

    def rotate_right(self, parent: BSTNode | None = None) -> BSTNode:
        old_left = self.left
        self.left = old_left.right
        old_left.right = self

        self.update_weight()
        old_left.update_weight()

        if parent:
            if old_left.key < parent.key:
                parent.left = old_left
            else:
                parent.right = old_left

        return old_left

    def update_weight(self) -> tuple[int, int]:
        left_weight = self.left.weight if self.left else 0
        right_weight = self.right.weight if self.right else 0
        self.weight = left_weight + right_weight + 1
        return left_weight, right_weight

    def remove(self, key: Any) -> BSTNode:
        """Returns the node this one should be replaced with."""
        if key == self.key:
            # If there is only 1 child, move it up.
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right

            # Swap with max node in left, and remove this node again.
            max_node = self.left.get_max_node()

            self.key, max_node.key = max_node.key, self.key
            self.value, max_node.value = max_node.value, self.value

            self.left = self.remove(key)

        elif (key < self.key) and self.left:
            self.left = self.left.remove(key)
        elif (key > self.key) and self.right:
            self.right = self.right.remove(key)
        else:
            raise KeyError(f"Key {key} not in BST.")

        return self

    def get_max_node(self) -> BSTNode:
        if self.right is None:
            return self
        return self.right.get_max_node()

    def in_order(self) -> Iterator[tuple]:
        if self.left:
            yield from self.left.in_order()

        yield (self.key, self.value)

        if self.right:
            yield from self.right.in_order()
