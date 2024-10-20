from __future__ import annotations

from typing import Any


class LLNode:
    def __init__(self, data: Any, link: LLNode = None):
        """A linked list node"""
        self.data = data
        self.link = link

    def __len__(self) -> int:
        """Return the length of the linked list."""
        if self.link is None:
            return 1
        return 1 + len(self.link)

    def __repr__(self) -> str:
        """Return a string representation of the node."""
        return f"LLNode({self.data})"

    def get_tail(self) -> Any:
        """Return the data at the tail of the linked list."""
        if self.link is None:
            return self.data
        return self.link.get_tail()

    def add_last(self, item: Any) -> None:
        """Add an item to the end of the linked list."""
        if self.link is None:
            self.link = LLNode(item)
        self.link.add_last(item)

    def sum_all(self) -> Any:
        """Return the sum of all items in the linked list."""
        if self.link is None:
            return self.data
        return self.data + self.link.sum_all()

    def contains(self, item: Any) -> bool:
        """Return True if the linked list contains the item."""
        if self.data == item:
            return True

        if self.link is not None:
            return self.link.contains(item)

        return False

    def remove_all(self, item: Any) -> LLNode | None:
        """Remove all nodes containing a given item. Return the new head."""
        if self.link is None:
            if self.data == item:
                return None
            return self

        self.link = self.link.remove_all()
        if self.data == item:
            return self.link
        return self

    def reverse(self, prev: LLNode | None) -> LLNode | None:
        """Reverse the linked list and return the new head."""
        prev_link = self.link
        self.link = prev

        if prev_link is None:
            return self

        return prev_link.reverse(self)


#########################################################
# No changes below this point - all your work should be #
# in LLNode.                                            #
#########################################################
class LinkedList:
    def __init__(self, items=None):
        """Initializes a new empty LinkedList"""
        self._head = None
        if items is not None:
            for item in items:
                self.add_last(item)  # use add_last() to maintain ordering

    def add_first(self, item):
        """Adds to beginning of Linked List"""
        self._head = LLNode(item, self._head)

    def remove_first(self):
        """Removes and returns first item"""
        # Edge case
        if self._head is None:
            raise RuntimeError("Cannot remove from an empty list.")
        item = self._head.data  # retrieve data
        self._head = self._head.link  # update head
        return item

    # For demonstration and debug purposes: Prints all the elements
    def __repr__(self):
        """Recursively prints the Linked List"""
        return repr(self._head)

    def __len__(self):
        """Returns the number of nodes in Linked List"""
        return len(self._head) if self._head else 0

    def __contains__(self, item):
        """Returns True if item is in Linked List. Returns False otherwise."""
        if self._head is None:
            return False
        return self._head.contains(item)

    def add_last(self, item):
        """Adds item to end of Linked List"""
        if self._head is None:
            return self.add_first(item)
        self._head.add_last(item)

    def sum_all(self):
        """Returns sum of all items in Linked List"""
        return self._head.sum_all() if self._head else 0

    def remove_all(self, item):
        """Removes all occurrences of item from Linked List"""
        if self._head is not None:
            self._head = self._head.remove_all(item)

    # Reverses the list in linear time, no copying of the data
    def reverse(self):
        """Reverses linked list"""
        # Note that LLNode.reverse() should return the new head
        if self._head is not None:
            self._head = self._head.reverse()

    def get_tail(self):
        """Returns the item stored in tail"""
        return self._head.get_tail() if self._head else None
