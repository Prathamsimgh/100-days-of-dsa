from collections import Counter


def min_window(s: str, t: str) -> str:
    """Smallest substring of s containing every character of t (with counts).

    Sliding window: expand the right edge until the window covers t, then
    shrink the left edge as far as possible while it still does. The
    `formed` counter tracks how many distinct characters have reached their
    required count, so each end moves only O(n). O(n) time, O(m) space
    where m is the number of distinct characters in t.
    """
    if not s or not t:
        return ""
    need: dict[str, int] = Counter(t)
    required = len(need)
    formed = 0
    window: dict[str, int] = {}
    left = 0
    best = (0, len(s) + 1)  # (start, length)

    for right, ch in enumerate(s):
        if ch in need:
            window[ch] = window.get(ch, 0) + 1
            if window[ch] == need[ch]:
                formed += 1

        while formed == required:
            if right - left + 1 < best[1]:
                best = (left, right - left + 1)
            left_ch = s[left]
            if left_ch in need:
                window[left_ch] -= 1
                if window[left_ch] < need[left_ch]:
                    formed -= 1
            left += 1

    start, length = best
    return "" if length == len(s) + 1 else s[start:start + length]


if __name__ == "__main__":
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""
    assert min_window("ab", "b") == "b"
    assert min_window("abc", "cba") == "abc"
    assert min_window("aaab", "aab") == "aab"
    assert min_window("", "a") == ""
    assert min_window("a", "") == ""
    print("all tests passed")
