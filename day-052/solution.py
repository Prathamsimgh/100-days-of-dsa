import heapq
from typing import List


def k_smallest_pairs(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    """Return the k pairs (u, v) with the smallest sums, u from nums1, v from nums2.

    Both arrays are sorted ascending. Seed a min-heap with the smallest
    possible pair (0, 0); each pop yields the next smallest sum, and its
    neighbours (i + 1, j) and (i, j + 1) are the only pairs that can
    follow it. A visited set keeps each index pair in the heap at most
    once, so every popped pair is in increasing sum order.
    """
    if not nums1 or not nums2 or k <= 0:
        return []

    heap = [(nums1[0] + nums2[0], 0, 0)]
    visited = {(0, 0)}
    result = []

    while heap and len(result) < k:
        _, i, j = heapq.heappop(heap)
        result.append([nums1[i], nums2[j]])
        if i + 1 < len(nums1) and (i + 1, j) not in visited:
            visited.add((i + 1, j))
            heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
        if j + 1 < len(nums2) and (i, j + 1) not in visited:
            visited.add((i, j + 1))
            heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
    return result


if __name__ == "__main__":
    assert k_smallest_pairs([1, 7, 11], [2, 4, 6], 3) == [[1, 2], [1, 4], [1, 6]]
    assert k_smallest_pairs([1, 1, 2], [1, 2, 3], 2) == [[1, 1], [1, 1]]
    # k larger than the number of pairs: return all pairs
    assert k_smallest_pairs([1, 2], [3], 3) == [[1, 3], [2, 3]]
    # Empty input or k = 0: nothing to pair
    assert k_smallest_pairs([], [1], 1) == []
    assert k_smallest_pairs([1], [2], 0) == []
    # Duplicates in the inputs produce duplicate pairs in order
    assert k_smallest_pairs([1, 1], [1, 1], 3) == [[1, 1], [1, 1], [1, 1]]
    print("all cases passed")
