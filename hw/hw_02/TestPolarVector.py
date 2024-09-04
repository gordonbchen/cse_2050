import unittest

from vector import PolarVector as PV, RectangularVector as RV, Vector as V


class TestPolarVector(unittest.TestCase):
    def setUp(self):
        """SetUp is run before every test."""
        self.pv1 = PV(5, 0.927295)
        self.pv1_eq = PV(5, 0.927295)
        self.pv2 = PV(13, 1.176)
        self.pv2_eq = PV(13, 1.176)

    def test_inheritance_structure(self):
        """Checks that a PolarVector inherits from Vector"""
        self.assertIsInstance(self.pv1, PV)
        self.assertIsInstance(self.pv1, V)

    def test_properties(self):
        """
        v1.x; v1.get_y(); v1.get_mag(); v1.get_ang()
        should all be correct within 3 decimal places.
        """
        self.assertAlmostEqual(self.pv1.get_x(), 3, 3)
        self.assertAlmostEqual(self.pv1.get_y(), 4, 3)
        self.assertAlmostEqual(self.pv1.get_mag(), 5, 3)
        self.assertAlmostEqual(self.pv1.get_ang(), 0.927, 3)

        self.assertAlmostEqual(self.pv2.get_x(), 5, 3)
        self.assertAlmostEqual(self.pv2.get_y(), 12, 3)
        self.assertAlmostEqual(self.pv2.get_mag(), 13, 3)
        self.assertAlmostEqual(self.pv2.get_ang(), 1.176, 3)

    def test_setters_valid(self):
        """v1.get_mag()=a; v1.get_ang()=a"""
        self.assertAlmostEqual(self.pv1.get_x(), 3, 3)
        self.assertAlmostEqual(self.pv1.get_y(), 4, 3)
        self.assertAlmostEqual(self.pv1.get_mag(), 5, 3)
        self.assertAlmostEqual(self.pv1.get_ang(), 0.927, 3)

        self.pv1.set_mag(10)
        self.assertAlmostEqual(self.pv1.get_x(), 6, 3)
        self.assertAlmostEqual(self.pv1.get_y(), 8, 3)
        self.assertAlmostEqual(self.pv1.get_mag(), 10, 3)
        self.assertAlmostEqual(self.pv1.get_ang(), 0.927, 3)

        self.pv1.set_ang(0.5)
        self.assertAlmostEqual(self.pv1.get_x(), 8.776, 3)
        self.assertAlmostEqual(self.pv1.get_y(), 4.794, 3)
        self.assertAlmostEqual(self.pv1.get_mag(), 10, 3)
        self.assertAlmostEqual(self.pv1.get_ang(), 0.5, 3)

    def test_setters_invalid(self):
        """v1.x = a; v1.get_y()=a"""
        with self.assertRaises(AttributeError):
            self.pv1.set_x(3)

        with self.assertRaises(AttributeError):
            self.pv1.set_y(4)

    def test_eq(self):
        """v1 == v2"""
        self.assertEqual(self.pv1, self.pv1_eq)
        self.assertNotEqual(self.pv1, self.pv2)

    def test_conversions(self):
        """rectangular(v) and polar(v)"""
        # Uncomment lines below when you have RectangularVector working
        self.assertEqual(self.pv1.rectangular(), RV(3, 4))
        self.assertEqual(self.pv1.polar(), PV(5, 0.927295))

        self.assertEqual(self.pv2.rectangular(), RV(5, 12))
        self.assertEqual(self.pv2.polar(), PV(13, 1.176))


if __name__ == "__main__":
    unittest.main()
