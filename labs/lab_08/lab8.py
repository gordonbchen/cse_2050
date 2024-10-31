from typing import Any


class CustomSet:
    """A custom set using a hashtable."""

    def __init__(self) -> None:
        """Initialize an empty CustomSet."""
        self._min_buckets = 8  # Never rehash down below this many buckets.
        self._n_buckets = 8  # Initial size. Good to use a power of 2 here.
        self._len = 0  # Number of items in custom set.
        self._L = [[] for i in range(self._n_buckets)]  # List of empty buckets.

    def __len__(self) -> int:
        """Returns the number of items in CustomSet."""
        return self._len

    def _find_bucket(self, item: Any) -> int:
        """Returns the index of the bucket `item` should go in."""
        return hash(item) % self._n_buckets

    def __contains__(self, item: Any) -> bool:
        """Returns True if item is in the CustomSet."""
        bucket_idx = self._find_bucket(item)
        return item in self._L[bucket_idx]

    def add(self, item: Any) -> None:
        """
        Add an item to CustomSet.
        Duplicate adds are ignored, they don't increase the length or raise an error.
        """
        if item in self:
            return

        # Add the item to the hashtable and increment len.
        bucket_idx = self._find_bucket(item)
        self._L[bucket_idx].append(item)

        self._len += 1

        # Rehash if # items >= 2 * # buckets.
        if len(self) >= (2 * self._n_buckets):
            self._rehash(2 * self._n_buckets)

    def remove(self, item: Any) -> None:
        """
        Remove an item from CustomSet.
        Raise a KeyError if the item is not in the CustomSet.
        """
        if item not in self:
            raise KeyError(f"{item} not in CustomSet.")

        # remove item from hashtable and decrement len.
        bucket_idx = self._find_bucket(item)
        self._L[bucket_idx].remove(item)

        self._len -= 1

        # Rehash if (# items <= 1/2 * # buckets), and (1/2 * # buckets >= min_buckets).
        if (len(self) <= (self._n_buckets // 2)) and ((self._n_buckets // 2) >= self._min_buckets):
            self._rehash(self._n_buckets // 2)

    def _rehash(self, new_buckets: int) -> None:
        """
        Rehash every item to a hash table with new_buckets.
        new_buckets be either 2*n_buckets (rehash up) or n_buckets/2 (hash down).
        """
        # Set the new number of buckets and create an empty list of buckets.
        self._n_buckets = new_buckets
        new_L = [list() for i in range(self._n_buckets)]

        # For each item in each existing bucket, find the new bucket and append.
        for bucket in self._L:
            for item in bucket:
                bucket_idx = self._find_bucket(item)
                new_L[bucket_idx].append(item)

        # Replace old buckets with new buckets.
        self._L = new_L
