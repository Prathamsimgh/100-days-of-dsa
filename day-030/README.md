# Day 30 — Valid Parentheses

**Topic:** Stacks & Queues

## Problem

Given a string containing only `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`,
determine whether the brackets are balanced: every opening bracket is
closed by the same type of bracket, in the correct nesting order.

```
"()[]{}"  -> True
"(]"      -> False
"([)]"    -> False
"{[]}"    -> True
```

## Approach

Scan left to right with a stack. Push every opening bracket; on a closing
bracket, pop the top of the stack and check it is the matching opener.
A mismatch, or a closing bracket with an empty stack, means the string is
invalid. After the scan, the string is valid only if the stack is empty
(no unmatched openers left over).

## Complexity

- Time: O(n) — one pass over the string, each bracket pushed and popped once.
- Space: O(n) — the stack holds at most all the opening brackets.

## Edge cases

- Empty string: valid (nothing to match).
- Single bracket, e.g. `"("` or `")"`: invalid.
- Interleaved types, e.g. `"([)]"`: invalid — the stack catches the
  nesting violation even though the counts balance.
- Closing bracket before any opener, e.g. `")("`: invalid on the first
  character.
