# Day 37 — Diameter of Binary Tree

**Topic:** Trees & BST

## Problem

Given the root of a binary tree, return the length of the diameter —
the longest path between any two nodes, measured in edges. The path
may or may not pass through the root.

```
[1, 2, 3, 4, 5] -> 3       (4 -> 2 -> 1 -> 3)
[1, 2, 3, 4, 5, 6, 7] -> 4 (4 -> 2 -> 1 -> 3 -> 7)
[1] -> 0
[] -> 0
```

## Approach

For every node, the diameter passing *through* that node is the sum
of the heights of its left and right subtrees (in edges). The tree's
diameter is the largest such sum over all nodes. A single post-order
walk computes both at once: the recursive `height` helper returns the
height of each subtree to its parent and updates a running best with
`left + right` as it unwinds.

The iterative version does the same thing with an explicit stack:
nodes are pushed with a "visited" flag, so each node is processed
after both children, and heights are recorded in a dict instead of
on the call stack.

## Complexity

- Time: O(n) — every node is visited exactly once.
- Space: O(h) recursive (call stack depth = tree height), O(n)
  iterative (the height map holds every node). For a balanced tree h
  is O(log n); for a skewed tree both degrade to O(n).

## Edge cases

- Empty tree or single node: no edges, diameter 0.
- A straight chain: the diameter is n − 1, the full length of the
  chain — it only passes through the root's child path, not the root.
- A skewed tree makes the recursive version as deep as the node
  count — the iterative version avoids the recursion limit there.
- Diameter is counted in edges, not nodes: a two-node tree has
  diameter 1, not 2.
