class Queue:
    """First in first out."""

    def __init__(self):
        self.items = list()

    def enqueue(self, item):
        self.items.append(item)  # O(1).

    def dequeue(self):
        return self.items.pop(0)  # O(n).


if __name__ == "__main__":
    q = Queue()

    for i in range(10):
        q.enqueue(i)

    for i in range(10):
        print(q.dequeue())
