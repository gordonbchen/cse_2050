class Node:
    """
    A class to represent a node in the tree.
    """
    def __init__(self, word, meaning):
        pass


class DictionaryBST:
    """
    A class to represent a dictionary using self-balancing trees.
    
    Methods:
        insert(word, meaning): Insert a word and its meaning into the dictionary.
        search(word): Search for a word in the dictionary and return its meaning.
        print_alphabetical(): Return all dictionary entries in alphabetical order.
    """
    def __init__(self, entries: dict[str, str] | None = None):
        """
        Parameters:
        entries (dict[str, str] | None, optional): A dictionary with string words and meanings.
                                                  Defaults to None if not provided.
        """
        pass

    def insert(self, word, meaning):
        """
        Insert a word and its meaning into the tree. If inserting a duplicate word updates the meaning.
        
        Args:
            word (str): The word to insert.
            meaning (str): The meaning of the word.
        """
        pass

    def search(self, word):
        """
        Search for a word in the tree and return its meaning.
        
        Args:
            word (str): The word to search for.
        
        Returns:
            str: The meaning of the word if found, else return None'
        """
        pass 

    def print_alphabetical(self):
        """
        Retrieve all dictionary entries in alphabetical order.
        
        Returns:
            list of tuple: List of tuples, each containing (word, meaning).
        """
        pass

    # Feel free to implement other helper and private methods
