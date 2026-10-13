# Day 12 — Set Matrix Zeroes

**Topic:** Arrays

## Problem

Given an `m x n` integer matrix, if an element is `0`, set its entire row
and column to `0`. Do it in place.

## Approach

Two passes over the matrix. First pass records which rows and columns
contain at least one zero (two hash sets). Second pass rewrites every
cell whose row or column is marked.

The follow-up constant-space trick reuses the first row and first column
as the marker storage (with two booleans to remember whether the first
row/column themselves were zeroed); the sets version above is the clearer
base solution.

## Complexity

- Time: O(m * n)
- Space: O(m + n)

## Edge cases

- A `1 x n` or `m x 1` matrix — the second pass handles it with no special
  casing.
- Zero in the first row or column — no overlap problem since marking and
  rewriting are separate passes.
- Empty matrix — guarded up front.
