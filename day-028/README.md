# Day 28 — Reorder List

**Topic:** Linked Lists

## Problem

You are given the head of a singly linked list. Reorder it in place to:

```
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...
```

You may not change the values of the nodes, only their links.

Example: `1 → 2 → 3 → 4` becomes `1 → 4 → 2 → 3`.

## Approach

Three passes, all in place:

1. **Find the middle** with slow/fast pointers — slow lands on the last
   node of the first half.
2. **Reverse the second half** by flipping links one node at a time.
3. **Merge the halves alternately** — take one node from the front half,
   then one from the reversed back half, until the back half runs out.

Splitting the list at the middle before reversing matters: it keeps the
merge loop from chasing its own tail, and the merge naturally stops
because the first half is either the same length as the second or one
node longer.

## Complexity

- Time: O(n) — three linear passes.
- Space: O(1) extra — only a handful of pointers; the reordering itself
  reuses the existing nodes.

## Edge cases

- Empty list or a single node — nothing to reorder.
- Two nodes — already in order, the merge is a no-op.
- Odd length — the middle node stays last in the final order.
- Even length — both halves are equal, the merge consumes every node.
