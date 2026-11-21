import heapq
from collections import Counter
from typing import List


def least_interval(tasks: List[str], n: int) -> int:
    """Return the fewest intervals needed to run all tasks.

    Same-type tasks need at least n other intervals between them, so
    idle slots only appear while the most frequent task waits for its
    cooldown. A max-heap of remaining counts drives each cycle of
    n + 1 slots: pop up to n + 1 tasks, run each once, and push back
    the ones still unfinished. A cycle with no tasks left waiting
    finishes early — no idle slots are added for it.
    """
    counts = Counter(tasks)
    heap = [-c for c in counts.values()]
    heapq.heapify(heap)

    intervals = 0
    while heap:
        cycle = []
        run = 0
        for _ in range(n + 1):
            if not heap:
                break
            count = -heapq.heappop(heap)
            if count > 1:
                cycle.append(count - 1)
            intervals += 1
            run += 1
        for count in cycle:
            heapq.heappush(heap, -count)
        if heap:
            intervals += (n + 1) - run
    return intervals


if __name__ == "__main__":
    assert least_interval(["A", "A", "A", "B", "B", "B"], 2) == 8
    assert least_interval(["A", "C", "A", "B", "D", "B"], 1) == 6
    assert least_interval(["A", "A", "A", "B", "B", "B"], 0) == 6
    # Single task type — idle slots fill every gap
    assert least_interval(["A", "A", "A", "A"], 3) == 13
    # One of each — no cooldown ever applies
    assert least_interval(["A", "B", "C", "D"], 2) == 4
    # Cooldown larger than the task list
    assert least_interval(["A", "B"], 5) == 2
    print("all cases passed")
