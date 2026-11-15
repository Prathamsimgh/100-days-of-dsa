# Day 44 — Binary Tree Right Side View

**Topic:** Trees & BST

## Problem

Given the root of a binary tree, return the values of the nodes visible
when the tree is viewed from the right side, ordered top to bottom.

## Approach

Level-order traversal (BFS) with a queue. For each level, record the last
node dequeued — that is the rightmost node of the level, which is exactly
what is visible from the right.

## Complexity

- Time: O(n) — every node is visited once
- Space: O(w) — the queue holds at most the widest level

## Edge cases

- Empty tree — returns `[]`.
- A left-leaning chain (`[1, 2, 3, 4]`) — every level has one node, so the
  whole chain is visible: `[1, 2, 3, 4]`.
