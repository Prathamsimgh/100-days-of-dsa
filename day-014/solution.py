from collections import Counter


def valid_anagram(s: str, t: str) -> bool:
    """Return True if t is an anagram of s.

    Two strings are anagrams when they contain the same characters with the
    same frequencies. Compare Counter maps of both strings. O(n) time,
    O(1)-ish space (alphabet-bounded).
    """
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


if __name__ == "__main__":
    assert valid_anagram("anagram", "nagaram") is True
    assert valid_anagram("rat", "car") is False
    assert valid_anagram("", "") is True
    assert valid_anagram("a", "ab") is False
    assert valid_anagram("listen", "silent") is True
    assert valid_anagram("aabb", "abab") is True
    print("all cases passed")
