import heapq
from collections import Counter
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """Return the k most frequent elements in nums, in any order.

    Count frequencies once, then keep a min-heap of size k keyed by
    frequency: the heap root is always the least frequent of the
    current top k, so any element more frequent than it replaces it.
    O(n log k) time, O(n) space for the counts plus O(k) for the heap.
    """
    counts = Counter(nums)
    heap: List[tuple[int, int]] = []  # (frequency, value)
    for num, freq in counts.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for _, num in heap]


def top_k_frequent_builtin(nums: List[int], k: int) -> List[int]:
    """Same result via heapq.nlargest — simpler, same complexity."""
    counts = Counter(nums)
    return [num for num, _ in heapq.nlargest(k, counts.items(),
                                             key=lambda item: item[1])]


if __name__ == "__main__":
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert top_k_frequent([1], 1) == [1]
    assert sorted(top_k_frequent([4, 4, 4, 4, 2, 2, 3, 3, 3], 2)) == [3, 4]
    assert sorted(top_k_frequent([1, 2, 3], 3)) == [1, 2, 3]
    # k equal to the number of distinct elements: everything comes back.
    assert sorted(top_k_frequent([-1, -1, 0, 0, 0, 5], 3)) == [-1, 0, 5]
    for fn in (top_k_frequent, top_k_frequent_builtin):
        assert sorted(fn([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    print("all self-tests passed")
