import heapq
from typing import List


def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    """Return the k points closest to the origin (0, 0).

    A max-heap of size k holds the current best candidates, keyed by
    squared distance (no sqrt needed — it preserves the ordering).
    Each new point is pushed and the farthest is evicted while the heap
    is over capacity, so only the k closest survive.
    """
    heap: List[tuple] = []  # (-dist_sq, x, y): max-heap via negation
    for x, y in points:
        dist_sq = x * x + y * y
        heapq.heappush(heap, (-dist_sq, x, y))
        if len(heap) > k:
            heapq.heappop(heap)
    return [[x, y] for _, x, y in heap]


if __name__ == "__main__":
    assert sorted(k_closest([[1, 3], [-2, 2]], 1)) == [[-2, 2]]
    assert sorted(k_closest([[3, 3], [5, -1], [-2, 4]], 2)) == [[-2, 4], [3, 3]]
    # k equals the number of points — everything comes back
    assert sorted(k_closest([[0, 1], [1, 0]], 2)) == [[0, 1], [1, 0]]
    # Origin itself and duplicates
    assert sorted(k_closest([[0, 0], [0, 0], [1, 1]], 2)) == [[0, 0], [0, 0]]
    # Negative coordinates, ties on distance
    assert sorted(k_closest([[-1, -1], [1, 1], [2, 0]], 1)) in (
        [[-1, -1]],
        [[1, 1]],
    )
    print("all cases passed")
