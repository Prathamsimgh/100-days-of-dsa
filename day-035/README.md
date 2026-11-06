# Day 35 — Maximum Depth of Binary Tree

**Topic:** Trees & BST

## Problem

Given the root of a binary tree, return its maximum depth — the number of
nodes along the longest path from the root down to the farthest leaf.

```
[3, 9, 20, null, null, 15, 7] -> 3
[1, null, 2] -> 2
[] -> 0
```

## Approach

Depth is defined recursively: an empty tree has depth 0, and any other
tree is 1 (the root) plus the deeper of its two subtrees. The recursive
solution is a direct translation of that definition. The iterative
version does the same work level by level with a queue — one pass per
level, counting levels until the queue drains — which avoids recursion
depth limits on degenerate trees.

## Complexity

- Time: O(n) — every node is visited exactly once.
- Space: O(h) recursive (call stack depth = tree height), O(w)
  iterative (queue holds one level, w = max width). For a balanced tree
  h is O(log n); for a skewed tree both degrade to O(n).

## Edge cases

- An empty tree (`None` root) has depth 0, not 1.
- A single node has depth 1.
- A skewed tree (every node has one child) has depth equal to its node
  count — the recursive version can hit Python's recursion limit on a
  very deep tree, which is when the iterative version earns its keep.
- Depth counts nodes, not edges: a root with one leaf child is depth 2.
