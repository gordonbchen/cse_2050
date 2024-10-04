def reverse_str_recursive(letters: str) -> str:
    """Reverse a string recursively."""
    if len(letters) == 1:
        return letters
    return letters[-1] + reverse_str_recursive(letters[:-1])


def reverse_str_iterative(letters: str) -> str:
    """Reverse a string iteratively."""
    reversed_letters = ""
    for letter in letters:
        reversed_letters = letter + reversed_letters
    return reversed_letters


if __name__ == "__main__":
    print(reverse_str_recursive("hello world!"))
    print(reverse_str_iterative("hello world!"))
