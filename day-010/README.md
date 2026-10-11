# Day 10 — Subarray Sum Equals K

**Topic:** Arrays

## Problem

Given an array of integers `nums` and an integer `k`, return the total
number of subarrays whose elements sum to `k`.

## Approach

Prefix sums with a frequency map. For each running prefix sum `s`, any
earlier prefix sum equal to `s - k` marks a subarray ending at the current
position that sums to `k`, so add its count to the answer and then record
the current prefix sum in the map.

The brute-force O(n²) scan of all subarrays works, but the map drops it
to a single pass at the cost of linear space.

## Complexity

- Time: O(n)
- Space: O(n)

## Edge cases

- Negative numbers are fine — the map handles non-monotonic prefix sums,
  unlike a sliding window.
- The empty prefix sum (`0: 1` seed) counts subarrays that start at
  index 0.
- An empty array returns 0 with no special-casing.
