def longest_common_prefix(strs: list[str]) -> str:
    """Longest string that is a prefix of every string in the list.

    Vertical scan: compare characters column by column across all strings,
    stopping at the first mismatch or the end of the shortest string.
    O(S) time where S is the total character count, O(1) extra space.
    """
    if not strs:
        return ""
    for i, ch in enumerate(strs[0]):
        for s in strs[1:]:
            if i >= len(s) or s[i] != ch:
                return strs[0][:i]
    return strs[0]


if __name__ == "__main__":
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""
    assert longest_common_prefix(["a"]) == "a"
    assert longest_common_prefix(["", "abc"]) == ""
    assert longest_common_prefix([]) == ""
    assert longest_common_prefix(["abc", "abc", "abc"]) == "abc"
    assert longest_common_prefix(["abcd", "abce", "ab"]) == "ab"
    assert longest_common_prefix(["interspecies", "interstellar", "interstate"]) == "inters"
    print("all tests passed")
