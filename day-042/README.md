# Day 42 — Kth Smallest Element in a BST

**Topic:** Trees & BST

## Problem

Given the root of a binary search tree and an integer `k`, return the kth
smallest value (1-indexed) in the tree.

## Approach

Inorder traversal of a BST visits nodes in sorted order, so the kth node
visited is the answer. Walk down left with an explicit stack, pop, count
down, then move right — and stop as soon as the counter hits zero instead
of traversing the rest of the tree.

A recursive inorder does the same thing in fewer lines, but the iterative
version makes the early exit obvious and avoids recursion depth limits on
a skewed tree.

## Complexity

- Time: O(h + k), where h is the tree height — O(n) worst case on a skewed tree
- Space: O(h) for the explicit stack

## Edge cases

- `k = 1` — the leftmost node, the tree minimum.
- `k` equal to the node count — the rightmost node, the tree maximum.
- `k` larger than the node count — no such element; raise an error instead
  of returning a made-up value.
