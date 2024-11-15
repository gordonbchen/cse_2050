from entry import Entry
from heap import Heap
import unittest, random
random.seed(658) # fix seed so we always fail with the same numbers (makes debugging easier)

###############################################################################
# We test some private attributes here for the sake of making this assignment #
# autograded. In practice, you should only test the public interface.         #
# #############################################################################

class TestHeap(unittest.TestCase):
    def assertHeap(self, h):
        """Checks that h._idx is correct and that h._L is heap-ordered"""
        # Verify that the item:index dictionary `h._idx` is correct
        for i in range(len(h)):
            item = h._L[i].item
            self.assertEqual(h._idx[item], i)
        
        for item, idx in h._idx.items():
            self.assertEqual(h._L[idx].item, item)

        # Verify that array is heap-ordered
        self.assertTrue(self.is_heap_ordered(h))

    def is_heap_ordered(self, h, idx=0):
        """Returns True (False) if every branch of heap h is heap-ordered"""
        idx_left = h.idx_left(idx) 
        idx_right = h.idx_right(idx)

        # recursively call on left and right
        if idx_left is not None:
            if h._L[idx] > h._L[idx_left] or not self.is_heap_ordered(h, idx_left): return False
            
        if idx_right is not None:
            if h._L[idx] > h._L[idx_right] or not self.is_heap_ordered(h, idx_right): return False

        # everything at subheap rooted here is heap sorted 
        return True
    
    def test_idx_par(self):
        """Tests that we get the correct parent for a range of indices"""
        h = Heap()
        for i in range(15):
            h.insert(item=str(i), priority=i)

        self.assertEqual(h.idx_parent(0), None)  # level 0

        self.assertEqual(h.idx_parent(1), 0)     # level 1
        self.assertEqual(h.idx_parent(2), 0)

        self.assertEqual(h.idx_parent(3), 1)     # level 2
        self.assertEqual(h.idx_parent(4), 1)
        self.assertEqual(h.idx_parent(5), 2)
        self.assertEqual(h.idx_parent(6), 2)

        self.assertEqual(h.idx_parent(7), 3)     # level 3
        self.assertEqual(h.idx_parent(8), 3)
        self.assertEqual(h.idx_parent(9), 4)
        self.assertEqual(h.idx_parent(10), 4)
        self.assertEqual(h.idx_parent(11), 5)
        self.assertEqual(h.idx_parent(12), 5)
        self.assertEqual(h.idx_parent(13), 6)
        self.assertEqual(h.idx_parent(14), 6)

    def test_idx_left(self):
        """Tests that we get the correct left child for a range of indices"""
        h = Heap()
        for i in range(30):
            h.insert(item=str(i), priority=i)

        self.assertEqual(h.idx_left(0), 1)     # level 0

        self.assertEqual(h.idx_left(1), 3)     # level 1
        self.assertEqual(h.idx_left(2), 5)

        self.assertEqual(h.idx_left(3), 7)     # level 2
        self.assertEqual(h.idx_left(4), 9)
        self.assertEqual(h.idx_left(5), 11)
        self.assertEqual(h.idx_left(6), 13)

        self.assertEqual(h.idx_left(7), 15)     # level 3
        self.assertEqual(h.idx_left(8), 17)
        self.assertEqual(h.idx_left(9), 19)
        self.assertEqual(h.idx_left(10), 21)
        self.assertEqual(h.idx_left(11), 23)
        self.assertEqual(h.idx_left(12), 25)
        self.assertEqual(h.idx_left(13), 27)
        self.assertEqual(h.idx_left(14), 29)

    def test_idx_right(self):
        """Tests that we get the correct right child for a range of indices"""
        h = Heap()
        for i in range(31):
            h.insert(item=str(i), priority=i)
        
        self.assertEqual(h.idx_right(0), 2)     # level 0

        self.assertEqual(h.idx_right(1), 4)     # level 1
        self.assertEqual(h.idx_right(2), 6)

        self.assertEqual(h.idx_right(3), 8)     # level 2
        self.assertEqual(h.idx_right(4), 10)
        self.assertEqual(h.idx_right(5), 12)
        self.assertEqual(h.idx_right(6), 14)

        self.assertEqual(h.idx_right(7), 16)     # level 3
        self.assertEqual(h.idx_right(8), 18)
        self.assertEqual(h.idx_right(9), 20)
        self.assertEqual(h.idx_right(10), 22)
        self.assertEqual(h.idx_right(11), 24)
        self.assertEqual(h.idx_right(12), 26)
        self.assertEqual(h.idx_right(13), 28)
        self.assertEqual(h.idx_right(14), 30)

    def test_insert(self):
        """Tests that we can add items and stay heap-ordered"""
        h = Heap()
        n = 100
        for i in range(n):
            self.assertEqual(len(h), i)         # before adding

            priority = random.randint(0, 100)       # generate random entry
            h.insert(item=i, priority=priority)
            self.assertHeap(h)

    def test_remove_min(self):
        """Tests that we can remove_min in correct order and maintain heap-ordering"""
        h = Heap()
        n = 100
        for i in range(n):
            self.assertEqual(len(h), i)         # before adding

            priority = random.randint(0, 100)       # generate random entry
            priority = i
            h.insert(item=i, priority=priority)

            self.assertHeap(h)

            # self.assertTrue(self.is_heap_ordered(h)) # after adding


        old_entry = Entry(item=None, priority=float('-inf'))
        for i in range(n):
            self.assertEqual(len(h), n-i)                                       # before removing
            new_entry = h.remove_min()                                          # remove

            self.assertHeap(h)   # CHEATER METHOD - typically we don't test this explicitly
            
            self.assertGreaterEqual(new_entry.priority, old_entry.priority)     # compare
            old_entry = new_entry                                               # prepare for next loop

    def test_iter(self):
        """Checks that we can iterate through heap"""
        h = Heap()
        n = 100
        for i in range(n):
            h.insert(item=i, priority=random.randint(0, n))
        
        old_priority = float('-inf')
        for entry in h:
            priority = entry.priority
            self.assertLessEqual(old_priority, priority)
            old_priority=priority

            self.assertHeap(h)

    def test_change_priority(self):
        """Checks that we can arbitrarily change the priority of items"""         
        h = Heap()

        # Construct a heap with 100 items, priority 0->100
        n = 100
        for i in range(n):
            h.insert(item=i, priority=i)

        # Change each priority, but items stay the same
        for i in range(n):
            new_position = h.change_priority(item=i, priority = random.randint(0, n)) 
            self.assertHeap(h)
            self.assertEqual(h._L[new_position].item, i)    # check item is at the indicated position
            self.assertEqual(h._idx[i], new_position)     # check that new_position is updated correctly

        # Repeat to verify it works on non-sorted list
        for i in range(n):
            new_position = h.change_priority(item=i, priority = random.randint(0, n)) 
            self.assertHeap(h)
            self.assertEqual(h._L[new_position].item, i)    # check item is at the indicated position
            self.assertEqual(h._idx[i], new_position)     # check that new_position is updated correctly

    def test_heapify(self):
        """Tests that we can heapify an unordered list of entries"""
        n = 100

        for trial in range(10):
            entries = [Entry(item=i, priority=random.randint(0, n)) for i in range(n)]
            h = Heap.heapify(entries)
            self.assertHeap(h)


if __name__ == '__main__':
    unittest.main()