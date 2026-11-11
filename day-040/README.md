# Day 40 — Invert Binary Tree

**Topic:** Trees & BST

## Problem

Given the root of a binary tree, invert the tree: swap the left and right
subtree of every node, and return the new root.

## Approach

Recursive post-order swap. At each node, invert the left subtree and the
right subtree, then swap them. A `None` root is the base case.

Iterative BFS with a queue works the same way, but recursion keeps the code
short here; the call stack is bounded by the tree height.

## Complexity

- Time: O(n)
- Space: O(h), h = tree height (recursion stack; O(n) for a skewed tree)

## Edge cases

- Empty tree (`None`) — returns `None`.
- Single node — unchanged.
- Skewed tree (all left children) — inversion turns it into an all-right
  tree; the swap still visits every node exactly once.
