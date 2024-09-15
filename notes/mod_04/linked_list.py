from typing import Any


class Node:
    def __init__(self, item, next_node=None) -> None:
        self.item = item
        self.next_node = next_node


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def add_first(self, item) -> None:
        self.head = Node(item, next_node=self.head)

    def remove_first(self) -> Any:
        if self.head is None:
            raise ValueError("No more nodes to remove.")
        old_head = self.head
        self.head = self.head.next_node
        return old_head


if __name__ == "__main__":
    ll = LinkedList()
    print(ll.head)
    print()

    for i in range(10):
        ll.add_first(i)

    for i in range(10):
        print(ll.remove_first().item)

    print()
    print(ll.head)

    try:
        a = ll.remove_first().item
    except ValueError as e:
        print(e)
