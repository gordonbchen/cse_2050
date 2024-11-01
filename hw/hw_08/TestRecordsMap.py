import unittest

from RecordsMap import LocalRecord, RecordsMap


class TestLocalRecord(unittest.TestCase):
    """Tests for LocalRecord."""

    def test_init(self) -> None:
        """Test LocalRecord initialization."""
        lr1 = LocalRecord((10.3, -10.8))
        self.assertEqual(lr1.pos, (10.0, -11.0))
        self.assertEqual(lr1.max, float("-inf"))
        self.assertEqual(lr1.min, float("inf"))

        lr2 = LocalRecord((10.8, -10.2), max=5.0, min=-5.0, precision=1)
        self.assertEqual(lr2.pos, (10.8, -10.2))
        self.assertEqual(lr2.max, 5.0)
        self.assertEqual(lr2.min, -5.0)

    def test_hash(self) -> None:
        """Test LocalRecord hashing."""
        lr1 = LocalRecord((10.3, -10.8))
        lr2 = LocalRecord((10.4, -10.7), max=5.0, min=-5.0, precision=0)
        self.assertEqual(hash(lr1), hash(lr2))

        lr3 = LocalRecord((11.0, -11.0))
        lr4 = LocalRecord((10.0, -10.0))
        lr5 = LocalRecord((11.0, -10.0))
        for lr in [lr3, lr4, lr5]:
            self.assertNotEqual(hash(lr1), hash(lr))

    def test_eq(self) -> None:
        """Test equality between LocalRecords."""
        lr1 = LocalRecord((10.3, -10.8))
        lr2 = LocalRecord((10.4, -10.7), max=5.0, min=-5.0, precision=0)
        self.assertEqual(lr1, lr2)

        lr3 = LocalRecord((11.0, -11.0))
        lr4 = LocalRecord((10.0, -10.0))
        lr5 = LocalRecord((11.0, -10.0))
        for lr in [lr3, lr4, lr5]:
            self.assertNotEqual(lr1, lr)

    def test_add_report(self) -> None:
        """Test adding a report and updating min/max temps."""
        lr = LocalRecord((10.3, -10.8))
        self.assertEqual(lr.min, float("inf"))
        self.assertEqual(lr.max, float("-inf"))

        lr.add_report(100.0)
        self.assertEqual(lr.min, 100.0)
        self.assertEqual(lr.max, 100.0)

        lr.add_report(-100.0)
        self.assertEqual(lr.min, -100.0)
        self.assertEqual(lr.max, 100.0)

        lr.add_report(200.0)
        self.assertEqual(lr.min, -100.0)
        self.assertEqual(lr.max, 200.0)


class TestRecordsMap(unittest.TestCase):
    """Tests for RecordsMap."""

    def test_empty(self) -> None:
        """Test an empty RecordsMap."""
        rm = RecordsMap()
        self.assertEqual(len(rm), 0)

        self.assertFalse((10.0, 10.0) in rm)
        with self.assertRaises(KeyError):
            rm[(10.0, 10.0)]

    def test_add_one_report(self):
        """Test adding 1 report."""
        rm = RecordsMap()
        rm.add_report((10.3, -10.8), 70.0)

        self.assertEqual(len(rm), 1)
        self.assertTrue((10.0, -11.0) in rm)
        self.assertTrue((10.4, -10.7) in rm)
        self.assertTrue((10.3, -10.8) in rm)

        self.assertFalse((11.0, -10.0) in rm)
        self.assertFalse((10.6, -10.7) in rm)
        self.assertFalse((10.3, -10.2) in rm)

        self.assertEqual(rm[(10.0, -11.0)], (70.0, 70.0))

    def test_add_many_reports(self):
        """Test adding multiple reports. Update the same report and add different reports."""
        rm = RecordsMap()
        rm.add_report((10.3, -10.8), 70.0)
        self.assertEqual(len(rm), 1)
        self.assertEqual(rm[(10.0, -11.0)], (70.0, 70.0))

        # Add new max.
        rm.add_report((10.2, -10.7), 90.0)
        self.assertEqual(len(rm), 1)
        self.assertEqual(rm[(10.2, -10.7)], (70.0, 90.0))

        # Add new min.
        rm.add_report((10.0, -11.2), 50.0)
        self.assertEqual(len(rm), 1)
        self.assertEqual(rm[(10.0, -11.2)], (50.0, 90.0))

        # Add a different report.
        rm.add_report((99.3, -99.8), 70.0)
        self.assertEqual(len(rm), 2)
        self.assertEqual(rm[(10.0, -11.0)], (50.0, 90.0))
        self.assertEqual(rm[(99.0, -100.0)], (70.0, 70.0))

        # Test contains.
        self.assertTrue((10.0, -11.0) in rm)
        self.assertTrue((99.0, -100.0) in rm)
        self.assertFalse((50.0, 50.0) in rm)

    def test_rehashing(self):
        """Test rehashing frequency and functionality."""
        rm = RecordsMap()
        rm._rehash = call_counter(rm._rehash)
        self.assertEqual(rm._rehash.calls, 0)

        rm.add_report((10.3, -10.8), 70.0)
        self.assertEqual(rm._rehash.calls, 0)

        # Update the report many times. Should not rehash, len same.
        rm.add_report((10.0, -11.0), 90.0)
        rm.add_report((9.8, -11.4), 80.0)
        rm.add_report((10.0, -11.0), 10.0)
        rm.add_report((10.0, -11.0), 99.0)
        self.assertEqual(rm._rehash.calls, 0)

        # Add more reports (rehashes after 4, 8, 16, 32, 64, 128).
        for i in range(240):
            rm.add_report((i, i), i)
            self.assertEqual(len(rm), i + 2)
        self.assertEqual(rm._rehash.calls, 6)
        self.assertEqual(rm._n_buckets, 128 * 2)


def call_counter(func):
    """A function decorator that counts the number of times the func is called."""

    def helper(*args):
        helper.calls += 1
        return func(*args)

    helper.calls = 0
    return helper


if __name__ == "__main__":
    unittest.main()
