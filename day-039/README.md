# Day 39 — Binary Tree Level Order Traversal

**Topic:** Trees & BST

## Problem

Given the root of a binary tree, return the level order traversal of its
nodes' values — level by level, from left to right within each level.

Example: `[3, 9, 20, null, null, 15, 7]` →
`[[3], [9, 20], [15, 7]]`.

## Approach

Breadth-first search with a queue. The queue holds the current frontier;
before processing a level, snapshot the queue's length — that count is
exactly the number of nodes on this level. Pop that many nodes, record
their values, and enqueue their children. Repeat until the queue is empty.

A plain recursive DFS could also group by depth, but BFS gives the levels
naturally without an extra depth parameter.

## Complexity

- Time: O(n) — each node is enqueued and dequeued once.
- Space: O(w) — the queue holds at most the widest level (O(n) worst case
  for a complete tree, O(1) for a chain).

## Edge cases

- Empty tree (`root is None`) — return `[]`, not `[[]]`.
- Single node — `[[1]]`.
- Skewed tree (only right children) — one node per level, still correct.
