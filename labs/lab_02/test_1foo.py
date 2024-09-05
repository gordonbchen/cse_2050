from Foo import Foo
import unittest

# These test method names include numbers so Gradescope's autograder
#  displays them in a nice order. If you were writing this file, you
# should probably do something like:
#
#     class TestFoo(unittest.TestCase):
#         def setUp(self): ...
#         def test_init(self): ...
#         def test_speak(self): ...
#         def test_repr(self): ...
#     unittest.main()


class TestFoo(unittest.TestCase):
    def setUp(self):
        """Runs before every test, so every test has access to
        unmodified versions of these objects.
        """
        self.foo1 = Foo("jake", "Professor")
        self.foo2 = Foo("rachel", "Carpenter")

    def test_10_init(self):
        """Checks that name and profession are initialized"""
        self.assertEqual(self.foo1.name, "jake")
        self.assertEqual(self.foo1.profession, "Professor")

        self.assertEqual(self.foo2.name, "rachel")
        self.assertEqual(self.foo2.profession, "Carpenter")

    def test_11_speak(self):
        """obj.speak() -> obj.name says hello!"""
        self.assertEqual(self.foo1.speak(), "jake says hello!")
        self.assertEqual(self.foo2.speak(), "rachel says hello!")

    def test_12_repr(self):
        """repr(obj) -> Foo(obj.name, obj.profession)"""
        self.assertEqual(repr(self.foo1), "Foo(jake, Professor)")
        self.assertEqual(repr(self.foo2), "Foo(rachel, Carpenter)")


if __name__ == "__main__":
    unittest.main()
