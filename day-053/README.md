# Day 53 — Number of Islands
**Topic:** Graphs

## Problem

Given an `m x n` 2D binary grid of `'1'`s (land) and `'0'`s (water),
return the number of islands. An island is surrounded by water and is
formed by connecting adjacent lands horizontally or vertically. You may
assume all four edges of the grid are surrounded by water.

## Approach

Scan every cell; when an unvisited land cell is found, flood-fill the
whole island with BFS and count it once. Marking visited cells as `'0'`
in place avoids a separate visited set — each land cell is flipped
exactly once, so every island is counted exactly once. The BFS queue
holds only the current island's frontier.

## Complexity

- Time: O(m * n) — every cell is visited at most once
- Space: O(min(m, n)) — the BFS queue at its widest

## Edge cases

- Empty grid, or a grid with no land — zero islands.
- A single cell of land — one island.
- Land touching only diagonally — separate islands, since only
  horizontal and vertical adjacency counts.
