# Day 43 — Serialize and Deserialize Binary Tree

**Topic:** Trees & BST

## Problem

Design an algorithm to serialize a binary tree to a single string and
deserialize that string back into the original tree. There is no restriction
on how the serialization format looks, as long as it round-trips exactly.

## Approach

Preorder traversal, writing `#` for every null child. The marker is what
makes the format unambiguous: with it, each node's value is followed by
exactly its left subtree then its right subtree, so a recursive rebuild
consuming tokens in order reproduces the original shape. Serializing is a
straight preorder walk; deserializing pops the next token and recurses —
`#` returns `None`, otherwise a new node is built and its children are
filled from the following tokens.

A level-order (BFS) encoding works too, but preorder needs no queue and
rebuilds the tree in one pass.

## Complexity

- Time: O(n) — serialize visits every node once, deserialize consumes every token once
- Space: O(n) — the serialized string, plus O(h) recursion depth

## Edge cases

- Empty tree — serializes to just `#` and deserializes back to `None`.
- Single node — `7,#,#`; the two markers stop the rebuild at the leaves.
- Skewed tree — a left-only chain still round-trips; recursion depth is O(n) there, so very deep trees could hit Python's recursion limit.
- Negative values — tokens are parsed with `int()`, so `-3` survives the round-trip.
