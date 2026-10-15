# Day 14 — Valid Anagram

**Topic:** Strings

## Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`,
and `false` otherwise. An anagram uses the exact same characters with the
same frequencies.

## Approach

If the lengths differ, they can't be anagrams — early exit. Otherwise build
character frequency maps for both strings and compare them. `collections.Counter`
does this in one pass each.

The alternative — sorting both strings and comparing — costs O(n log n);
the frequency map keeps it linear.

## Complexity

- Time: O(n)
- Space: O(1) for a bounded alphabet (26 lowercase letters here)

## Edge cases

- Empty strings (`""`, `""`) — vacuously anagrams, returns true.
- Different lengths (`"a"`, `"ab"`) — caught by the early exit, no
  needless work.
- Repeated characters (`"aabb"`, `"abab"`) — frequencies must match, not
  just the character set.
