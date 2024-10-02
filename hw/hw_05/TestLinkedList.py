from recursive_linkedlist import RecursiveLinkedList as RLL
import unittest


###############################################################################
# Factory's are classes used to make other classes. All of our different      #
# LinkedList implementations (with a tail pointer, without a tail pointer,    #
# doubly linked, recursive, ...) have the same public interface, so their     #
# tests are identical. We write the tests in a factory, and inherit this      #
# factory *and* unittest.TestCase anytime we want to run these tests. The     #
# only thing our test calsses need to do is call Factory.setUp() and pass the #
# appropriate data structure, see below.                                      #
###############################################################################
class TestLinkedFactory:
    def assertList(self, _list, _len, _head, _tail):
        """Checks that list has expected length, head, and tail data"""
        self.assertEqual(len(_list), _len)
        self.assertEqual(_list.get_head(), _head)
        self.assertEqual(_list.get_tail(), _tail)

    def setUp(self, _class):
        """Runs before each method, specifies which class is using this factory"""
        self._class = _class
        self.ll1 = self._class()
        self.ll_big = self._class()
        for i in range(2000):
            self.ll_big.add_first(i)

    def test_init(self):
        """Creates a new, empty list"""
        self.assertEqual(len(self.ll1), 0)
        self.assertEqual(self.ll1.get_head(), None)
        self.assertEqual(self.ll1.get_tail(), None)

    def test_init_with_items(self):
        """Creates a new list with items specified, maintains correct ordering"""
        self.ll1 = self._class(range(10))
        self.assertList(self.ll1, _len=10, _head=0, _tail=9)

    def test_add_first_one(self):
        """Adds a single item to a list"""
        self.ll1.add_first("jake")
        self.assertList(self.ll1, _len=1, _head="jake", _tail="jake")

    def test_add_first_ten(self):
        """Calls add_first 10 times in a row"""
        n = 10
        for i in range(n):
            self.ll1.add_first(i)
            self.assertList(self.ll1, _len=i + 1, _head=i, _tail=0)

    def test_remove_first_one(self):
        """Removes one node from a list with only one node"""
        self.ll1 = self._class(["jake"])
        self.assertEqual(self.ll1.remove_first(), "jake")
        self.assertList(self.ll1, _len=0, _head=None, _tail=None)

    def test_add_first_remove_first_ten(self):
        """Adds 10 items to front, then removes 10 items from front"""
        n = 10
        for i in range(n):
            self.ll1.add_first(i)

        for i in range(n):
            self.assertList(self.ll1, _len=n - i, _head=n - 1 - i, _tail=0)
            self.assertEqual(self.ll1.remove_first(), n - 1 - i)

        self.assertList(self.ll1, _len=0, _head=None, _tail=None)

    def test_add_last_one(self):
        """Calls add_last one time"""
        self.ll1.add_last("jake")
        self.assertList(self.ll1, _len=1, _head="jake", _tail="jake")

    def test_add_last_ten(self):
        """Calls add_last ten times in a row"""
        n = 10
        for i in range(n):
            self.ll1.add_last(i)
            self.assertList(self.ll1, _len=i + 1, _head=0, _tail=i)

    def test_add_last_remove_last(self):
        """Adds 10 items to end, then removes 10 items from end"""
        n = 10
        for i in range(n):
            self.ll1.add_last(i)

        for i in range(n):
            self.assertList(self.ll1, _len=n - i, _head=0, _tail=n - 1 - i)
            self.assertEqual(self.ll1.remove_last(), n - 1 - i)

        self.assertList(self.ll1, _len=0, _head=None, _tail=None)

    def test_reverse(self):
        """Builds a list of 10 items, reversing it twice after every addition"""
        for i in range(10):
            self.ll1.add_first(i)
            self.assertList(self.ll1, _len=i + 1, _head=i, _tail=0)

            self.ll1.reverse()
            self.assertList(self.ll1, _len=i + 1, _head=0, _tail=i)

            self.ll1.reverse()
            self.assertList(self.ll1, _len=i + 1, _head=i, _tail=0)

    def test_total(self):
        """Tests that we can add up all items in list recursively"""
        for i in range(10):
            self.ll1.add_first(i)
            self.assertEqual(self.ll1.total(), i / 2 * (i + 1))

        ll2 = self._class([5, 7, -2])
        self.assertEqual(ll2.total(), 10)

    def test_len_recursive(self):
        """Tests that length is implemented recursively"""
        with self.assertRaises(RecursionError):
            len(self.ll_big)

    def test_add_last_recursive(self):
        """Tests that add_last is implemented recursively"""
        with self.assertRaises(RecursionError):
            len(self.ll_big.add_last(0))

    def test_remove_last_recursive(self):
        """Tests that remove_last is implemented recursively"""
        with self.assertRaises(RecursionError):
            len(self.ll_big.remove_last())

    def test_get_tail_recursive(self):
        """Tests that get_tail is implemented recursively"""
        with self.assertRaises(RecursionError):
            len(self.ll_big.get_tail())

    def test_reverse_recursive(self):
        """Tests that reverse is implemented recursively"""
        with self.assertRaises(RecursionError):
            len(self.ll_big.reverse())


class TestRecursiveLinkedList(TestLinkedFactory, unittest.TestCase):
    """Runs all tests above on a Recursive LinkedList"""

    def setUp(self):
        """
        All tests are implemented in TestLinkedFactory,
        this just specifies which class to use.
        """
        return TestLinkedFactory.setUp(self, RLL)


# If we wanted, we could also test other implementations with the same interface:
# class TestDoublyLinkedList(TestLinkedFactory, unittest.TestCase):
#     """Runs all tests on a DLL"""
#     def setUp(self):
#         return TestLinkedFactory.setUp(self, DoublyLinkedList)
#
# class TestLinkedListTail(TestLinkedFactory, unittest.TestCase):
#     """Runs all tests on a LL w/ tail pointer"""
#     def setUp(self):
#         return TestLinkedFactory.setUp(self, LinkedListTail)

if __name__ == "__main__":
    unittest.main()
