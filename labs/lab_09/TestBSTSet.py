import unittest
from BSTSet import BSTSet


class TestBSTSet(unittest.TestCase):
    def testPut(self):
        """Tests that put operation works with correct ordering"""
        bst = BSTSet()

        # In-order puts
        # Create a balanced tree with 7 nodes
        #       3
        #    /     \
        #   1       5
        #  / \     / \
        # 0   2   4   6
        for i in [3, 1, 0, 2, 5, 4, 6]:
            bst.put(i)

        ino = []
        for item in bst.in_order():
            ino.append(item)
        assert ino == [0, 1, 2, 3, 4, 5, 6]

    def test_put_duplicates(self):
        """Tests that put operation with duplicate keys."""
        bst = BSTSet()

        # In-order puts
        # Create a balanced tree with 7 nodes
        #       3
        #    /     \
        #   1       5
        #  / \     / \
        # 0   2   4   6
        for _ in range(2):
            for i in [3, 1, 0, 2, 5, 4, 6]:
                bst.put(i)

        ino = []
        for item in bst.in_order():
            ino.append(item)
        assert ino == [0, 1, 2, 3, 4, 5, 6]

        bst = BSTSet()

        # In-order puts
        # Create a balanced tree with 7 nodes
        #       3
        #    /     \
        #   1       5
        #  / \     / \
        # 0   2   4   6
        for i in [3, 1, 0, 2, 5, 4, 6]:
            bst.put(i)

        bst.put(3)
        bst.put(5)
        bst.put(6)

        ino = []
        for item in bst.in_order():
            ino.append(item)
        assert ino == [0, 1, 2, 3, 4, 5, 6]

    def test_preorder(self):
        """Tests that preorder traversal works in correct direction"""
        # Unbalanced tree
        # 0
        #  `-1
        #     `-2
        #        `-3
        # Build Set
        bst = BSTSet()
        for i in [0, 1, 2, 3]:
            bst.put(i)

        # Traverse Set
        preo = []
        for item in bst.pre_order():
            preo.append(item)
        assert preo == [0, 1, 2, 3]

        # Create a balanced tree with 7 nodes
        #       3
        #    /     \
        #   1       5
        #  / \     / \
        # 0   2   4   6
        # Build Set
        bst = BSTSet()
        for i in [3, 1, 0, 2, 5, 4, 6]:
            bst.put(i)

        # Traverse Set
        preo = []
        for item in bst.pre_order():
            preo.append(item)
        assert preo == [3, 1, 0, 2, 5, 4, 6]

    def test_postorder(self):
        """Tests that preorder traversal works in correct direction"""
        # Unbalanced tree
        # 0
        #  `-1
        #     `-2
        #        `-3
        # Build Set
        bst = BSTSet()
        for i in [0, 1, 2, 3]:
            bst.put(i)

        # Traverse Set
        posto = []
        for item in bst.post_order():
            posto.append(item)
        assert posto == [3, 2, 1, 0]

        # Create a balanced tree with 7 nodes
        #       3
        #    /     \
        #   1       5
        #  / \     / \
        # 0   2   4   6
        # Build Set
        bst = BSTSet()
        for i in [3, 1, 0, 2, 5, 4, 6]:
            bst.put(i)

        # Traverse Set
        posto = []
        for item in bst.post_order():
            posto.append(item)
        assert posto == [0, 2, 1, 4, 6, 5, 3]

    def test_empty(self):
        """Test iterating through an empty BST."""
        bst = BSTSet()

        items = []
        for item in bst.in_order():
            items.append(item)
        self.assertEqual(len(items), 0)

        items = []
        for item in bst.in_order():
            items.append(item)
        self.assertEqual(len(items), 0)

        items = []
        for item in bst.in_order():
            items.append(item)
        self.assertEqual(len(items), 0)


if __name__ == "__main__":
    unittest.main()
