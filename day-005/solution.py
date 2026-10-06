from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    """Return an array where answer[i] is the product of all elements except nums[i].

    Two passes with prefix/suffix products folded into the output array:
    first fill answer with prefix products (product of everything left of i),
    then sweep right-to-left multiplying in the suffix product (everything
    right of i). O(n) time, O(1) extra space besides the output.
    """
    n = len(nums)
    answer = [1] * n

    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer


if __name__ == "__main__":
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert product_except_self([0, 0]) == [0, 0]
    assert product_except_self([5]) == [1]
    assert product_except_self([2, 0, 4]) == [0, 8, 0]
    print("all cases passed")
