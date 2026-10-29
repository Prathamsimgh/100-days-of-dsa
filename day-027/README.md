# Day 27 — Add Two Numbers

**Topic:** Linked Lists

## Problem

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each node contains
a single digit. Add the two numbers and return the sum as a linked list
in the same format.

Example: `2 → 4 → 3` (342) + `5 → 6 → 4` (465) = `7 → 0 → 8` (807).

## Approach

Because the digits arrive least-significant first, the lists can be
walked together in a single pass, exactly like column addition on
paper. At each step the two digits plus the carry from the previous
step are summed; the digit written is `total % 10` and the carry passed
on is `total // 10`.

A dummy head node keeps the loop uniform — no special case for the
first result node. The loop continues while either list still has nodes
or a carry remains, so a trailing carry (e.g. `999 + 1 = 1000`) appends
one final node instead of being dropped.

This beats converting both lists to integers (unbounded size, O(n)
extra space for the digits) and the recursive approach (O(n) stack
depth) with a single pass and no extra storage.

## Complexity

- Time: O(max(m, n)) — one pass over the longer list.
- Space: O(1) extra — only pointers and the carry; the output list
  itself is excluded.

## Edge cases

- Unequal lengths — the exhausted list contributes zero from then on.
- Carry rippling through the whole longer list (`999 + 1 → 1000`).
- Final carry creating a new most-significant digit (`5 + 5 → 10`).
- One list empty — adding zero leaves the other list unchanged.
- Both lists empty — no digits and no carry, so the result is empty.
