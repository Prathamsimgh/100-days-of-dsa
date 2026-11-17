# Day 46 — Top K Frequent Elements

**Topic:** Heaps

## Problem

Given an integer array `nums` and an integer `k`, return the `k` most
frequent elements, in any order.

Example: `nums = [1, 1, 1, 2, 2, 3]`, `k = 2` → `[1, 2]`.

## Approach

Count frequencies with a hash map in one pass, then keep a min-heap of
size `k` keyed by frequency. Push each `(frequency, value)` pair onto
the heap and pop whenever it grows past `k` — the heap root is always
the least frequent of the current top `k`, so anything more frequent
than it takes its place. When every distinct element has been seen,
the heap holds exactly the top `k`.

Sorting all frequencies would also work, but the bounded heap avoids
paying `O(n log n)` for the sort; only the `k` survivors are ever
ordered. `heapq.nlargest` does the same thing in one call and is the
shorter way to write it in practice.

## Complexity

- Time: O(n log k) — one counting pass plus one heap push/pop per
  distinct element, each costing O(log k).
- Space: O(n) — the frequency map; the heap itself is O(k).

## Edge cases

- `k` equals the number of distinct elements — every element is
  returned.
- All elements identical — the heap never exceeds size 1.
- Negative numbers — frequencies are what matter, values are never
  compared as heap keys alone (the pair is `(freq, value)`, so ties
  break on the value without affecting correctness).
- `k = 1` — the heap holds just the single most frequent element.
