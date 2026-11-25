# Day 54 — Rotting Oranges
**Topic:** Graphs

## Problem

You are given an `m x n` grid where each cell is `0` (empty), `1`
(fresh orange) or `2` (rotten orange). Every minute, any fresh orange
that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes until no cell has a fresh orange,
or `-1` if this is impossible.

## Approach

Multi-source BFS: seed the queue with every rotten orange at once and
expand layer by layer, one layer per minute. Counting the fresh oranges
up front means the end state is a single comparison — if any fresh
orange is left after the queue drains, it was never reachable and the
answer is `-1`. Rotten cells are marked in place, so no visited set is
needed.

## Complexity

- Time: O(m * n) — every cell is enqueued at most once
- Space: O(m * n) — the queue in the worst case

## Edge cases

- No fresh oranges at all — zero minutes.
- A fresh orange with no rotten neighbour anywhere — `-1`.
- Empty grid — zero minutes.
