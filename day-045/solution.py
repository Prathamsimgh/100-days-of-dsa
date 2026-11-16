import heapq
from typing import List


def find_kth_largest(nums: List[int], k: int) -> int:
    """Return the kth largest element in the array.

    Keep a min-heap of the k largest elements seen so far. For each number,
    push it on the heap and pop the smallest whenever the heap grows past k.
    At the end the heap root is the kth largest. O(n log k) time, O(k) space.
    """
    heap: List[int] = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


if __name__ == "__main__":
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert find_kth_largest([1], 1) == 1
    assert find_kth_largest([7, 7, 7, 7], 3) == 7
    assert find_kth_largest([-1, -2, -3, -4], 2) == -2
    print("all tests passed")
