def _lps(pattern: str) -> list[int]:
    """Longest-proper-prefix-which-is-also-suffix table for KMP.

    lps[i] = length of the longest proper prefix of pattern[:i+1] that is
    also a suffix of pattern[:i+1].
    """
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
    return lps


def str_str(haystack: str, needle: str) -> int:
    """Index of the first occurrence of needle in haystack, -1 if absent.

    KMP: on a mismatch, the LPS table tells us how far to rewind the
    needle pointer instead of restarting from its beginning, so the
    haystack pointer never moves backwards. O(n + m) time, O(m) space.
    """
    if not needle:
        return 0
    table = _lps(needle)
    i = j = 0
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            if j == len(needle):
                return i - j
        elif j != 0:
            j = table[j - 1]
        else:
            i += 1
    return -1


if __name__ == "__main__":
    assert str_str("sadbutsad", "sad") == 0
    assert str_str("leetcode", "leeto") == -1
    assert str_str("hello", "ll") == 2
    assert str_str("mississippi", "issip") == 4
    assert str_str("aaaaab", "aaab") == 2        # overlapping prefixes
    assert str_str("abc", "") == 0              # empty needle convention
    assert str_str("", "a") == -1
    assert str_str("a", "a") == 0
    assert str_str("abcabcd", "abcd") == 3      # naive scan backtracks badly here
    assert str_str("ababababca", "abababca") == 2
    assert str_str("aaa", "aaaa") == -1
    print("all tests passed")
