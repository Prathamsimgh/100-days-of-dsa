# Day 20 — Implement strStr() (KMP)

**Topic:** Strings

## Problem

Given two strings `haystack` and `needle`, return the index of the first
occurrence of `needle` in `haystack`, or -1 if `needle` is not part of
`haystack`. An empty needle returns 0 by convention.

## Approach

Knuth–Morris–Pratt (KMP) instead of the naive O(n·m) scan. First, precompute
the LPS table for `needle`: `lps[i]` is the length of the longest proper
prefix of `needle[:i+1]` that is also a suffix of it. Then scan `haystack`
once, keeping a pointer `j` into `needle`. On a character match both
pointers advance; on a mismatch with `j > 0`, `j` is rewound to `lps[j-1]`
instead of 0 — the already-matched prefix of `needle` is reused, so the
haystack pointer `i` never moves backwards.

## Complexity

- Time: O(n + m) — one pass to build the LPS table (O(m)), one pass to scan (O(n))
- Space: O(m) — the LPS table

## Edge cases

- Empty needle — returns 0 by convention.
- Empty haystack with non-empty needle — no possible match → -1.
- Needle longer than haystack — the scan exhausts `haystack` first → -1.
- Overlapping prefixes — `"aaaaab"` vs `"aaab"` → 2 (the LPS fallback does the work a naive re-scan would repeat).
- Repeated matches — only the *first* occurrence is returned (`"sadbutsad"` vs `"sad"` → 0).
