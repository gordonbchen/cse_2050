import unittest

from circularqueue import CircularQueue
from process import Process


class TestCircularQueue(unittest.TestCase):
    """Tests for the CircularQueue class."""

    def test_init_empty(self) -> None:
        """Test creating an empty CircularQueue."""
        cq = CircularQueue()
        self.assertEqual(len(cq), 0)
        self.assertEqual(cq._head, None)

    def circular_queue_matches_process_list(
        self, cq: CircularQueue, ps: list[Process]
    ) -> None:
        """Test that the CircularQueue matches the list of Processes."""
        self.assertEqual(len(cq), len(ps))
        curr_process = cq._head
        for i, process in enumerate(ps):
            self.assertEqual(curr_process, process)
            self.assertEqual(process.prev, ps[i - 1])
            self.assertEqual(process.link, ps[(i + 1) % len(ps)])
            curr_process = curr_process.link

    def test_init_with_processes(self) -> None:
        """Test creating a CircularQueue with a list of processes."""
        ps = [Process("1"), Process("2"), Process("3")]
        cq = CircularQueue(ps)
        self.circular_queue_matches_process_list(cq, ps)

    def test_add_process_one(self) -> None:
        """Test adding 1 process."""
        cq = CircularQueue()
        p = Process("a")
        cq.add_process(p)

        self.circular_queue_matches_process_list(cq, [p])

    def test_add_process_two(self) -> None:
        """Test adding 2 process."""
        cq = CircularQueue()
        p1 = Process("a")
        p2 = Process("b")
        cq.add_process(p1)
        cq.add_process(p2)

        self.circular_queue_matches_process_list(cq, [p1, p2])

    def test_add_process_three(self) -> None:
        """Test adding 3 process."""
        cq = CircularQueue()
        p1 = Process("a")
        p2 = Process("b")
        p3 = Process("c")
        cq.add_process(p1)
        cq.add_process(p2)
        cq.add_process(p3)

        self.circular_queue_matches_process_list(cq, [p1, p2, p3])

    def test_repr(self) -> None:
        """Test str representation of CircularQueue."""
        p1 = Process("send_email", 250)
        p2 = Process("open_word", 100)
        p3 = Process("run_simulation", 1000)
        cq = CircularQueue([p1, p2, p3])

        repr_str = (
            "CircularQueue(Process(send_email, 250), "
            "Process(open_word, 100), Process(run_simulation, 1000))"
        )
        self.assertEqual(repr(cq), repr_str)

    def check_remove_process(
        self, cq: CircularQueue, ps: list[Process], ind: int
    ) -> None:
        """Test that removing the process at the given index works correctly."""
        self.assertEqual(cq.remove_process(ps[ind]), ps.pop(ind))
        self.circular_queue_matches_process_list(cq, ps)

    def test_remove_process_3_middle(self) -> None:
        """Test removing a process from the middle of the queue."""
        ps = [Process("1"), Process("2"), Process("3")]
        cq = CircularQueue(ps)
        self.check_remove_process(cq, ps, 1)

    def test_remove_process_3_head(self) -> None:
        """Test removing a process from the head of the queue."""
        ps = [Process("1"), Process("2"), Process("3")]
        cq = CircularQueue(ps)
        self.check_remove_process(cq, ps, 0)

    def test_remove_process_3_final(self) -> None:
        """Test removing a process from the end of the queue."""
        ps = [Process("1"), Process("2"), Process("3")]
        cq = CircularQueue(ps)
        self.check_remove_process(cq, ps, -1)

    def test_remove_process_1(self) -> None:
        """Test removing the only process in a queue."""
        ps = [Process("1")]
        cq = CircularQueue(ps)
        self.check_remove_process(cq, ps, 0)

        self.assertEqual(cq._head, None)

    def test_kill_3_middle(self) -> None:
        """Test killing a process in the middle of a queue."""
        ps = [Process("1"), Process("2"), Process("3")]
        cq = CircularQueue(ps)

        self.assertEqual(cq.kill("2"), ps.pop(1))
        self.circular_queue_matches_process_list(cq, ps)


if __name__ == "__main__":
    unittest.main()
