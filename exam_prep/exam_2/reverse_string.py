def reverse_string(letters: str) -> str:
    """Recursively reverse a string."""
    if len(letters) <= 1:
        return letters
    return reverse_string(letters[1:]) + letters[0]


if __name__ == "__main__":
    print(reverse_string("abcd"))
