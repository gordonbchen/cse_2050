from string import ascii_lowercase


def count_letters(text: str) -> dict:
    """Count the frequency of standard ascii lowercase chars."""
    freqs = {}
    for char in text.lower():
        if char in ascii_lowercase:
            freqs[char] = freqs.get(char, 0) + 1

    return freqs


if __name__ == "__main__":
    with open("frost.txt", mode="r") as f:
        text = f.read()

    print(text)

    print(count_letters(text))
