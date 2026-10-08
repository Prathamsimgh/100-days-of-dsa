from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """Merge all overlapping intervals, returning non-overlapping coverage.

    Sort by start, then sweep once: track the interval being built; extend
    its end when the next interval overlaps, otherwise close it and start
    a new one. O(n log n) time (sort dominates), O(n) output space.
    """
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda iv: iv[0])
    merged = [list(intervals[0])]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


if __name__ == "__main__":
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge([[1, 4], [0, 4]]) == [[0, 4]]
    assert merge([[2, 3], [4, 5], [6, 7]]) == [[2, 3], [4, 5], [6, 7]]
    assert merge([]) == []
    assert merge([[5, 5]]) == [[5, 5]]
    print("all cases passed")
