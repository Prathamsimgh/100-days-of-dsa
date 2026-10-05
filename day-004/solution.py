from typing import List


def max_area(height: List[int]) -> int:
    """Return the maximum water container area.

    Two pointers at both ends: area is min(height[l], height[r]) * (r - l).
    Move the shorter pointer inward, since only a taller line on that side
    can beat the current area. O(n) time, O(1) space.
    """
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        width = right - left
        if height[left] < height[right]:
            best = max(best, height[left] * width)
            left += 1
        else:
            best = max(best, height[right] * width)
            right -= 1
    return best


if __name__ == "__main__":
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([4, 3, 2, 1, 4]) == 16
    assert max_area([1, 2, 1]) == 2
    print("all cases passed")
