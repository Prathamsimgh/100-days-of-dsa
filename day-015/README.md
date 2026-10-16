# Day 15 — Longest Substring Without Repeating Characters

**Topic:** Strings

## Problem

Given a string `s`, find the length of the longest substring that contains
no repeating characters.

## Approach

Sliding window with a hash map from character to its most recent index.
The left edge of the window never moves backward: when the current char
was seen at index `i` inside the window (`i >= left`), jump `left` to
`i + 1`. Update the best length at every step.

The naive O(n²) check of every substring is replaced by the single-pass
window since each character is visited at most twice.

## Complexity

- Time: O(n)
- Space: O(min(n, m)) for the map, where m is the alphabet size

## Edge cases

- Empty string — returns 0; the loop simply never runs.
- All duplicates (`"bbbbb"`) — left chases right, best stays 1.
- Duplicate outside the window (`"dvdf"`) — `"d"` at index 2 is behind
  `left` after the first jump, so the map entry is stale and correctly
  ignored by the `last_seen[ch] >= left` guard.
