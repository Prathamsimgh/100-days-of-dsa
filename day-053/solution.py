from collections import deque
from typing import List


def num_islands(grid: List[List[str]]) -> int:
    """Return the number of islands in a grid of '1's (land) and '0's (water).

    An island is a group of '1's connected horizontally or vertically.
    Scan every cell; when an unvisited land cell is found, flood-fill
    the whole island with BFS and count it once. Marking visited cells
    as '0' in place keeps the extra space to the BFS queue.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "1":
                continue
            islands += 1
            grid[r][c] = "0"
            queue = deque([(r, c)])
            while queue:
                cr, cc = queue.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        queue.append((nr, nc))
    return islands


if __name__ == "__main__":
    assert num_islands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]) == 1
    assert num_islands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]) == 3
    # Empty grid and all-water grid: no islands
    assert num_islands([]) == 0
    assert num_islands([["0", "0"], ["0", "0"]]) == 0
    # Diagonally touching land is two islands, not one
    assert num_islands([["1", "0"], ["0", "1"]]) == 2
    # Single cell of land
    assert num_islands([["1"]]) == 1
    print("all cases passed")
