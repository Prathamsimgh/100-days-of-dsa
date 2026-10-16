def length_of_longest_substring(s: str) -> int:
    """Return the length of the longest substring without repeating chars.

    Sliding window with a hash map of char -> last index. The window's left
    edge only ever moves forward: when a duplicate is seen inside the
    window, jump left past its previous occurrence. O(n) time, O(min(n, m))
    space where m is the alphabet size.
    """
    last_seen: dict[str, int] = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring(" ") == 1
    assert length_of_longest_substring("dvdf") == 3
    print("all tests passed")
