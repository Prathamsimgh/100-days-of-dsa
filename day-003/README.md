# Day 3 — Maximum Subarray (Kadane's Algorithm)

Topic: Arrays

## Problem

Given an integer array `nums`, find the contiguous subarray (containing at
least one number) which has the largest sum, and return its sum.

Example: `[-2, 1, -3, 4, -1, 2, 1, -5, 4]` → `6` (subarray `[4, -1, 2, 1]`).

## Approach

Kadane's algorithm, single left-to-right pass. Keep two running values:

- `cur`: the maximum subarray sum **ending at** the current index.
- `best`: the maximum subarray sum seen **so far**.

For each element, either start a fresh subarray at it (`cur = num`) or
extend the previous best-ending-here (`cur = cur + num`) — whichever is
larger. The key insight: once `cur` goes negative it can only hurt any
future subarray, so dropping it never loses the optimum.

## Complexity

- Time: O(n) — one pass.
- Space: O(1) — two counters.

## Edge cases

- All numbers negative → answer is the largest (least negative) element,
  e.g. `[-3, -1, -2]` → `-1`. Starting `best = cur = nums[0]` (not 0)
  handles this.
- Single element → that element.
- Zeros-only → `0`.
