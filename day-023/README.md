# Day 23 — Merge Two Sorted Lists

**Topic:** Linked Lists

## Problem

Given the heads of two sorted singly-linked lists, merge them into one
sorted list by re-linking the existing nodes — i.e. return the head of the
combined list containing all nodes from both inputs, in order.

Example: `1 → 2 → 4` and `1 → 3 → 4` merge into `1 → 1 → 2 → 3 → 4 → 4`.

## Approach

Iterative two-pointer merge with a dummy head to simplify the first link.
While both lists are non-empty, compare the two current heads and attach
the smaller one to the tail of the result, advancing the pointer that won.
The comparison uses `<=` so equal values keep a stable, deterministic order.
When one list runs out, its remaining nodes are already sorted, so attach
the whole remainder with a single link — no further comparisons needed.

The key insight is that re-linking beats copying: the merged list reuses
the original nodes, so no memory is allocated beyond the dummy placeholder
(which is never part of the result).

## Complexity

- Time: O(n + m) — each node is visited exactly once before being linked.
- Space: O(1) — only the dummy pointer; all merges are in place.

## Edge cases

- Both lists empty (`None, None`) — the loop never runs, remainder attach
  links `None`, returns `None`.
- Exactly one list empty — the `tail.next` remainder step links the whole
  non-empty list untouched.
- Disjoint value ranges (e.g. `1 → 2` and `3 → 4`) — one list is consumed
  by comparisons, the other attached as a block; both orders work.
- All values equal — `<=` keeps the merge moving forward and terminates.
- Negative values — comparisons are plain integer order, no special case.
