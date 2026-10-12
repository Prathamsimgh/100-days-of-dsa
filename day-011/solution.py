from typing import List


def sort_colors(nums: List[int]) -> None:
    """Sort an array of 0s, 1s and 2s in-place, single pass.

    Dutch National Flag: three pointers split the array into a 0s
    region [0..low), a 1s region [low..mid), an unprocessed region
    [mid..high] and a 2s region (high..n). Each element is visited once.
    O(n) time, O(1) space.
    """
    low = mid = 0
    high = len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


if __name__ == "__main__":
    for arr, expected in [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
        ([0], [0]),
        ([1], [1]),
        ([2, 2, 2], [2, 2, 2]),
        ([], []),
        ([0, 0, 0, 1, 1, 1, 2, 2, 2], [0, 0, 0, 1, 1, 1, 2, 2, 2]),
        ([2, 1, 0], [0, 1, 2]),
        ([1, 2, 0, 1, 2, 0, 1], [0, 0, 1, 1, 1, 2, 2]),
    ]:
        sort_colors(arr)
        assert arr == expected, (arr, expected)
    print("all cases passed")
