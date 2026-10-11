from typing import List


def subarray_sum(nums: List[int], k: int) -> int:
    """Count subarrays whose elements sum to k.

    One pass with a prefix-sum frequency map: for each running prefix
    sum s, the number of subarrays ending here with sum k equals the
    count of earlier prefix sums equal to s - k. O(n) time, O(n) space.
    """
    prefix_counts = {0: 1}
    running = 0
    total = 0
    for num in nums:
        running += num
        total += prefix_counts.get(running - k, 0)
        prefix_counts[running] = prefix_counts.get(running, 0) + 1
    return total


if __name__ == "__main__":
    assert subarray_sum([1, 1, 1], 2) == 2
    assert subarray_sum([1, 2, 3], 3) == 2
    assert subarray_sum([-1, -1, 1], 0) == 1
    assert subarray_sum([1, -1, 0], 0) == 3
    assert subarray_sum([], 5) == 0
    assert subarray_sum([1], 0) == 0
    print("all cases passed")
