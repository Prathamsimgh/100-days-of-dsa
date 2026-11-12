# Day 41 — Symmetric Tree

**Topic:** Trees & BST

## Problem

Given the root of a binary tree, check whether the tree is symmetric
around its centre — i.e. whether it is a mirror image of itself.

## Approach

Recursive mirror check. Two trees are mirrors of each other when their
root values match and the left subtree of one mirrors the right subtree
of the other (and vice versa). Start by comparing the root's left and
right subtrees against each other.

An iterative BFS with a queue of node pairs works the same way, but
recursion keeps the code short here; the call stack is bounded by the
tree height.

## Complexity

- Time: O(n)
- Space: O(h), h = tree height (recursion stack; O(n) for a skewed tree)

## Edge cases

- Empty tree (`None`) — symmetric by definition.
- Single node — symmetric.
- One-sided tree (`[1, 2, 3]`) — not symmetric: the two children differ.
- Same values but different structure (`[1, 2, 2, None, 3, None, 3]`) —
  not symmetric: a missing child has no mirror.
