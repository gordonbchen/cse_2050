import unittest

from vector import Vector as V, RectangularVector as RV, PolarVector as PV


class TestVector(unittest.TestCase):
    def setUp(self):
        """SetUp is run before every test."""
        # Rectangular Vectors
        self.rv1 = RV(3, 4)
        self.rv2 = RV(5, 12)

        # PolarVectors
        self.pv1 = PV(5, 0.927295)
        self.pv2 = PV(13, 1.176)

    def test_init(self):
        """v1 = Vector(3, 4) should raise a NotImplementedError."""
        with self.assertRaises(NotImplementedError):
            v1 = V(3, 4)  # noqa

    def test_add_rvs(self):
        """rv1 + rv2 --> RectangularVector(a, b)"""
        u_expected = RV(8, 16)
        self.assertEqual(self.rv1 + self.rv2, u_expected)

    def test_add_mixed(self):
        """rv1 + pv1; pv2 + rv2 --> RectangularVector(a, b)"""
        u_expected = RV(6, 8)
        self.assertEqual(self.rv1 + self.pv1, u_expected)
        self.assertEqual(self.pv1 + self.rv1, u_expected)

    def test_add_pvs(self):
        """pv1 + pv2 --> RectangularVector(a, b)"""
        u_expected = RV(8, 16)
        self.assertEqual(self.pv1 + self.pv2, u_expected)

    def test_mul(self):
        """vec * vec should raise NotImplementedError"""
        with self.assertRaises(NotImplementedError):
            self.rv1 * self.rv2

        with self.assertRaises(NotImplementedError):
            self.pv1 * self.pv2

        with self.assertRaises(NotImplementedError):
            self.rv1 * self.pv1

        with self.assertRaises(NotImplementedError):
            self.pv1 * self.rv1

    def test_dot(self):
        """Vector.dot(v1, v2)"""
        self.assertEqual(self.rv1.dot(self.rv1), 25)
        self.assertEqual(self.rv1.dot(self.rv2), 63)


if __name__ == "__main__":
    unittest.main()
