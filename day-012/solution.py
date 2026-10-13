from typing import List


def set_zeroes(matrix: List[List[int]]) -> None:
    """Zero out the row and column of every 0, in place.

    Two passes: first mark which rows/columns contain a zero, then
    rewrite them. O(m*n) time, O(m + n) space.
    """
    rows = len(matrix)
    if rows == 0:
        return
    cols = len(matrix[0])

    zero_rows = set()
    zero_cols = set()
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    for i in range(rows):
        for j in range(cols):
            if i in zero_rows or j in zero_cols:
                matrix[i][j] = 0


if __name__ == "__main__":
    m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    set_zeroes(m)
    assert m == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    m = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    set_zeroes(m)
    assert m == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

    m = [[1, 2, 3]]
    set_zeroes(m)
    assert m == [[1, 2, 3]]

    print("all cases passed")
