from collections import deque
from typing import List


def oranges_rotting(grid: List[List[int]]) -> int:
    """Return the minutes until no fresh orange remains, or -1 if impossible.

    0 = empty cell, 1 = fresh orange, 2 = rotten orange. Every minute,
    each rotten orange rots its 4-directionally adjacent fresh oranges.
    Start a multi-source BFS from every rotten orange at once; the
    number of BFS layers is the minutes elapsed. Count fresh oranges
    up front so the end state is a single comparison, not a rescan.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    if fresh == 0:
        return 0

    minutes = -1
    while queue:
        minutes += 1
        for _ in range(len(queue)):
            cr, cc = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))

    return minutes if fresh == 0 else -1


if __name__ == "__main__":
    assert oranges_rotting([
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1],
    ]) == 4
    assert oranges_rotting([
        [2, 1, 1],
        [0, 1, 1],
        [1, 0, 1],
    ]) == -1
    # No fresh oranges: already done
    assert oranges_rotting([[0, 2]]) == 0
    # Empty grid: nothing to rot
    assert oranges_rotting([]) == 0
    # Single fresh orange with no rotten neighbour: impossible
    assert oranges_rotting([[1]]) == -1
    # Rot spreads in one minute
    assert oranges_rotting([[2, 1]]) == 1
    print("all cases passed")
