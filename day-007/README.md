# Day 7 — Merge Intervals

**Topic:** Arrays

## Problem

Given an array of intervals where `intervals[i] = [start, end]`, merge all
overlapping intervals and return an array of the non-overlapping intervals
that cover the same ranges.

## Approach

Sort by start time, then sweep left to right keeping the interval under
construction. If the next interval starts at or before the current end, it
overlaps — extend the current end to `max(current_end, next_end)`. Otherwise
close the current interval and start a new one.

## Complexity

- Time: O(n log n) — dominated by the sort; the sweep is linear
- Space: O(n) for the output (O(1) extra beyond that)

## Edge cases

- Touching intervals (`[1, 4]`, `[4, 5]`) merge into `[1, 5]` — the
  `<=` comparison makes this inclusive, matching the classic formulation.
- Empty input returns an empty list without touching the sort.
- Input list is not mutated: each interval is copied before merging, so the
  caller's data stays intact.
