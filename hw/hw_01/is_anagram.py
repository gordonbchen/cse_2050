from count_letters import count_letters


def is_anagram(word1: str, word2: str) -> bool:
    """Return True if the word is an anagram."""
    return count_letters(word1) == count_letters(word2)


if __name__ == "__main__":
    print(is_anagram("rat", "tar"))
    print(is_anagram("rat", "hat"))
    print(is_anagram("meat", "team"))
