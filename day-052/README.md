# Day 52 — Find K Pairs with Smallest Sums

**Topic:** Heaps

## Problem

Given two integer arrays `nums1` and `nums2`, both sorted in ascending
order, return the `k` pairs `(u, v)` — one element from each array — with
the smallest sums `u + v`. If fewer than `k` pairs exist, return them all.

## Approach

Seed a min-heap with the smallest possible pair, indices `(0, 0)`.
Each pop yields the next smallest sum, and the only pairs that can
follow it are its neighbours `(i + 1, j)` and `(i, j + 1)`, so push
those into the heap when they are in bounds. A visited set keeps each
index pair in the heap at most once, which guarantees the popped pairs
come out in increasing sum order.

## Complexity

- Time: O(k log k) — at most `k` pops and two pushes per pop, and the
  heap never holds more than about `k` entries
- Space: O(k) — the heap, the visited set, and the result

## Edge cases

- Either array empty, or `k = 0` — no pairs to return.
- `k` larger than `len(nums1) * len(nums2)` — return every pair.
- Duplicate values in the inputs produce duplicate pairs, still in
  increasing sum order.
