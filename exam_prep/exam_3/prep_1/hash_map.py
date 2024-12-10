"""
Mapping ADT implementation
    * KVPair: stores key and value
    * Bucket: stores list of KVPairs
    * HashMap: stores array of Buckets
"""

from __future__ import annotations
from typing import Any
import unittest


class KVPair:
    def __init__(self, key: Any, value: Any) -> None:
        self.key = key
        self.value = value


class Bucket:
    def __init__(self) -> None:
        self.pairs: list[KVPair] = []

    def get_kv_pair(self, key: Any) -> KVPair | None:
        for pair in self.pairs:
            if pair.key == key:
                return pair
        return None

    def put(self, key: Any, value: Any) -> None:
        pair = self.get_kv_pair(key)
        if pair is None:
            self.pairs.append(KVPair(key, value))
        else:
            pair.value = value

    def get(self, key: Any) -> Any:
        pair = self.get_kv_pair(key)
        if pair is None:
            raise KeyError(f"Key {key} not in Bucket.")
        else:
            return pair.value

    def __contains__(self, key: Any) -> bool:
        return self.get_kv_pair(key) is not None

    def __len__(self) -> int:
        return len(self.pairs)


class HashMap:
    def __init__(self) -> None:
        self.n_buckets = 32
        self.buckets = [Bucket() for i in range(self.n_buckets)]

        self.n_items = 0
        self.MAX_LOAD_FACTOR = 0.8

    def get_bucket(self, key) -> Bucket:
        return self.buckets[hash(key) % self.n_buckets]

    def put(self, key: Any, value: Any) -> None:
        bucket = self.get_bucket(key)
        if key not in bucket:
            self.n_items += 1
        bucket.put(key, value)

        load_factor = self.n_items / self.n_buckets
        if load_factor > self.MAX_LOAD_FACTOR:
            self.rehash(self.n_buckets * 2)

    def rehash(self, new_n_buckets: int) -> None:
        old_buckets = self.buckets

        self.n_buckets = new_n_buckets
        self.buckets = [Bucket() for i in range(self.n_buckets)]

        for bucket in old_buckets:
            for pair in bucket.pairs:
                bucket = self.get_bucket(pair.key)
                bucket.put(pair.key, pair.value)

    def get(self, key: Any) -> Any:
        bucket = self.get_bucket(key)
        return bucket.get(key)

    def __len__(self) -> int:
        return self.n_items


class HashMapTest(unittest.TestCase):
    def test_add_duplicates(self):
        hashmap = HashMap()

        hashmap.put("a", 1)
        self.assertEqual(hashmap.get("a"), 1)
        self.assertEqual(len(hashmap), 1)

        hashmap.put("a", 2)
        self.assertEqual(hashmap.get("a"), 2)
        self.assertEqual(len(hashmap), 1)

    def test_rehashing(self):
        hashmap = HashMap()

        for i in range(100):
            hashmap.put(i, str(i))
        self.assertEqual(len(hashmap), 100)

        for i in range(100):
            self.assertEqual(hashmap.get(i), str(i))

        self.assertEqual(hashmap.n_buckets, 128)

    def test_raises_key_error(self):
        hashmap = HashMap()

        for i in range(10):
            hashmap.put(i, str(i))

        self.assertEqual(hashmap.get(7), "7")

        with self.assertRaises(KeyError):
            hashmap.get(99)


if __name__ == "__main__":
    unittest.main()
