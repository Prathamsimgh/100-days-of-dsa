# Day 45 — Kth Largest Element in an Array

**Topic:** Heaps

## Problem

Given an integer array `nums` and an integer `k`, return the kth largest
element in the array (not the kth distinct element). The array may contain
duplicates, and `1 <= k <= len(nums)`.

## Approach

Keep a min-heap of the k largest elements seen so far. For each number,
push it onto the heap; if the heap grows past size k, pop the smallest.
Once every number has been processed, the heap holds exactly the k largest
elements and its root — the smallest of them — is the kth largest overall.

## Complexity

- Time: O(n log k) — one heap push/pop per element, heap size capped at k
- Space: O(k) — the heap holds at most k elements

## Edge cases

- `k == 1` — returns the maximum element.
- `k == len(nums)` — returns the minimum element.
- All elements equal (`[7, 7, 7, 7]`, k = 3) — returns 7.
- Negative numbers — the heap comparison works the same way.
