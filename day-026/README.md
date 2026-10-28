# Day 26 — Palindrome Linked List

**Topic:** Linked Lists

## Problem

Given the head of a singly-linked list, return `True` if the list is a
palindrome — the values read the same forwards and backwards — and
`False` otherwise.

Example: `1 → 2 → 2 → 1` is a palindrome; `1 → 2 → 3` is not.

## Approach

Fast and slow pointers find the middle of the list in one pass: the
fast pointer moves two nodes per step, so when it reaches the end the
slow pointer sits at the middle. For an odd-length list the middle node
is skipped, since it never needs comparing with anything.

The second half is then reversed in place and compared node by node
with the first half. Reversing back at the end restores the caller's
list, so the check has no observable side effects.

This beats the copy-to-array alternative (O(n) extra space) and the
recursive approach (O(n) stack depth) with no extra storage beyond a
few pointers.

## Complexity

- Time: O(n) — one pass to find the middle, one to reverse, one to compare.
- Space: O(1) — only pointers; the reversal is in place.

## Edge cases

- Empty list and single node — trivially palindromes.
- Two nodes — palindrome only when both values match.
- Odd length — the middle node is skipped, not compared.
- Equal values that are not symmetric (`1 → 2 → 1 → 2`) — the
  pairwise comparison catches the mismatch.
- The input list is restored after the check — values and order are
  unchanged for the caller.
