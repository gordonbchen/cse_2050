from typing import Optional

from process import Process


class CircularQueue:
    """A circular queue to allow us to run processes turn-by-turn"""

    def __init__(self, processes: Optional[list[Process]] = None) -> None:
        """Create circular queue."""
        self._len = 0
        self._head: Process | None = None
        self._d_processes: dict[str, Process] = {}

        if processes is not None:
            for process in processes:
                self.add_process(process)

    def add_process(self, process: Process):
        """Add a process to the queue."""
        if len(self) == 0:
            self._head = process
            process.link = process
            process.prev = process
        else:
            process.link = self._head
            process.prev = self._head.prev
            self._head.prev = process
            process.prev.link = process

        self._d_processes[process.pid] = process
        self._len += 1

    def remove_process(self, process: Process) -> Process:
        """Remove a process from the queue by Process object."""
        return self.kill(process.pid)

    def kill(self, pid: str) -> Process:
        """Remove a process from the queue based on its pid."""
        process = self._d_processes.pop(pid)

        if len(self) == 1:
            self._head = None
        else:
            process.prev.link = process.link
            process.link.prev = process.prev

            if self._head.pid == pid:
                self._head = self._head.link

        self._len -= 1
        return process

    def __len__(self) -> int:
        """Return the number of processes in the queue."""
        return self._len

    def __repr__(self) -> str:
        """Return the str representation of the circular queue."""
        process_reprs = []
        curr_process = self._head
        for i in range(len(self)):
            process_reprs.append(repr(curr_process))
            curr_process = curr_process.link

        return f"CircularQueue({', '.join(process_reprs)})"

    def run(self, n_cycles: int) -> str:
        """Runs circular queue for n_cycles, giving each process 1 cycle at a time"""
        n_remaining = n_cycles

        # Using an intermediate list since appending to a string is O(n)
        return_strings = []

        while n_remaining:
            self._head.cycles -= 1

            if self._head.cycles == 0:
                return_strings.append(
                    f"{self._head.pid} finished after {n_cycles-n_remaining+1}"
                    " computational cycles."
                )
                self.remove_process(self._head)

            else:
                self._head = self._head.link

            n_remaining -= 1

        return "\n".join(return_strings)


if __name__ == "__main__":
    p1 = Process("send_email", 250)
    p2 = Process("open_word", 100)
    p3 = Process("run_simulation", 1000)
    cq = CircularQueue([p1, p2, p3])
    run_return = cq.run(1000)
    print(run_return)
