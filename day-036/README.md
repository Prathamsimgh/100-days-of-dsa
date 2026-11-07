# Day 36 — Lowest Common Ancestor of a Binary Tree

**Topic:** Trees & BST

## Problem

Given a binary tree, find the lowest common ancestor (LCA) of two given
nodes `p` and `q`. The LCA is the deepest node that has both `p` and `q`
as descendants — a node counts as a descendant of itself.

```
[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1 -> 3
[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 4 -> 5
[1, 2], p = 1, q = 2 -> 1
```

## Approach

Walk the tree recursively. If the current node is `None`, or is `p` or
`q` itself, return it — that is the answer for this subtree. Otherwise
recurse into both children: if both sides return a node, `p` and `q`
split at this node, so it is the LCA; if only one side returns a node,
that side's answer bubbles up. The iterative version does the same job
without recursion: record every node's parent with a stack walk, collect
`p`'s ancestors in a set, then climb from `q` until the paths meet.

## Complexity

- Time: O(n) — every node is visited exactly once.
- Space: O(h) recursive (call stack depth = tree height), O(n)
  iterative (the parent map holds every node). For a balanced tree h
  is O(log n); for a skewed tree both degrade to O(n).

## Edge cases

- `p` is an ancestor of `q` (or vice versa): the ancestor itself is
  the LCA.
- `p` and `q` are the same node: that node is the LCA.
- A two-node tree: the root is the LCA of itself and its child.
- A skewed tree (every node has one child) makes the recursive version
  as deep as the node count — the parent-map version avoids the
  recursion limit there.
