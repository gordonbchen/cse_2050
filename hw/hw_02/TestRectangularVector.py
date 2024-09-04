import unittest

from vector import PolarVector as PV, RectangularVector as RV, Vector as V


class TestRectangularVector(unittest.TestCase):
    def setUp(self):
        self.v1 = RV(3, 4)
        self.v1_eq = RV(3, 4)
        self.v2 = RV(5, 12)
        self.v2_eq = RV(5, 12)

    def test_inheritance_structure(self):
        """Checks that a RectangularVector inherits from Vector"""
        self.assertIsInstance(self.v1, RV)
        self.assertIsInstance(self.v1, V)

    def test_properties(self):
        """
        v1.x; v1.get_y(); v1.get_mag(); v1.get_ang()
        should all be correct within 3 decimal places.
        """
        self.assertEqual(self.v1.get_x(), 3)
        self.assertEqual(self.v1.get_y(), 4)
        self.assertEqual(self.v1.get_mag(), 5)
        self.assertAlmostEqual(self.v1.get_ang(), 0.927, 3)

        self.assertEqual(self.v2.get_x(), 5)
        self.assertEqual(self.v2.get_y(), 12)
        self.assertEqual(self.v2.get_mag(), 13)
        self.assertAlmostEqual(self.v2.get_ang(), 1.176, 3)

    def test_setters_valid(self):
        """v.x = a; v.y = a"""
        self.assertEqual(self.v1.get_x(), 3)
        self.assertEqual(self.v1.get_y(), 4)
        self.assertEqual(self.v1.get_mag(), 5)
        self.assertAlmostEqual(self.v1.get_ang(), 0.927, 3)

        self.v1.set_x(4)
        self.assertEqual(self.v1.get_x(), 4)
        self.assertEqual(self.v1.get_y(), 4)
        self.assertAlmostEqual(self.v1.get_mag(), 5.657, 3)
        self.assertAlmostEqual(self.v1.get_ang(), 0.785, 3)

        self.v1.set_y(7)
        self.assertEqual(self.v1.get_x(), 4)
        self.assertEqual(self.v1.get_y(), 7)
        self.assertAlmostEqual(self.v1.get_mag(), 8.062, 3)
        self.assertAlmostEqual(self.v1.get_ang(), 1.052, 3)

    def test_setters_invalid(self):
        """v.mag and v.ang"""
        with self.assertRaises(AttributeError):
            self.v1.set_mag(3)

        with self.assertRaises(AttributeError):
            self.v1.set_ang(4)

    def test_eq(self):
        """v1 == v2"""
        self.assertEqual(self.v1, self.v1_eq)
        self.assertNotEqual(self.v1, self.v2)

    def test_conversions(self):
        """rectangular(v) and polar(v)"""
        self.assertEqual(self.v1.rectangular(), RV(3, 4))
        self.assertEqual(self.v1.polar(), PV(5, 0.927295))

    def test_repr(self):
        """tests string representation"""
        self.assertEqual(
            repr(self.v1), f"RectangularVector({self.v1.get_x()}, {self.v1.get_y()})"
        )


if __name__ == "__main__":
    unittest.main()
