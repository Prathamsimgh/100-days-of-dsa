# Day 21 — Reverse Linked List

**Topic:** Linked Lists

## Problem

Given the head of a singly-linked list, reverse the list and return the new
head.

Example: `1 → 2 → 3 → 4 → 5` becomes `5 → 4 → 3 → 2 → 1`.

## Approach

Iterative three-pointer reversal. Walk the list with `prev` trailing the
current node: save `curr.next`, point `curr.next` back at `prev`, then
advance both pointers. When `curr` runs off the end, `prev` is the new head.

Recursion gives the same O(n) time with a cleaner expression, but the
iterative version keeps space at O(1) — relevant on long lists where a
recursive call stack could blow the limit.

## Complexity

- Time: O(n)
- Space: O(1)

## Edge cases

- Empty list (`None`) — the loop never runs, returns `None`.
- Single node — its `next` (already `None`) just gets pointed at the
  previous `None`, so the node is returned as-is.
