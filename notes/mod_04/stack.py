from typing import Any


class Stack:
    """Last in first out stack."""

    def __init__(self, items: list = None) -> None:
        """Initialize the stack."""
        self.items = list() if items is None else items

    def push(self, item) -> None:
        """Add item to the top of the stack."""
        self.items.append(item)

    def pop(self) -> Any:
        """Pop top item from stack."""
        return self.items.pop()

    def peek(self) -> Any:
        """Get but don't remove top item from stack."""
        return self.items[-1]

    def size(self) -> int:
        """Return the stack size."""
        return len(self.items)

    def is_empty(self) -> bool:
        """Return True if the stack is empty."""
        return len(self.items) == 0


if __name__ == "__main__":
    stack = Stack([1, 2, 3, 4])
    print(stack.items)

    print(stack.pop())
    print(stack.items)

    stack.push(99)
    print(stack.size())
    print(stack.items)

    print(stack.peek())
    print(stack.items)

    print(stack.is_empty())
