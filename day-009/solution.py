from typing import List


def trap(height: List[int]) -> int:
    """Return the total units of rainwater trapped between bars.

    Two pointers from both ends: move the pointer on the side with the
    smaller bar height, since the trapped water at that position is bounded
    by the smaller of the two running max heights. O(n) time, O(1) space.
    """
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water


if __name__ == "__main__":
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert trap([4, 2, 0, 3, 2, 5]) == 9
    assert trap([3, 0, 3]) == 3
    assert trap([1, 2, 3, 4]) == 0
    assert trap([4, 3, 2, 1]) == 0
    assert trap([]) == 0
    assert trap([5]) == 0
    print("all cases passed")
