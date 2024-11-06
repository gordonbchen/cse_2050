from __future__ import annotations

from typing import Any, Iterator


class Node:
    def __init__(self, parent: Node | None, data: Any) -> None:
        """Initialize the node."""
        self.parent = parent
        self.data = data
        self.children = []

    def add_child(self, data: Any) -> Node:
        """Add a child node."""
        new_child = Node(self, data)
        self.children.append(new_child)
        return new_child

    def pre_order(self) -> Iterator[Node]:
        """Traverse the tree in pre-order. Root, left, right."""
        yield self
        for child in self.children:
            for node in child.pre_order():
                yield node

    def post_order(self) -> Iterator[Node]:
        """Traverse the tree in post-order. Left, right, root."""
        for child in self.children:
            for node in child.post_order():
                yield node
        yield self


if __name__ == "__main__":
    #    root
    #    /  \
    #   x1   x2
    #  /  \
    # y1  y2
    root = Node(None, "root")
    x1 = root.add_child("x1")
    x2 = root.add_child("x2")
    y1 = x1.add_child("y1")
    y2 = x1.add_child("y2")

    print("Pre-order")
    for i in root.pre_order():
        print(i.data)

    print("\nPost-order")
    for i in root.post_order():
        print(i.data)
