class Foo:
    """A class called Foo."""

    def __init__(self, name: str, profession: str) -> None:
        """Create Foo instance."""
        self.name = name
        self.profession = profession

    def speak(self) -> str:
        """Say hi."""
        return f"{self.name} says hello!"

    def __repr__(self) -> str:
        """Return the str representation of Foo."""
        return f"Foo({self.name}, {self.profession})"
