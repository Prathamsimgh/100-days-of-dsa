# Day 5 — Product of Array Except Self

**Topic:** Arrays

## Problem

Given an integer array `nums`, return an array `answer` such that
`answer[i]` equals the product of all elements of `nums` except `nums[i]`.
You must not use division, and the algorithm should run in O(n) time.

## Approach

Two linear passes, folding both products into the output array itself.
Left-to-right pass: `answer[i]` gets the product of everything to the
left of `i` (the prefix product). Right-to-left pass: multiply in the
product of everything to the right of `i` (the suffix product).

Because the answer array holds the prefixes first, no extra arrays are
needed — only the output itself plus two running scalars.

The naive approach recomputes the product per index (O(n²)); the
prefix/suffix trick shares the overlapping work.

## Complexity

- Time: O(n) — two passes over the array
- Space: O(1) extra (not counting the output array)

## Edge cases

- Zeroes: with two or more zeroes every entry is 0; with exactly one zero
  at index `i`, only `answer[i]` is non-zero. The prefix/suffix passes
  handle this naturally — no special casing needed.
- Single element: `answer[0] = 1` (product of nothing), since both running
  products start at 1.
- Negative numbers: sign flips are absorbed by the multiplications; the
  parity of negatives decides each entry's sign correctly.
