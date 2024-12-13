from typing import Any


class Entry:
    def __init__(self, key: Any, value: Any) -> None:
        self.key = key
        self.value = value


class HashMap:
    def __init__(self) -> None:
        self._n_buckets = 8
        self._buckets = [[] for i in range(self._n_buckets)]
        self._len = 0

        self._MIN_BUCKETS = 8
        self._MAX_LOAD_FACTOR = 0.8
        self._MIN_LOAD_FACTOR = 0.2

    def __getitem__(self, key: Any) -> Any:
        bucket = self._get_bucket(key)
        for entry in bucket:
            if entry.key == key:
                return entry.value

        raise KeyError(f"Failed to find key {key}.")

    def __setitem__(self, key: Any, value: Any) -> None:
        bucket = self._get_bucket(key)
        for entry in bucket:
            if entry.key == key:
                entry.value = value
                return

        bucket.append(Entry(key, value))
        self._len += 1

        load_factor = len(self) / self._n_buckets
        if load_factor > self._MAX_LOAD_FACTOR:
            self._rehash(self._n_buckets * 2)

    def remove(self, key: Any) -> Any:
        bucket = self._get_bucket(key)
        for entry in bucket:
            if entry.key == key:
                bucket.remove(entry)
                self._len -= 1

                load_factor = len(self) / self._n_buckets
                if (load_factor < self._MIN_LOAD_FACTOR) and (
                    (self.n_buckets // 2) >= self._MIN_BUCKETS
                ):
                    self._rehash(self._n_buckets // 2)

                return entry.value

        raise KeyError(f"Failed to find and remove key {key}.")

    def __len__(self) -> int:
        return self._len

    def _get_bucket(self, key: Any) -> int:
        bucket_idx = hash(key) % self._n_buckets
        return self._buckets[bucket_idx]

    def _rehash(self, n_buckets: int) -> None:
        old_buckets = self._buckets

        self._n_buckets = n_buckets
        self._buckets = [[] for i in range(self._n_buckets)]

        for bucket in old_buckets:
            for entry in bucket:
                new_bucket = self._get_bucket(entry.key)
                new_bucket.append(entry)
