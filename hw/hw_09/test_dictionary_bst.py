import unittest

from dictionary_bst import DictionaryBST


class DictionaryBSTTests(unittest.TestCase):
    """Tests for DictionaryBST."""

    def test_insert_single(self) -> None:
        """Test inserting a single entry into the BST."""
        bst = DictionaryBST()
        self.assertEqual(bst.print_alphabetical(), [])

        bst.insert("hi", "hello")
        self.assertEqual(bst.print_alphabetical(), [("hi", "hello")])

    def test_search(self) -> None:
        """Test searching for entries in the BST."""
        bst = DictionaryBST()

        self.assertEqual(bst.search("hi"), None)

        bst.insert("hi", "hello")
        self.assertEqual(bst.search("hi"), "hello")
        self.assertEqual(bst.search("hello"), None)

        for word, meaning in self.get_test_words_meanings():
            bst.insert(word, meaning)

        for word, meaning in self.get_test_words_meanings():
            self.assertEqual(bst.search(word), meaning)

    def get_test_words_meanings(self) -> list[tuple[str, str]]:
        """Get test words and meanings."""
        words_meanings = [
            ("Apple", "a fruit"),
            ("apple", "a lowercase fruit"),
            ("banana", "a yellow fruit"),
            ("3453dsg", "not a fruit"),
        ]
        return words_meanings

    def test_insert_duplicates(self) -> None:
        """Test inserting duplicate entries into the BST."""
        bst = DictionaryBST()

        bst.insert("hi", "hello")
        self.assertEqual(bst.search("hi"), "hello")

        bst.insert("hi", "not hello")
        self.assertEqual(bst.search("hi"), "not hello")

    def test_dict_init(self) -> None:
        """Test initializign the BST with a dictionary."""
        init_dict = {k: v for (k, v) in self.get_test_words_meanings()}
        bst = DictionaryBST(init_dict)

        for word, meaning in self.get_test_words_meanings():
            self.assertEqual(bst.search(word), meaning)

    def test_print_alphabetical(self) -> None:
        """Test printing the words out in alphabetical order."""
        bst = DictionaryBST()

        self.assertEqual(bst.print_alphabetical(), [])

        for word, meaning in self.get_test_words_meanings():
            bst.insert(word, meaning)

        self.assertEqual(
            bst.print_alphabetical(), sorted(self.get_test_words_meanings(), key=lambda x: x[0])
        )


if __name__ == "__main__":
    unittest.main()
