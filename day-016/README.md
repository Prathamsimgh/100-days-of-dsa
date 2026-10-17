# Day 16 — Group Anagrams

**Topic:** Strings

## Problem

Given an array of strings `strs`, group all anagrams together. Return the
groups in any order. An anagram is a word formed by rearranging the letters
of another word.

## Approach

Anagrams have identical character counts, so each word maps to a canonical
signature: a 26-length tuple of lowercase letter frequencies. A hash map
from signature to word list groups them in one pass — no sorting needed.

Using the count tuple as the key is O(k) per word (k = word length),
cheaper than the O(k log k) sorted-string alternative for long words.

## Complexity

- Time: O(n·k) — n words, each hashed in O(k)
- Space: O(n·k) for the map entries

## Edge cases

- Empty string `""` — counts tuple is all zeros, groups on its own.
- Empty input — returns `[]`; no groups created.
- Single word or no anagrams — every word gets its own group.
- Group order is arbitrary — tests normalize before comparing.
