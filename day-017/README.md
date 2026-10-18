# Day 17 — Minimum Window Substring

**Topic:** Strings

## Problem

Given strings `s` and `t`, return the smallest substring of `s` that
contains every character of `t` (with the same multiplicities — `"aab"`
needs two a's). Return `""` if no such window exists.

## Approach

Sliding window. Expand the right edge until the window covers all of `t`,
then shrink the left edge as far as possible while the window still covers
`t`, recording the best window each time. A `formed` counter tracks how
many distinct characters have hit their required count, so the check for
"window is valid" is O(1) and each pointer moves at most n steps.

## Complexity

- Time: O(n) — n = length of `s`; each end of the window moves at most n times
- Space: O(m) — m = distinct characters in `t` (the `need`/`window` maps)

## Edge cases

- `t` longer than `s`, or a needed character missing from `s` — returns `""`.
- Duplicate characters in `t` — counts must match, not just presence
  (`"aaab"` / `"aab"` → `"aab"`, not `"ab"`).
- Empty `s` or empty `t` — returns `""` (nothing to cover / nothing needed).
- Whole string is the only window — e.g. `"abc"` / `"cba"`.
