# Day 32 — Daily Temperatures

**Topic:** Stacks & Queues

## Problem

Given a list of daily temperatures, return for each day how many days you
have to wait until a warmer temperature. If there is no future warmer
day, the answer for that day is 0.

```
[73, 74, 75, 71, 69, 72, 76, 73] -> [1, 1, 4, 2, 1, 1, 0, 0]
```

## Approach

Walk the temperatures once, keeping a stack of indices whose warmer day
hasn't been seen yet. The stack is kept in strictly decreasing
temperature order: whenever the current temperature is warmer than the
temperature at the top of the stack, it resolves that day's wait (the
distance between the two indices), and we keep popping while the stack
top is still cooler. Then the current day goes on the stack, waiting for
its own warmer day. Days left on the stack at the end never see a warmer
day, so their answers stay 0.

## Complexity

- Time: O(n) — each index is pushed and popped at most once.
- Space: O(n) — the stack holds at most one index per day.

## Edge cases

- Equal temperatures are not warmer, so the pop condition is strict
  (`<`), not `<=` — `[70, 70, 70, 71]` gives `[3, 2, 1, 0]`.
- Strictly decreasing input leaves the whole stack unresolved: all zeros.
- Empty input returns an empty list; a single day always returns `[0]`.
