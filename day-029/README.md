# Day 29 — Rotate List

**Topic:** Linked Lists

## Problem

Given the head of a linked list, rotate the list to the right by `k` places.

```
1 -> 2 -> 3 -> 4 -> 5, k = 2  becomes  4 -> 5 -> 1 -> 2 -> 3
```

## Approach

One pass to find the length and the tail, then close the list into a ring
by pointing the tail at the head. The new head sits `k` places back from
the old tail, so walk `length - k % length` steps from the old head to
find the new tail and break the ring there.

Reducing `k` modulo the length first handles `k` larger than the list
(and `k` a multiple of the length leaves the list unchanged).

## Complexity

- Time: O(n) — one pass to measure the list, one partial walk to the new tail.
- Space: O(1) extra — only a handful of pointers.

## Edge cases

- Empty list or single node: returned unchanged.
- `k = 0`, or `k` a multiple of the length: returned unchanged.
- `k > length`: reduced with `k % length` before rotating.
