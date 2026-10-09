from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """Return all unique triplets [a, b, c] with a + b + c == 0.

    Sort, then for each fixed index use two pointers on the rest.
    Duplicates are skipped at all three positions. O(n^2) time, O(1)
    extra space (not counting the output list).
    """
    nums.sort()
    triplets = []
    n = len(nums)
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                triplets.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return triplets


if __name__ == "__main__":
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([0, 1, 1]) == []
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
    assert three_sum([-2, 0, 1, 1, 2]) == [[-2, 0, 2], [-2, 1, 1]]
    assert three_sum([1, 2, -2, -1]) == []
    print("all cases passed")
