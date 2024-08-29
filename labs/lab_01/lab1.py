def generic_hi(name: str = "world") -> str:
    """Say hi with a default name."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(generic_hi("jake"))
    print(generic_hi("greninja"))
    print(generic_hi())
