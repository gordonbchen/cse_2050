from typing import Any


class KVPair:
    def __init__(self, key: Any, value: Any) -> None:
        self.key = key
        self.value = value


class HashMap:
    def __init__(self) -> None:
        self.n_buckets = 8
        self.buckets: list[list[KVPair]] = [[] for i in range(self.n_buckets)]

        self.n_items = 0
        self.MAX_LOAD_FACTOR = 0.8
        self.MIN_LOAD_FACTOR = 0.2
        self.MIN_BUCKETS = 8

    def get_bucket(self, key: Any) -> list[KVPair]:
        bucket_idx = hash(key) % self.n_buckets
        return self.buckets[bucket_idx]

    def put(self, key: Any, value: Any) -> None:
        bucket = self.get_bucket(key)

        for kv_pair in bucket:
            if kv_pair.key == key:
                kv_pair.value = value
                return

        self.n_items += 1
        bucket.append(KVPair(key, value))

        load_factor = self.n_items / self.n_buckets
        if load_factor > self.MAX_LOAD_FACTOR:
            self.rehash(self.n_buckets * 2)

    def rehash(self, n_buckets: int) -> None:
        self.n_buckets = n_buckets
        old_buckets = self.buckets
        self.buckets = [[] for i in range(self.n_buckets)]

        for bucket in old_buckets:
            for kv_pair in bucket:
                bucket = self.get_bucket(kv_pair.key)
                bucket.append(kv_pair)

    def get(self, key: Any) -> Any:
        bucket = self.get_bucket(key)
        for kv_pair in bucket:
            if kv_pair.key == key:
                return kv_pair.value

        raise KeyError(f"Failed to find key {key}.")

    def remove(self, key: Any) -> None:
        bucket = self.get_bucket(key)
        for kv_pair in bucket:
            if kv_pair.key == key:
                bucket.remove(kv_pair)

                self.n_items -= 1
                load_factor = self.n_items / self.n_buckets
                if (load_factor < self.MIN_LOAD_FACTOR) and (
                    (self.n_buckets // 2) >= self.MIN_BUCKETS
                ):
                    self.rehash(self.n_buckets // 2)

                return kv_pair.value

        else:
            raise KeyError(f"Failed to find key {key}.")
