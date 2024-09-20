from __future__ import annotations


class Process:
    """A process running on the cpu."""

    def __init__(self, pid: str, cycles: int = 100) -> None:
        """Create process."""
        self.pid = pid
        self.cycles = cycles

        self.link = None
        self.prev = None

    def __eq__(self, other: Process) -> bool:
        """Return True if the process have the same pid."""
        return self.pid == other.pid

    def __repr__(self) -> str:
        """Return a str representation of the process."""
        return f"Process({self.pid}, {self.cycles})"
