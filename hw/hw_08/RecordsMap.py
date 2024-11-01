from __future__ import annotations


class LocalRecord:
    """Stores record temperatures for a single grid point."""

    def __init__(
        self,
        pos: tuple[float, float],
        max: float = float("-inf"),
        min: float = float("inf"),
        precision: int = 0,
    ) -> None:
        """Initialize LocalRecord."""
        self.pos = (round(pos[0], precision), round(pos[1], precision))
        self.max = max
        self.min = min

    def add_report(self, temp: float) -> None:
        """Update the min and max temp if the temp is a record."""
        if temp > self.max:
            self.max = temp
        if temp < self.min:
            self.min = temp

    def __eq__(self, other: LocalRecord) -> bool:
        """Return True if the records are for the same position."""
        return self.pos == other.pos

    def __hash__(self) -> int:
        """Return the hash of the position coordinate."""
        return hash(self.pos)

    def __repr__(self) -> str:
        """Return a str representation of the LocalRecord."""
        return f"Record(pos={self.pos}, max={self.max}, min={self.min})"


class RecordsMap:
    """A hash map of temperature records."""

    def __init__(self) -> None:
        """Initialize the temperature record hash map."""
        self._len = 0
        self._n_buckets = 4
        self._buckets: list[list[LocalRecord]] = self._create_empty_buckets()

    def _create_empty_buckets(self) -> list[list[LocalRecord]]:
        """Create empty buckets storing LocalRecords."""
        return [list() for i in range(self._n_buckets)]

    def __len__(self) -> int:
        """Return the number of records in the hash map."""
        return self._len

    def add_report(self, pos: tuple[float, float], temp: float) -> None:
        """Add a report to the LocalRecord corresponding to the position."""
        target_lr = LocalRecord(pos)
        bucket = self._get_bucket(target_lr)

        for lr in bucket:
            if lr == target_lr:
                lr.add_report(temp)
                return

        self._len += 1
        target_lr.add_report(temp)
        bucket.append(target_lr)

        if self._len > self._n_buckets:
            self._rehash(self._n_buckets * 2)

    def _get_bucket(self, lr: LocalRecord) -> list[LocalRecord]:
        """Return the bucket with the LocalRecord."""
        bucket_idx = hash(lr) % self._n_buckets
        return self._buckets[bucket_idx]

    def __getitem__(self, pos: tuple[float, float]) -> tuple[float, float]:
        """
        Return the (min, max) temperatures for the position.
        Raise a KeyError if pos is not in the hashmap.
        """
        target_lr = LocalRecord(pos)
        for lr in self._get_bucket(target_lr):
            if lr == target_lr:
                return (lr.min, lr.max)
        raise KeyError(f"LocalRecord at pos {pos} not found.")

    def __contains__(self, pos: tuple[float, float]) -> bool:
        """Return True if the hash map contains a LocalRecord for the position."""
        target_lr = LocalRecord(pos)
        for lr in self._get_bucket(target_lr):
            if lr == target_lr:
                return True
        return False

    def _rehash(self, new_n_buckets: int) -> None:
        """Rehash every entry in the hashtable with new_n_buckets."""
        old_buckets = self._buckets
        self._n_buckets = new_n_buckets
        self._buckets = self._create_empty_buckets()

        for bucket in old_buckets:
            for lr in bucket:
                self._get_bucket(lr).append(lr)
