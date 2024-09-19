import unittest

from linkedlist import Node, LinkedList


class TestNode(unittest.TestCase):
    """Tests for the Node class."""

    def test_init(self):
        """Test node initialization."""
        n1 = Node("a")
        n2 = Node("b", link=n1)

        self.assertEqual(n1.item, "a")
        self.assertEqual(n1.link, None)

        self.assertEqual(n2.item, "b")
        self.assertEqual(n2.link, n1)

    def test_repr(self):
        """Test node str representation."""
        n1 = Node("a")
        self.assertEqual(repr(n1), "Node(a)")


class TestLinkedList(unittest.TestCase):
    """Tests for the LinkedList class."""

    def test_empty_init(self):
        """Test empty LinkedList initialization."""
        ll = LinkedList()
        self.assertEqual(len(ll), 0)
        self.assertEqual(ll.get_head(), None)
        self.assertEqual(ll.get_tail(), None)

    def test_add_last(self):
        """Test adding an item to the end of the linked list."""
        items = ["a", "b", "c"]
        ll = LinkedList()

        for i, item in enumerate(items):
            ll.add_last(item)
            self.assertEqual(len(ll), i + 1)
            self.assertEqual(ll.get_head(), "a")
            self.assertEqual(ll.get_tail(), item)

    def test_add_first(self):
        """Test adding an item to the start of the linked list."""
        items = ["a", "b", "c"]
        ll = LinkedList()

        for i, item in enumerate(items):
            ll.add_first(item)
            self.assertEqual(len(ll), i + 1)
            self.assertEqual(ll.get_head(), item)
            self.assertEqual(ll.get_tail(), "a")

    def test_init(self):
        """Test non-empty LinkedList initalization."""
        ll1 = LinkedList(list("abc"))
        self.assertEqual(len(ll1), 3)
        self.assertEqual(ll1.get_head(), "a")
        self.assertEqual(ll1.get_tail(), "c")

        ll2 = LinkedList(range(10))
        self.assertEqual(len(ll2), 10)
        self.assertEqual(ll2.get_head(), 0)
        self.assertEqual(ll2.get_tail(), 9)

    def test_remove_first(self):
        """Test removing an item from the beginning of the linked list."""
        items = ["a", "b", "c"]
        ll = LinkedList(items)

        for i, item in enumerate(items):
            self.assertEqual(ll.remove_first(), item)
            self.assertEqual(len(ll), len(items) - 1 - i)
            self.assertEqual(ll.get_head(), items[i + 1] if len(ll) != 0 else None)
            self.assertEqual(ll.get_tail(), "c" if len(ll) != 0 else None)

        with self.assertRaises(RuntimeError):
            ll.remove_first()

    def test_remove_last(self):
        """Test removing an item from the end of the linked list."""
        items = ["a", "b", "c"]
        ll = LinkedList(items)

        for i in range(len(items)):
            self.assertEqual(ll.remove_last(), items[-1 - i])
            self.assertEqual(len(ll), len(items) - 1 - i)
            self.assertEqual(ll.get_head(), "a" if len(ll) != 0 else None)
            self.assertEqual(ll.get_tail(), items[-2 - i] if len(ll) != 0 else None)

        with self.assertRaises(RuntimeError):
            ll.remove_last()


if __name__ == "__main__":
    unittest.main()
