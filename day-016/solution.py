from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """Group anagrams together using a character-frequency signature.

    Each word is mapped to a 26-length count tuple, which is identical for
    anagrams and different otherwise. A hash map from signature -> word
    list does the grouping in a single pass. O(n*k) time where n is the
    number of words and k the max word length, O(n*k) space for the map.
    """
    groups: dict[tuple[int, ...], list[str]] = defaultdict(list)
    for word in strs:
        counts = [0] * 26
        for ch in word:
            counts[ord(ch) - ord("a")] += 1
        groups[tuple(counts)].append(word)
    return list(groups.values())


def _norm(groups: list[list[str]]) -> list[list[str]]:
    return sorted(sorted(g) for g in groups)


if __name__ == "__main__":
    got = _norm(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    want = _norm([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
    assert got == want

    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert _norm(group_anagrams(["ab", "ba", "cd"])) == _norm(
        [["ab", "ba"], ["cd"]]
    )
    assert group_anagrams([]) == []
    print("all tests passed")
