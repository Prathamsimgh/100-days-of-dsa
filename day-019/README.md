# Day 19 — Valid Palindrome

**Topic:** Strings

## Problem

Given a string, decide whether it is a palindrome after removing all
non-alphanumeric characters and ignoring case. An empty (or purely
punctuation) string counts as a valid palindrome.

## Approach

Two pointers, one at each end, converging inward. The outer loops skip
anything that is not alphanumeric (`str.isalnum()`), and the surviving
characters are compared case-insensitively. The first mismatch rejects;
if the pointers meet or cross, the string reads the same both ways.

## Complexity

- Time: O(n) — each character is visited at most once
- Space: O(1) extra — no cleaned copy of the string is built

## Edge cases

- Empty string / only punctuation — both pointers cross immediately → `True`.
- Single character — trivially a palindrome → `True`.
- Case differences — `"Madam"` → `True` (comparison is lowercased).
- Digits and mixed content — `"ab_a"` → `True`; `"0P"` → `False` (both alphanumerics, `'0' != 'p'`).
- Underscores and other symbols — skipped as non-alphanumeric.
