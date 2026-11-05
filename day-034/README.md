# Day 34 — Next Greater Element I

**Topic:** Stacks & Queues

## Problem

Given two distinct arrays `nums1` and `nums2`, where `nums1` is a subset
of `nums2`, return an array where each entry is the next greater element
of the corresponding `nums1` value in `nums2` — the first element to its
right that is larger than it, or `-1` if there is none.

```
[4, 1, 2], [1, 3, 4, 2] -> [-1, 3, -1]
[2, 4], [1, 2, 3, 4] -> [3, -1]
```

## Approach

Scan `nums2` once with a monotonically decreasing stack. For each value,
pop every smaller value off the stack — the current value is their next
greater element — then push the current value. Values still on the stack
at the end have no greater element to their right, so they map to `-1`.
Answering `nums1` is then just a lookup per query.

## Complexity

- Time: O(n + m) — each element of `nums2` is pushed and popped at most once, plus one lookup per element of `nums1`.
- Space: O(n) — the stack and the map hold at most one entry per element of `nums2`.

## Edge cases

- A strictly decreasing `nums2` leaves every element on the stack, so every answer is `-1`.
- The next greater element must be to the right in `nums2`, not just larger anywhere — scanning order is what makes the stack correct.
- `nums1` may query values in any order; the map is built once from `nums2`, so query order doesn't matter.
