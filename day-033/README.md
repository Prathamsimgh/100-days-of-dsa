# Day 33 — Evaluate Reverse Polish Notation

**Topic:** Stacks & Queues

## Problem

Given a list of tokens in Reverse Polish Notation (postfix order),
evaluate the expression and return the result as an integer. Division
truncates toward zero.

```
["2", "1", "+", "3", "*"] -> 9
["4", "13", "5", "/", "+"] -> 6
["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"] -> 22
```

## Approach

Scan the tokens once, keeping a stack of operands. Numbers are pushed
straight on. When an operator appears, pop the top two operands — the
first pop is the right operand, the second is the left — apply the
operator, and push the result back. After the last token, the stack
holds exactly one value: the answer.

## Complexity

- Time: O(n) — each token is pushed and popped at most once.
- Space: O(n) — the stack holds at most one entry per token.

## Edge cases

- Division truncates toward zero, so `-7 / 2` is `-3`, not `-4` —
  Python's `//` would floor, so the solution divides with `/` and
  converts with `int()` instead.
- Operand order matters for `-` and `/`: the first value popped is the
  right operand, the second is the left.
- A single token is just itself — no operator is ever applied.
