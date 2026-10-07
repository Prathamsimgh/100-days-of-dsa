# Day 6 — Find Minimum in Rotated Sorted Array

**Topic:** Arrays

## Problem

Given a sorted array of distinct integers that has been rotated an unknown
number of times (e.g. `[0,1,2,4,5,6,7]` became `[4,5,6,7,0,1,2]`), return
the minimum element. The algorithm should run in O(log n) time.

## Approach

Binary search for the rotation point — the index where the order breaks.
Compare `nums[mid]` against the right end `nums[hi]`:

- If `nums[mid] > nums[hi]`, the minimum must be strictly to the right of
  `mid` (the right half contains the wrap), so `lo = mid + 1`.
- Otherwise `mid` itself is a candidate minimum and everything to its
  right is too large, so `hi = mid`.

Each iteration halves the search window, and `lo == hi` converges exactly
on the minimum. The comparison against the right end (not the left) works
because the right end is always in the rotated segment when one exists.

A linear scan works too (O(n)), but wastes the rotation structure.

## Complexity

- Time: O(log n) — halving the window each step
- Space: O(1) — two pointers only

## Edge cases

- No rotation (`[11,13,15,17]`): `nums[mid] <= nums[hi]` always holds, so
  `hi` walks down to index 0 and the answer is `nums[0]`.
- Single element: the loop never runs; returns `nums[0]`.
- Rotation of one (`[2,1]`): `mid` equals `lo`, the left-half test pushes
  `lo` past it, and `hi` stays at the minimum.
- Distinct elements assumed — with duplicates the worst case degrades
  toward O(n) and needs extra handling.
