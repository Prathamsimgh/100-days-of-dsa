"""Next Greater Element I.

Given two distinct arrays nums1 and nums2, where nums1 is a subset of
nums2, return an array ans where ans[i] is the next greater element of
nums1[i] in nums2: the first element to its right that is larger than
it. If no such element exists, the answer is -1.
"""


def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    """Monotonic stack: scan nums2 once, mapping each value to its next greater."""
    next_greater: dict[int, int] = {}
    stack: list[int] = []
    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)
    # Anything left on the stack has no greater element to its right.
    for num in stack:
        next_greater[num] = -1
    return [next_greater[num] for num in nums1]


if __name__ == "__main__":
    assert next_greater_element([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
    assert next_greater_element([2, 4], [1, 2, 3, 4]) == [3, -1]
    # Every element has a greater one to its right.
    assert next_greater_element([1, 2, 3], [1, 2, 3, 4]) == [2, 3, 4]
    # Strictly decreasing: nothing has a next greater element.
    assert next_greater_element([4, 3, 2], [4, 3, 2, 1]) == [-1, -1, -1]
    # A single element with no greater element.
    assert next_greater_element([5], [5]) == [-1]
    # Queries in a different order than nums2.
    assert next_greater_element([3, 1], [1, 3, 5]) == [5, 3]
    print("all tests passed")
