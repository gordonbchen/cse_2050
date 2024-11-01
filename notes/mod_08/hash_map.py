from typing import Any


class KeyValuePair:
    """An key-value pair in a hashmap bucket."""

    def __init__(self, key: Any, value: Any) -> None:
        """Initialize key-value pair."""
        self.key = key
        self.value = value


class BucketList:
    """A bucket represented as a list of key-value pairs."""

    def __init__(self) -> None:
        """Initialize bucket."""
        self._kv_pairs: list[KeyValuePair] = []

    def _get_kv_pair(self, key: Any) -> KeyValuePair | None:
        """Return the KeyValuePair with the key or None if it doesn't exist."""
        for kv_pair in self._kv_pairs:
            if kv_pair.key == key:
                return kv_pair
        return None

    def __getitem__(self, key: Any) -> Any:
        """Get the value associated with the given key. Raise a KeyError if key not found."""
        kv_pair = self._get_kv_pair(key)
        if kv_pair is None:
            raise KeyError(f"Key {key} not found.")
        return kv_pair.value

    def __setitem__(self, key: Any, value: Any) -> None:
        """Add or update a key-value pair."""
        kv_pair = self._get_kv_pair(key)
        if kv_pair is None:
            self._kv_pairs.append(KeyValuePair(key, value))
        else:
            kv_pair.value = value

    def remove(self, key: Any) -> None:
        """Remove the key-value pair. Raise a KeyError if key not found."""
        kv_pair = self._get_kv_pair(key)
        if kv_pair is None:
            raise KeyError(f"Key {key} not found, could not be removed.")
        self._kv_pairs.remove(kv_pair)

    def __len__(self) -> int:
        """Get the length of the bucket list."""
        return len(self._kv_pairs)

    def __contains__(self, key: Any) -> bool:
        """Return True if the key is in the bucket list."""
        kv_pair = self._get_kv_pair(key)
        return kv_pair is not None

    def __iter__(self) -> tuple[Any]:
        """Return an iterator of the keys."""
        return (kv.key for kv in self._kv_pairs)

    def items(self) -> tuple[tuple[Any, Any]]:
        """Return a tuple of all kv pairs."""
        return ((kv.key, kv.value) for kv in self._kv_pairs)


class HashMap:
    """A hash map."""

    def __init__(self, n_buckets: int = 2) -> None:
        """Initialize hashmap."""
        self._n_buckets = n_buckets
        self._buckets = [BucketList() for i in range(self._n_buckets)]
        self._len = 0

    def __len__(self) -> int:
        """Return the number of items in the hashmap."""
        return self._len

    def _get_bucket_idx(self, key: Any) -> int:
        """Get the bucket idx for the key."""
        return hash(key) % self._n_buckets

    def _get_bucket(self, key: Any) -> BucketList:
        """Get the bucket for the key."""
        return self._buckets[self._get_bucket_idx(key)]

    def __setitem__(self, key: Any, value: Any) -> None:
        """Add or update the key-value pair."""
        bucket = self._get_bucket(key)
        if key not in bucket:
            self._len += 1
        bucket[key] = value

        if self._len > self._n_buckets:
            self._rehash(self._n_buckets * 2)

    def __getitem__(self, key: Any) -> Any:
        """Get the value associated with the key if it exists. Otherwise raise a KeyError."""
        bucket = self._get_bucket(key)
        if key in bucket:
            return bucket[key]
        raise KeyError(f"Key {key} not found.")

    def remove(self, key: Any) -> None:
        """Remove the kev-value pair from the hashmap. Raise a KeyError if the key doesn't exist."""
        bucket = self._get_bucket(key)
        if key not in bucket:
            raise KeyError(f"Key {key} not found. Could not remove key.")
        bucket.remove(key)
        self._len -= 1

    def _rehash(self, new_n_buckets: int) -> None:
        """Rehash all items in the hashmap."""
        self._n_buckets = new_n_buckets
        new_buckets = [BucketList() for i in range(self._n_buckets)]

        for bucket in self._buckets:
            for k, v in bucket.items():
                bucket_idx = self._get_bucket_idx(k)
                new_buckets[bucket_idx][k] = v

        self._buckets = new_buckets

    def __contains__(self, key: Any) -> bool:
        """Return True if the key is in the hashmap."""
        bucket = self._get_bucket(key)
        return key in bucket


if __name__ == "__main__":
    # BucketList.
    bucket_list = BucketList()
    bucket_list[3] = "v"
    bucket_list[1] = "a"
    bucket_list[2] = "b"
    bucket_list[3] = "c"

    assert bucket_list[3] == "c"
    assert 3 in bucket_list
    assert 4 not in bucket_list
    assert len(bucket_list) == 3

    for k in bucket_list:
        print(k)
    for k, v in bucket_list.items():
        print(k, v)

    bucket_list.remove(3)
    assert 3 not in bucket_list

    try:
        bucket_list.remove(4)
    except KeyError as e:
        print(e)

    print("\n\n")

    # HashMap.
    hash_map = HashMap()
    hash_map["c"] = 42
    hash_map["a"] = 1
    hash_map["b"] = 2
    hash_map["c"] = 3

    assert hash_map["c"] == 3
    assert "c" in hash_map
    assert len(hash_map) == 3

    hash_map.remove("c")
    assert "c" not in hash_map

    try:
        hash_map.remove("d")
    except KeyError as e:
        print(e)

    hash_map["d"] = 1
    hash_map["e"] = 2
    hash_map["f"] = 3
    print(hash_map._n_buckets)
