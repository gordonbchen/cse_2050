from typing import Any


class Entry:
    """An entry in a hashmap bucket."""

    def __init__(self, key: Any, value: Any) -> None:
        """Key-value pair."""
        self.key = key
        self.value = value


class ListMapping:
    """Stores the key-value pairs in list."""

    def __init__(self) -> None:
        """Initialize bucket."""
        self._entries: list[Entry] = []

    def __getitem__(self, key: Any) -> Any:
        """
        Access the value associated with a given key, raise KeyError if key not found.
        Implements the evaluation of self[key].
        """
        for entry in self._entries:
            if entry.key == key:
                return entry.value
        raise KeyError(f"Key {key} not found.")

    def __setitem__(self, key: Any, value: Any) -> None:
        """
        Add a new or update a key-value pair.
        Implements the assignment self[key] = value.
        """
        for entry in self._entries:
            if entry.key == key:
                entry.value = value
                break
        else:
            self._entries.append(Entry(key, value))

    def __len__(self) -> int:
        """Implements the built-in function len()."""
        return len(self._entries)

    def __contains__(self, key: Any) -> bool:
        """Implements the membership test operator: keyword in (and not in)."""
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True


if __name__ == "__main__":
    myMapping = ListMapping()
    myMapping[3] = "v"
    myMapping[1] = "a"
    myMapping[2] = "b"
    myMapping[3] = "c"
    print(myMapping[3])
