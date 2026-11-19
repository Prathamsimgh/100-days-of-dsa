import heapq
from typing import List


class MedianFinder:
    """Maintain the median of a stream of integers.

    Two heaps: ``low`` is a max-heap (stored negated) holding the lower
    half, ``high`` is a min-heap holding the upper half. ``low`` may hold
    at most one element more than ``high``, so the median is either the
    top of ``low`` (odd count) or the average of the two tops (even).
    """

    def __init__(self) -> None:
        self.low: List[int] = []   # max-heap via negation
        self.high: List[int] = []  # min-heap

    def add_num(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        # The largest of the lower half must not exceed the smallest
        # of the upper half — move it across if it does.
        heapq.heappush(self.high, -heapq.heappop(self.low))
        # Rebalance so low holds the extra element when the count is odd.
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def find_median(self) -> float:
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2


if __name__ == "__main__":
    mf = MedianFinder()
    mf.add_num(1)
    mf.add_num(2)
    assert mf.find_median() == 1.5
    mf.add_num(3)
    assert mf.find_median() == 2.0
    mf.add_num(4)
    assert mf.find_median() == 2.5
    mf.add_num(5)
    assert mf.find_median() == 3.0
    # Negative numbers and duplicates
    mf2 = MedianFinder()
    for n in [-5, -5, 0, 10]:
        mf2.add_num(n)
    assert mf2.find_median() == -2.5
    print("all cases passed")
