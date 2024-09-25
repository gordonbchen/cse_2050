class Animal:
    """An animal."""

    def __init__(self, name: str, sound: str, species: str) -> None:
        """Initialize the animal."""
        self.name = name
        self.sound = sound
        self.species = species


class Dog(Animal):
    """A dog."""

    def __init__(self, name: str, sound: str, species: str, is_good_boy: bool) -> None:
        """Initialize the dog."""
        super().__init__(name, sound, species)
        self.is_good_boy = is_good_boy


class Cat(Animal):
    """A cat."""

    def __init__(self, name: str, sound: str, species: str) -> None:
        """Initialize the cat."""
        super().__init__(name, sound, species)


c = Cat("gordon", "meow", "cat")
print(c.name)
