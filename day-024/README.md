# Day 24 — Remove Nth Node From End of List

**Topic:** Linked Lists

## Problem

Given the head of a singly-linked list, remove the nth node from the end
of the list and return its head. `n` is guaranteed valid (1 <= n <=
list length).

Example: `1 → 2 → 3 → 4 → 5` with `n = 2` becomes `1 → 2 → 3 → 5`.

## Approach

Two-pointer gap method. Start both pointers at a dummy head pointing at
the list, then advance the fast pointer `n + 1` steps so it sits exactly
`n` nodes ahead of the slow pointer. Walk both forward together; when
the fast pointer falls off the end, the slow pointer is on the node just
before the one to remove, so one re-link (`slow.next = slow.next.next`)
drops it.

The dummy head is what makes this clean: removing the first node is the
same operation as removing any other, because the slow pointer can sit
on the dummy instead of needing a separate head-update branch. The
two-pointer trick avoids a first pass to count the length, so the list
is traversed exactly once.

## Complexity

- Time: O(n) — a single pass; the gap setup and the joint walk together
  visit each node at most once.
- Space: O(1) — only the dummy node and two pointers.

## Edge cases

- Removing the head (`n` == length) — the slow pointer stays on the
  dummy, and the re-link drops the original head; `dummy.next` is the
  new head.
- Removing the tail (`n` == 1) — the slow pointer lands on the second
  last node, and its `next` becomes `None`.
- Single-node list (`n` == 1) — the re-link empties the list; returns
  `None`.
- Two-node list, either end — both directions covered by the same
  re-link, no special cases.
