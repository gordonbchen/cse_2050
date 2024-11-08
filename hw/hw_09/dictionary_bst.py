from typing import Iterator


class Node:
    """A node in a binary search tree."""

    def __init__(self, word: str, meaning: str) -> None:
        """Initialize the node."""
        self.word = word
        self.meaning = meaning

        # Children.
        self.left = None
        self.right = None

    def insert(self, word: str, meaning: str) -> None:
        """Insert the word into the BST."""
        if self.word == word:
            self.meaning = meaning
        elif word < self.word:
            if self.left is not None:
                self.left.insert(word, meaning)
            else:
                self.left = Node(word, meaning)
        else:
            if self.right is not None:
                self.right.insert(word, meaning)
            else:
                self.right = Node(word, meaning)

    def search(self, word: str) -> str | None:
        """
        Find and return the meaning of the word.
        Return None if the word is not in the BST.
        """
        if self.word == word:
            return self.meaning
        elif (self.left is not None) and (word < self.word):
            return self.left.search(word)
        elif (self.right is not None) and (word > self.word):
            return self.right.search(word)
        else:
            return None

    def in_order_traverse(self) -> Iterator[tuple[str, str]]:
        """Traverse the BST in order (left, root, right)."""
        if self.left is not None:
            yield from self.left.in_order_traverse()

        yield (self.word, self.meaning)

        if self.right is not None:
            yield from self.right.in_order_traverse()


class DictionaryBST:
    """
    A class to represent a dictionary using self-balancing trees.

    Methods:
        insert(word, meaning): Insert a word and its meaning into the dictionary.
        search(word): Search for a word in the dictionary and return its meaning.
        print_alphabetical(): Return all dictionary entries in alphabetical order.
    """

    def __init__(self, entries: dict[str, str] | None = None) -> None:
        """
        Parameters:
        entries (dict[str, str] | None, optional): A dictionary with string words and meanings.
                                                  Defaults to None if not provided.
        """
        self.root = None

        if entries is not None:
            for word, meaning in entries.items():
                self.insert(word, meaning)

    def insert(self, word: str, meaning: str) -> None:
        """
        Insert a word and its meaning into the tree.
        If inserting a duplicate word, update the meaning.

        Args:
            word (str): The word to insert.
            meaning (str): The meaning of the word.
        """
        if self.root is None:
            self.root = Node(word, meaning)
        else:
            self.root.insert(word, meaning)

    def search(self, word: str) -> None:
        """
        Search for a word in the tree and return its meaning.

        Args:
            word (str): The word to search for.

        Returns:
            str: The meaning of the word if found, else return None'
        """
        if self.root is None:
            return None
        return self.root.search(word)

    def print_alphabetical(self) -> list[tuple]:
        """
        Retrieve all dictionary entries in alphabetical order.

        Returns:
            list of tuple: List of tuples, each containing (word, meaning).
        """
        if self.root is None:
            return []

        return list(self.root.in_order_traverse())

    # Feel free to implement other helper and private methods


if __name__ == "__main__":
    dictionary = DictionaryBST()
    dictionary.insert("banana", "A yellow tropical fruit.")
    dictionary.insert("apple", "A fruit that grows on trees.")
    dictionary.insert("cherry", "A small, round, red fruit.")

    # Search for a word
    print(dictionary.search("banana"))  # Output: A yellow tropical fruit.

    # Print all entries in alphabetical order
    print(dictionary.print_alphabetical())
    # Output:
    # [
    #     ("apple", "A fruit that grows on trees."),
    #     ("banana", "A yellow tropical fruit."),
    #     ("cherry", "A small, round, red fruit.")
    # ]
