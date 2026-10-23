# Day 22 — Linked List Cycle

**Topic:** Linked Lists

## Problem

Given the head of a singly-linked list, determine whether the list contains a
cycle — i.e. some node's `next` pointer points back to an earlier node so the
list never terminates.

Example: `1 → 2 → 3 → 4 → 2` (the `4` points back at the `2`) has a cycle;
`1 → 2 → 3 → 4` does not.

## Approach

Floyd's tortoise-and-hare. Two pointers start at the head: `slow` advances
one node per step, `fast` advances two. If the fast pointer reaches `None`,
there is no cycle. If the two pointers ever land on the same node, a cycle
must exist — the fast pointer laps the slow one inside the loop.

The alternative is a hash set of visited nodes, which is simpler but uses
O(n) extra space. Floyd's keeps the pointer-chasing style that the
linked-list section favours and costs nothing beyond the two pointers.

## Complexity

- Time: O(n) — the fast pointer visits each node at most twice before either
  meeting the slow pointer or leaving the list.
- Space: O(1)

## Edge cases

- Empty list (`None`) — the loop condition fails immediately, returns `False`.
- Single node without a cycle — `fast.next` is `None`, returns `False`.
- Single node pointing at itself — `slow is fast` on the first step, returns
  `True`. (Note `fast.next.next` is safe here because the loop checks
  `fast.next is not None` first.)
