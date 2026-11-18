# Day 47 — Merge K Sorted Lists

**Topic:** Heaps

## Problem

You are given an array of `k` linked lists, each sorted in ascending order.
Merge all the lists into one sorted linked list and return its head.

## Approach

Min-heap merge. Push the head of every non-empty list into a heap keyed by
node value, then repeatedly pop the smallest node, append it to the result,
and push that node's successor. Each list contributes its nodes in order, so
the popped sequence is globally sorted.

The list index is stored alongside the value in each heap entry so that
equal values never force a comparison between `ListNode` objects.

A divide-and-conquer pairwise merge also works in the same O(N log k) time,
but the heap version is a single pass and easier to get right.

## Complexity

- Time: O(N log k) — N total nodes, each pushed and popped once from a heap of size at most k
- Space: O(k) — the heap holds at most one node per list (output excluded)

## Edge cases

- No lists at all (`[]`) or all lists empty — return `None`.
- A single list — returned unchanged, no extra work.
- Duplicate values across lists — handled by the index tie-breaker in the heap entries.
