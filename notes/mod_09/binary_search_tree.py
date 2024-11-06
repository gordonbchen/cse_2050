from __future__ import annotations

from typing import Any


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
        """Get the value associated with the key."""
        if self.key == key:
            return self.value
        elif (self.key < key) and (self.right is not None):
            return self.right.get(key)
        elif (self.key > key) and (self.left is not None):
            return self.left.get(key)

        raise KeyError(f"Key {key} not found in tree.")

    def put(self, key: Any, value: Any, parent: BSTNode | None = None) -> None:
        if self.key == key:
            self.value = value
        elif self.key < key:
            if self.right:
                self.right.put(key, value, parent=self)
            else:
                self.right = BSTNode(key, value)
        else:
            if self.left:
                self.left.put(key, value, parent=self)
            else:
                self.left = BSTNode(key, value)


if __name__ == "__main__":
    pass
