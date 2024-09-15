from typing import Any

from linked_list import Node


class DoubleNode(Node):
    def __init__(self, item, next_node=None, prev_node=None) -> None:
        super().__init__(item, next_node)
        self.prev_node = prev_node


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add_first(self, item) -> None:
        new_node = DoubleNode(item, next_node=self.head)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev_node = new_node
            self.head = new_node

    def add_last(self, item) -> None:
        new_node = DoubleNode(item, prev_node=self.tail)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def remove_first(self) -> Any:
        if self.head is None:
            raise ValueError("No more nodes to remove.")

        removed_item = self.head.item
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next_node
            self.head.prev_node = None
        return removed_item

    def remove_last(self) -> Any:
        if self.tail is None:
            raise ValueError("No more nodes to remove.")

        removed_item = self.tail.item
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev_node
            self.tail.next_node = None
        return removed_item


if __name__ == "__main__":
    dll = DoublyLinkedList()
    print(dll.head, dll.tail)
    print()

    dll.add_last(1)
    print(dll.head.item, dll.tail.item)

    dll.add_first(0)
    print(dll.head.item, dll.tail.item)

    print(dll.remove_first())
    print(dll.head.item, dll.tail.item)

    print(dll.remove_last())
    print(dll.head, dll.tail)
