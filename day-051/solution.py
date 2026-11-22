import heapq
from typing import List


def last_stone_weight(stones: List[int]) -> int:
    """Return the weight of the last remaining stone.

    Repeatedly smash the two heaviest stones together: if they weigh
    the same both are destroyed, otherwise the lighter one is destroyed
    and a stone of the weight difference remains. A max-heap (negated,
    since Python's heap is a min-heap) always yields the two heaviest
    stones, so each smash is one pop, one pop, and at most one push.
    """
    heap = [-s for s in stones]
    heapq.heapify(heap)

    while len(heap) > 1:
        heaviest = -heapq.heappop(heap)
        second = -heapq.heappop(heap)
        if heaviest != second:
            heapq.heappush(heap, -(heaviest - second))
    return -heap[0] if heap else 0


if __name__ == "__main__":
    assert last_stone_weight([2, 7, 4, 1, 8, 1]) == 1
    assert last_stone_weight([1]) == 1
    assert last_stone_weight([2, 2]) == 0
    # Heaviest pair cancels, then the rest cancel in pairs
    assert last_stone_weight([5, 5, 3, 3]) == 0
    # Single smash leaves the difference
    assert last_stone_weight([10, 4]) == 6
    # Large stone absorbs the smaller ones one by one
    assert last_stone_weight([9, 3, 2, 10]) == 0
    print("all cases passed")
