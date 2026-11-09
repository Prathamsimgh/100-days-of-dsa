# Day 38 — Validate Binary Search Tree

**Topic:** Trees & BST

## Problem

Given the root of a binary tree, determine whether it is a valid binary
search tree: for every node, all values in its left subtree must be
smaller than the node's value and all values in its right subtree
larger. Values are strictly ordered — duplicates are not allowed.

```
[2, 1, 3] -> true
[5, 1, 4, null, null, 3, 6] -> false   (3 < 5 but sits in the right subtree)
[5, 4, 6, null, null, 3, 7] -> false   (3 < 5 but is a descendant of 6)
[2, 2, 2] -> false                     (duplicates break strict ordering)
[] -> true
```

## Approach

Comparing a node only with its immediate children is not enough: a
value can be on the correct side of its parent yet still violate a
bound set by a higher ancestor. So the recursive walk carries the
allowed (low, high) range down the tree. The root may hold any value;
each left child inherits its parent's value as the new upper bound,
each right child as the new lower bound, and a node outside its range
fails the whole tree at once.

The iterative version uses the other classic BST property instead: an
inorder traversal of a valid BST visits values in strictly increasing
order. An explicit stack walks the tree inorder, remembering only the
previous value, and returns false the moment a value is not larger
than the one before it.

## Complexity

- Time: O(n) — both versions visit each node exactly once and stop
  early on the first violation.
- Space: O(h) recursive (call stack depth = tree height), O(h)
  iterative (the stack holds at most one path down the tree). For a
  balanced tree h is O(log n); for a skewed tree both degrade to O(n).

## Edge cases

- Empty tree or single node: trivially valid.
- Duplicates anywhere fail — the ordering is strict (`low < val <
  high`), so `[2, 2, 2]` is not a BST.
- The subtle failure is a deep violation: a node that is on the right
  side of its parent but the wrong side of a grandparent, e.g. `3`
  under `6` under `5`. The bounds approach catches it; a
  parent-only comparison misses it.
- A left-skewed chain of decreasing values is a valid BST — the
  iterative version handles it without recursion depth worries.
