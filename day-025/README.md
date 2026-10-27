# Day 25 — Intersection of Two Linked Lists

**Topic:** Linked Lists

## Problem

Given the heads of two singly-linked lists, return the node at which
they intersect — the first node shared by both lists. If the lists do
not intersect, return `None`. The intersection is defined by reference,
not by value: two nodes with the same value are not an intersection
unless they are the same object.

Example: `4 → 1 → 8 → 4 → 5` and `5 → 6 → 1 → 8 → 4 → 5` intersect at
the node with value `8`.

## Approach

Two pointers, one per list, walking in lockstep. When a pointer reaches
the end of its list it jumps to the head of the other list. After the
jump, each pointer covers the other list's prefix, so both end up
travelling `len(A) + len(B)` steps before the intersection — the length
difference cancels out, and they arrive at the shared node together. If
there is no intersection, both pointers fall off the end at the same
time and meet at `None`.

This avoids the length-counting alternative (measure both lists, skip
the difference, then walk together) with no extra pass and no hash set
of visited nodes.

## Complexity

- Time: O(m + n) — each pointer visits at most both lists once.
- Space: O(1) — only the two pointers.

## Edge cases

- No intersection — both pointers reach `None` together; returns `None`.
- Intersection at the head — the lists are the same object from the
  start; the loop never runs and the head is returned.
- One or both lists empty — the pointer starting at `None` jumps once
  and the two meet at `None`.
- Same values, different nodes — identity comparison (`is`) means
  equal values before the true intersection never match.
- Intersection at the last node only — the pointers still align after
  the switch and meet on that single shared node.
