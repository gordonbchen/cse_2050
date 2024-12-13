from __future__ import annotations

from typing import Any, Iterator


class BSTNode:
    def __init__(self, key: Any, value: Any) -> None:
        self.key = key
        self.value = value

        self.left = None
        self.right = None

        self.weight = 0

    def get(self, key: Any) -> Any:
        if key == self.key:
            return self.value
        elif (key < self.key) and self.left:
            return self.left.get(key)
        elif (key > self.key) and self.right:
            return self.right.get(key)

        raise KeyError(f"Failed to find key {key}.")

    def put(self, key: Any, value: Any) -> BSTNode:
        if key == self.key:
            self.value = value
        elif key < self.key:
            self.left = self.left.put(key, value) if self.left else BSTNode(key, value)
        else:
            self.right = self.right.put(key, value) if self.right else BSTNode(key, value)

        left_weight, right_weight = self._calc_weight()
        if (max(left_weight, right_weight) / 4) > min(left_weight, right_weight):
            if left_weight > right_weight:
                return self.rotate_right()
            else:
                return self.rotate_left()

        return self

    def remove(self, key: Any) -> BSTNode:
        if key == self.key:
            if not self.left:
                return self.right
            if not self.right:
                return self.left

            max_left = self.left._get_max_node()

            self.key, max_left.key = max_left.key, self.key
            self.value, max_left.value = max_left.value, self.value

            self.left = self.left.remove(key)

        elif (key < self.key) and self.left:
            self.left = self.left.remove(key)
        elif (key > self.key) and self.right:
            self.right = self.right.remove(key)
        else:
            raise KeyError(f"Failed to find key {key}.")

        return self

    def in_order(self) -> Iterator[tuple[Any, Any]]:
        if self.left:
            yield from self.left.in_order()

        yield (self.key, self.value)

        if self.right:
            yield from self.right.in_order()

    def floor(self, key: Any) -> Any:
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

    def _calc_weight(self) -> tuple[int, int]:
        left_weight = self.left.weight if self.left else 0
        right_weight = self.right.weight if self.right else 0

        self.weight = left_weight + right_weight + 1
        return left_weight, right_weight

    def _rotate_right(self) -> BSTNode:
        old_left = self.left
        self.left = old_left.right
        old_left.right = self

        self._calc_weight()
        old_left._calc_weight()

        return old_left

    def _rotate_left(self) -> BSTNode:
        old_right = self.right
        self.right = old_right.left
        old_right.left = self

        self._calc_weight()
        old_right._calc_weight()

        return old_right

    def _get_max_node(self) -> BSTNode:
        return self.right._get_max_node() if self.right else self
