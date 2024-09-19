from __future__ import annotations

from typing import Optional, Any, Iterable


class Node:
    """A node in a linked list."""

    def __init__(self, item: Any, link: Optional[Node] = None) -> None:
        """Initialize node."""
        self.item = item
        self.link = link

    def __repr__(self) -> str:
        """Return a str representation of the node."""
        return f"Node({self.item})"


class LinkedList:
    """A linked list."""

    def __init__(self, items: Optional[Iterable] = None) -> None:
        """Initialize linked list."""
        self._head = None
        self._tail = None
        self._len = 0

        if items is not None:
            for item in items:
                self.add_last(item)

    def __len__(self) -> int:
        """Return the length of the linked list."""
        return self._len

    def get_head(self) -> Any:
        """Get the item at the head of the linked list."""
        if self._head is None:
            return None
        return self._head.item

    def get_tail(self) -> Any:
        """Get the item at the tail of the linked list."""
        if self._tail is None:
            return None
        return self._tail.item

    def add_first(self, item: Any) -> None:
        """Add an item to the start of the linked list."""
        new_node = Node(item)
        if len(self) == 0:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.link = self._head
            self._head = new_node

        self._len += 1

    def add_last(self, item: Any) -> None:
        """Add an item to the end of the linked list."""
        new_node = Node(item)
        if len(self) == 0:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.link = new_node
            self._tail = new_node

        self._len += 1

    def remove_first(self) -> Any:
        """Remove and return the first item from the linked list."""
        if len(self) == 0:
            raise RuntimeError("Cannot remove first item from empty LinkedList.")

        item = self._head.item

        self._head = self._head.link
        if len(self) == 1:
            self._tail = None

        self._len -= 1
        return item

    def remove_last(self) -> Any:
        """Remove and return the last item from the linked list."""
        if len(self) == 0:
            raise RuntimeError("Cannot remove last item from empty LinkedList.")

        item = self._tail.item

        if len(self) == 1:
            self._head = None
            self._tail = None
        else:
            # Find node before tail and unlink tail.
            curr = self._head
            while curr.link != self._tail:
                curr = curr.link
            self._tail = curr

        self._len -= 1
        return item
