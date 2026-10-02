from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """Return indices of the two numbers that add up to target.

    One pass with a hash map: for each number, check whether its
    complement (target - num) was seen before. O(n) time, O(n) space.
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    raise ValueError("no two-sum solution")


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    print("all cases passed")
