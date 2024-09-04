from __future__ import annotations

import math


class Vector:
    """Base vector class."""

    def __init__(self, *args) -> None:
        """Users should specify rectangular or polar vector instead."""
        raise NotImplementedError("Specify RectangularVector or PolarVector.")

    def get_x(self) -> float:
        """x-component of the vector."""
        return self._x

    def get_y(self) -> float:
        """y-component of the vector."""
        return self._y

    def get_mag(self) -> float:
        """Magnitude of the vector."""
        return ((self.get_x() ** 2) + (self.get_y() ** 2)) ** (1 / 2)

    def get_ang(self) -> float:
        """Angle (radians) of the vector."""
        return math.atan(self.get_y() / self.get_x())

    def __eq__(self, other: Vector) -> bool:
        """Return True if the vector components are equal."""
        x_equal = self._within_error(self.get_x(), other.get_x())
        y_equal = self._within_error(self.get_y(), other.get_y())
        return x_equal and y_equal

    def _within_error(self, a: float, b: float, abs_error: float = 0.001) -> bool:
        """Return True if abs(a - b) < abs_error."""
        return abs(a - b) < abs_error

    def __add__(self, other: Vector) -> RectangularVector:
        """Add the vector components."""
        return RectangularVector(
            self.get_x() + other.get_x(), self.get_y() + other.get_y()
        )

    def __mul__(self, other: Vector) -> None:
        """Mul is ambiguous for vectors. Use dot instead."""
        raise NotImplementedError("Mul is ambiguous for vectors. Use dot instead.")

    def rectangular(self) -> RectangularVector:
        """Return the vector as a RectangularVector."""
        return RectangularVector(self.get_x(), self.get_y())

    def polar(self) -> PolarVector:
        """Return the vector as a PolarVector."""
        return PolarVector(self.get_mag(), self.get_ang())

    def dot(self, other: Vector) -> float:
        """Return the dot product of 2 vectors."""
        return (self.get_x() * other.get_x()) + (self.get_y() * other.get_y())


class RectangularVector(Vector):
    """A vector defined by an x and y component."""

    def __init__(self, x: float, y: float) -> None:
        """Creates rectangular vector."""
        self._x = x
        self._y = y
        self._update()

    def _update(self) -> None:
        """Calculate and set magnitude and angle attributes."""
        self._mag = self.get_mag()
        self._ang = self.get_ang()

    def set_x(self, new_x: float) -> None:
        """Set x component."""
        self._x = new_x
        self._update()

    def set_y(self, new_y: float) -> None:
        """Set y component."""
        self._y = new_y
        self._update()

    def __repr__(self) -> str:
        """Return the str representation of the vector."""
        return f"RectangularVector({self.get_x()}, {self.get_y()})"


class PolarVector(Vector):
    """A vector defined by magnitude and angle."""

    def __init__(self, mag: float, ang: float) -> None:
        """Create polar vector."""
        self._mag = mag
        self._ang = ang
        self._update()

    def get_mag(self) -> float:
        """Return vector magnitude."""
        return self._mag

    def get_ang(self) -> float:
        """Return vector angle."""
        return self._ang

    def _update(self) -> None:
        """Calculate and set x and y attributes."""
        self._x = self.get_mag() * math.cos(self.get_ang())
        self._y = self.get_mag() * math.sin(self.get_ang())

    def set_mag(self, new_mag: float) -> None:
        """Set magnitude."""
        self._mag = new_mag
        self._update()

    def set_ang(self, new_ang: float) -> None:
        """Set angle."""
        self._ang = new_ang
        self._update()

    def __repr__(self) -> str:
        """Return the str representation of the vector."""
        return f"PolarVector({self.get_mag()}, {self.get_ang()})"
