# Day 18 — Longest Common Prefix

**Topic:** Strings

## Problem

Given a list of strings, return the longest string that is a prefix of
every one of them. Return `""` if there is no common prefix (or the list
is empty).

## Approach

Vertical scan. Take the first string as the reference and walk it
character by character; at each index, check the same index in every
other string. The moment any string is shorter than the current index or
disagrees at that character, the prefix ends there — everything before
it is common to all strings.

## Complexity

- Time: O(S) — S = total characters across all strings; each character is compared at most once
- Space: O(1) extra — the result slice is output

## Edge cases

- Empty list — returns `""` (no reference string to scan).
- A string is itself empty — the first column comparison ends immediately → `""`.
- One string is a strict prefix of the others — e.g. `["ab", "abcd"]` → `"ab"`.
- All strings identical — the whole first string is the prefix.
