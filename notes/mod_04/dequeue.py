class Dequeue:
    """Push and pop from both sides."""

    def __init__(self):
        self.items = list()

    def add_first(self, item):
        self.items.insert(0, item)  # O(n).

    def add_last(self, item):
        self.items.append(item)  # O(1).

    def remove_first(self):
        return self.items.pop(0)  # O(n).

    def remove_last(self):
        return self.items.pop()  # O(1).


if __name__ == "__main__":
    dq = Dequeue()

    for i in range(10):
        dq.add_first(i)
    for i in range(10):
        print(dq.remove_first())
    print()

    for i in range(10):
        dq.add_last(i)
    for i in range(10):
        print(dq.remove_last())
