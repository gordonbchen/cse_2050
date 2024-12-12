from __future__ import annotations

from typing import Any, Iterator


class BSTNode:
    def __init__(self, key: Any, value: Any) -> None:
        self.key = key
        self.value = value

        self.left = None
        self.right = None

        self.height = 0

    def get(self, key: Any) -> Any:
        if self.key == key:
            return self.value

        elif (key < self.key) and self.left:
            return self.left.get(key)
        elif (key > self.key) and self.right:
            return self.right.get(key)

        raise KeyError(f"Failed to find key {key}")

    def put(self, key: Any, value: Any) -> BSTNode:
        if self.key == key:
            self.value = value

        elif key < self.key:
            self.left = self.left.put(key, value) if self.left else BSTNode(key, value)
        elif key > self.key:
            self.right = self.right.put(key, value) if self.right else BSTNode(key, value)

        left_height, right_height = self.calc_heights()
        misbalance = left_height - right_height
        if misbalance > 1:
            h_outer = self.left.left.height if self.left.left else -1
            h_inner = self.left.right.height if self.left.right else -1

            if h_inner > h_outer:
                self.left = self.left.rotate_left()

            return self.rotate_right()
        elif misbalance < -1:
            h_outer = self.right.right.height if self.right.right else -1
            h_inner = self.right.left.height if self.right.left else -1

            if h_inner > h_outer:
                self.right = self.right.rotate_right()

            return self.rotate_left()

        return self

    def calc_heights(self) -> tuple[int, int]:
        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1

        self.height = max(left_height + right_height) + 1

        return left_height, right_height

    def rotate_right(self) -> BSTNode:
        old_left = self.left
        self.left = old_left.right
        old_left.right = self

        self.calc_heights()
        old_left.calc_heights()
        return old_left

    def rotate_left(self) -> BSTNode:
        old_right = self.right
        self.right = old_right.left
        old_right.left = self

        self.calc_heights()
        old_right.calc_heights()
        return old_right

    def remove(self, key: Any) -> BSTNode:
        if self.key == key:
            # Move the existing child node (or None) up.
            if not self.left:
                return self.right
            if not self.right:
                return self.left

            # Both children exist. Find the max on the left subtree.
            # Swap with the max, and call remove on the left subtree.
            max_node = self.left.get_max_node()

            self.key, max_node.key = max_node.key, self.key
            self.value, max_node.value = max_node.value, self.value

            self.left = self.left.remove(key)

        elif (key < self.key) and self.left:
            self.left = self.left.remove(key)
        elif (key > self.key) and self.right:
            self.right = self.right.remove(key)

        else:
            raise KeyError(f"Failed to find key {key}.")

        return self

    def get_max_node(self) -> BSTNode:
        if self.right:
            return self.right.get_max_node()
        return self

    def floor(self, key: Any) -> Any | None:
        if self.key == key:
            return self.value

        elif key < self.key:
            return self.left.floor(key) if self.left else None
        else:
            if self.right:
                right_floor = self.right.floor(key)
                return right_floor if right_floor else self.value
            else:
                return self.value

    def in_order(self) -> Iterator[tuple[Any, Any]]:
        if self.left:
            yield from self.left.in_order()

        yield (self.key, self.value)

        if self.right:
            yield from self.right.in_order()
