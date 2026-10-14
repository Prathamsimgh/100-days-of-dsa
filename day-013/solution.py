def longest_palindromic_substring(s: str) -> str:
    """Return the longest palindromic substring of s.

    Expand around center: treat every index (and every gap between
    indices) as a potential palindrome center, expand while characters
    match, and keep the longest span seen. O(n^2) time, O(1) space.
    """
    if not s:
        return ""
    start, best = 0, 1

    def span(l: int, r: int) -> int:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1  # length of the matching region

    for i in range(len(s)):
        length = max(span(i, i), span(i, i + 1))
        if length > best:
            best = length
            start = i - (length - 1) // 2
    return s[start:start + best]


if __name__ == "__main__":
    assert longest_palindromic_substring("babad") in ("bab", "aba")
    assert longest_palindromic_substring("cbbd") == "bb"
    assert longest_palindromic_substring("a") == "a"
    assert longest_palindromic_substring("ac") in ("a", "c")
    assert longest_palindromic_substring("racecar") == "racecar"
    assert longest_palindromic_substring("") == ""
    assert longest_palindromic_substring("aaaa") == "aaaa"
    print("all cases passed")
