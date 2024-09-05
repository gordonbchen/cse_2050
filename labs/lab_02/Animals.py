class Animal:
    """A class that represents an animal."""

    def __init__(self, name: str, species: str = "animal", sound: str = "hi") -> None:
        """Initialize animal."""
        self.name = name
        self.species = species
        self.sound = sound

    def speak(self) -> str:
        """Make a sound."""
        return f"{self.name}, a {self.species}, says {self.sound}!"

    def __repr__(self) -> str:
        """Return a str representation of the animal."""
        return f"Animal({self.name}, {self.species}, {self.sound})"


class Dog(Animal):
    """A class that represents a dog."""

    def __init__(self, name: str, is_good_boy: bool = True) -> None:
        """Initialize the dog."""
        super().__init__(name, species="dog", sound="ruff")
        self.is_good_boy = is_good_boy

    def __repr__(self) -> str:
        """Return a str representation of the dog."""
        return f"Dog({self.name})"


class Cat(Animal):
    """A class that represents a cat."""

    def __repr__(self) -> str:
        """Return a str representation of the cat."""
        return f"Cat({self.name}, {self.species}, {self.sound})"


if __name__ == "__main__":
    a1 = Animal("Arthur", "Ardvark")
    d1 = Dog("Doug")
    c1 = Cat("Caroline", "calico cat", "meow")
    print(a1, d1, c1)
    print(a1.speak(), d1.speak(), c1.speak())
