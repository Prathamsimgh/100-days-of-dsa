# Day 8 — 3Sum

**Topic:** Arrays

## Problem

Given an integer array `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]`
such that `i != j`, `i != k`, `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

The output must not contain duplicate triplets. Order of triplets and of
elements inside each triplet does not matter.

## Approach

Sort the array first, then fix one index and run a two-pointer scan on the
rest — the same idea as Day 1's complement trick, extended one dimension.

For each `i`, put `left` at `i + 1` and `right` at the end. If the sum is
below zero move `left` up, above zero move `right` down, and on zero record
the triplet and advance both. Skipping equal neighbours at all three
positions (`nums[i]`, then both pointers after each hit) guarantees unique
triplets without a dedup set.

The brute-force O(n³) triple loop is infeasible beyond tiny inputs; sorting
plus two pointers brings it down to quadratic.

## Complexity

- Time: O(n²) — the sort is O(n log n), the double loop dominates.
- Space: O(1) extra (not counting the output list).

## Edge cases

- Fewer than three elements, e.g. `[0, 1, 1]` — the loop bounds mean no
  triplet is ever attempted; returns `[]`.
- All zeros (`[0, 0, 0]`) — returns a single `[0, 0, 0]`, not three copies;
  the skip logic collapses them.
- Entire array positive or negative — no sum can reach zero; pointers cross
  immediately each iteration.
