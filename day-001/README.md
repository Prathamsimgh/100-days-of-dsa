# Day 1 — Two Sum

**Topic:** Arrays

## Problem

Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to `target`. Exactly one solution exists.

## Approach

Single pass with a hash map. For each number, look up `target - num` among
previously seen values — if found, return both indices; otherwise store the
current number and its index.

The brute-force O(n²) pair check works too, but the hash map drops it to
linear time at the cost of linear space.

## Complexity

- Time: O(n)
- Space: O(n)

## Edge cases

- Duplicate values (`[3, 3]`, target 6) — the map lookup happens before
  inserting the current element, so an element never pairs with itself.
