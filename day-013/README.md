# Day 13 — Longest Palindromic Substring

**Topic:** Strings

## Problem

Given a string `s`, return the longest substring of `s` that is a palindrome.

## Approach

Expand around center. Every palindrome has a center: either a single
character (odd length) or the gap between two characters (even length).
Try all `2n - 1` centers, expand each outward while the ends match, and
keep the longest span found.

The DP variant (`O(n²)` space) works but is wasteful — the expansion
approach only needs the current best window.

## Complexity

- Time: O(n²)
- Space: O(1)

## Edge cases

- Empty string returns `""`.
- All-same-character strings (`"aaaa"`) — both centers work, handled by
  `max(span(i, i), span(i, i + 1))`.
- Single character or two different characters return one of the
  length-1 options.
- Multiple correct answers (e.g. `"babad"` → `"bab"` or `"aba"`) —
  either is accepted.
