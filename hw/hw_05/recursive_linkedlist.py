from recursive_node import Node


###############################################################################
# This code is provided for you - you should not change anything in this file #
# and you do not need to submit this. The test cases will use exactly this    #
# code for the RecursiveLinkedList.                                           #
###############################################################################
class RecursiveLinkedList:
    def __init__(self, items=None):
        """Instantiates a new RecursiveLinkedList with optional collection items"""
        self._head = None

        if items is not None:
            for item in items:
                self.add_last(item)

    def __len__(self):
        """Returns number of items in list"""
        if self._head is None:
            return 0
        return len(self._head)

    def get_head(self):
        """Returns the data stored in the head node"""
        return self._head.data if self else None

    def get_tail(self):
        """Returns the data stored in the tail node"""
        return self._head.get_tail() if self else None

    def add_first(self, data):
        """Adds item to beginning of linked list"""
        self._head = Node(data, link=self._head)

    def add_last(self, data):
        """Recursively adds item to end of linked list"""
        if len(self) == 0:
            self._head = Node(data)
        else:
            self._head.add_last(data)

    def remove_first(self):
        """Removes first item from linked list"""
        if len(self) == 0:
            raise IndexError("Cannot remove from empty list")

        data = self._head.data
        self._head = self._head.link

        return data

    def remove_last(self):
        """Removes last item from linked list"""
        if len(self) == 0:
            raise IndexError("Cannot remove from empty list")

        self._head, data = self._head.remove_last()

        return data

    def reverse(self):
        """Reverses list"""
        self._head = self._head.reverse(None) if self._head else self._head

    def total(self):
        """Adds up all items in list"""
        return self._head.total() if self._head else 0
