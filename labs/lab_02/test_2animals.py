from Animals import Animal, Dog, Cat
import unittest

# These test method names include numbers so Gradescope's autograder
# displays them in a nice order. If you were writing this file, you
# should probably use non-numbered names like:
#
#     class TestAnimal(unittest.TestCase):
#         def setUp(self): ...
#         def test_init(self): ...
#         def test_speak(self): ...
#         def test_repr(self): ...
#     unittest.main()


class Test2_Animal(unittest.TestCase):
    def setUp(self):
        """Runs before every test, so every test has access to
        unmodified versions of these objects.
        """
        self.a1 = Animal("Arthur", "Ardvark")
        self.a2 = Animal("Colin", "Carpenter Bee", "buzz")

    def test_20_init(self):
        """Checks that name, species, and sound are initialized"""
        self.assertEqual(self.a1.name, "Arthur")
        self.assertEqual(self.a1.species, "Ardvark")
        self.assertEqual(self.a1.sound, "hi")

        self.assertEqual(self.a2.name, "Colin")
        self.assertEqual(self.a2.species, "Carpenter Bee")
        self.assertEqual(self.a2.sound, "buzz")

    def test_21_speak(self):
        """obj.speak() -> name, a species, says sound!"""
        self.assertEqual(self.a1.speak(), "Arthur, a Ardvark, says hi!")
        self.assertEqual(self.a2.speak(), "Colin, a Carpenter Bee, says buzz!")

    def test_22_repr(self):
        """repr(obj) -> Animal(name, species, sound)"""
        self.assertEqual(repr(self.a1), "Animal(Arthur, Ardvark, hi)")
        self.assertEqual(repr(self.a2), "Animal(Colin, Carpenter Bee, buzz)")

    def test_23_inheritances(self):
        "Animal objects should not be Dogs or Cats"
        self.assertIsInstance(self.a1, Animal)
        self.assertNotIsInstance(self.a1, Dog)
        self.assertNotIsInstance(self.a1, Cat)


class Test3_Dog(unittest.TestCase):
    def setUp(self):
        """Runs before every test, so every test has access to
        unmodified versions of these objects.
        """
        self.d1 = Dog("Arthur")
        self.d2 = Dog("Colin")

    def test_30_init(self):
        """Checks that name, species, sound, and is_good_boy are initialized"""
        self.assertEqual(self.d1.name, "Arthur")
        self.assertEqual(self.d1.species, "dog")
        self.assertEqual(self.d1.sound, "ruff")
        self.assertTrue(self.d1.is_good_boy)

        self.assertEqual(self.d2.name, "Colin")
        self.assertEqual(self.d2.species, "dog")
        self.assertEqual(self.d2.sound, "ruff")
        self.assertTrue(self.d2.is_good_boy)

    def test_31_speak(self):
        """obj.speak() -> name, a species, says sound!"""
        self.assertEqual(self.d1.speak(), "Arthur, a dog, says ruff!")
        self.assertEqual(self.d2.speak(), "Colin, a dog, says ruff!")

    def test_32_repr(self):
        """repr(obj) -> Dog(name)"""
        self.assertEqual(repr(self.d1), "Dog(Arthur)")
        self.assertEqual(repr(self.d2), "Dog(Colin)")

    def test_33_inheritances(self):
        "Dog objects should be Dogs and Animals"
        self.assertIsInstance(self.d1, Dog)
        self.assertIsInstance(self.d1, Animal)
        self.assertNotIsInstance(self.d1, Cat)


class Test4_Cat(unittest.TestCase):
    def setUp(self):
        """Runs before every test, so every test has access to
        unmodified versions of these objects.
        """
        self.c1 = Cat("Arthur", "cat", "meow")
        self.c2 = Cat("Colin", "cat", "meow")

    def test_40_init(self):
        """Checks that name, species, and sound are initialized"""
        self.assertEqual(self.c1.name, "Arthur")
        self.assertEqual(self.c1.species, "cat")
        self.assertEqual(self.c1.sound, "meow")

        self.assertEqual(self.c2.name, "Colin")
        self.assertEqual(self.c2.species, "cat")
        self.assertEqual(self.c2.sound, "meow")

    def test_41_speak(self):
        """obj.speak() -> name, a species, says sound!"""
        self.assertEqual(self.c1.speak(), "Arthur, a cat, says meow!")
        self.assertEqual(self.c2.speak(), "Colin, a cat, says meow!")

    def test_42_repr(self):
        """repr(obj) -> Cat(name, species, sound)"""
        self.assertEqual(repr(self.c1), "Cat(Arthur, cat, meow)")
        self.assertEqual(repr(self.c2), "Cat(Colin, cat, meow)")

    def test_43_inheritances(self):
        "cat objects should be Cats and Animals"
        self.assertIsInstance(self.c1, Cat)
        self.assertIsInstance(self.c1, Animal)
        self.assertNotIsInstance(self.c1, Dog)


if __name__ == "__main__":
    unittest.main()
