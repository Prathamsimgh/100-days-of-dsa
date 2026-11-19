# Day 48 — Find Median from Data Stream

**Topic:** Heaps

## Problem

Design a data structure that supports adding integers from a stream and
returning the median of all elements seen so far. `addNum(num)` inserts a
number; `findMedian()` returns the median of the current stream.

## Approach

Two heaps split the stream into a lower half and an upper half. `low` is a
max-heap (values stored negated) holding the smaller half, `high` is a
min-heap holding the larger half. On each insert, the number goes into
`low`, the largest element of `low` moves to `high`, and the heaps are
rebalanced so `low` holds at most one element more than `high`. With that
invariant the median is the top of `low` when the count is odd, or the
average of the two tops when it is even.

A single sorted list would make insertion O(n); the two-heap split keeps
every operation logarithmic.

## Complexity

- Time: O(log n) per `addNum`, O(1) per `findMedian`
- Space: O(n)

## Edge cases

- Even count — the median is the average of the two middle values, so
  `findMedian` returns a float even for integer inputs.
- Duplicates and negative numbers — the heap ordering handles both; the
  negation trick for the max-heap works for any integer.
