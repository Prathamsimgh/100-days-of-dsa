from typing import List


def find_min(nums: List[int]) -> int:
    """Return the minimum of a rotated sorted array (distinct elements).

    Binary search for the inflection point: at each step compare nums[mid]
    with nums[right]. If nums[mid] > nums[right], the minimum lies strictly
    right of mid; otherwise mid is a candidate and the minimum is at mid or
    left of it. The loop shrinks until lo == hi, which must be the minimum.
    O(log n) time, O(1) space.
    """
    lo, hi = 0, len(nums) - 1

    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid

    return nums[lo]


if __name__ == "__main__":
    assert find_min([3, 4, 5, 1, 2]) == 1
    assert find_min([4, 5, 6, 7, 0, 1, 2]) == 0
    assert find_min([11, 13, 15, 17]) == 11
    assert find_min([1]) == 1
    assert find_min([2, 1]) == 1
    assert find_min([3, 1, 2]) == 1
    print("all cases passed")
