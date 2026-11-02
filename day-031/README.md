# Day 31 — Min Stack

**Topic:** Stacks & Queues

## Problem

Design a stack that supports `push`, `pop`, `top`, and retrieving the
minimum element, all in constant time.

```
push(-2), push(0), push(-3), get_min() -> -3
pop()    -> -3
top()    -> 0
get_min() -> -2
```

## Approach

Keep two stacks side by side: the main stack and an auxiliary min stack.
On every push, also push onto the min stack if the new value is less than
or equal to the current minimum (the `<=` matters for duplicate minima).
On pop, pop from the min stack too whenever the popped value equals the
current minimum. Then the top of the min stack is always the minimum of
everything still in the main stack — no scan needed.

## Complexity

- Time: O(1) — push, pop, top, and get_min are all single stack operations.
- Space: O(n) — the min stack holds at most one entry per push (fewer in
  practice, since only new minima are recorded).

## Edge cases

- Duplicate minima, e.g. pushing `5, 5`: popping one `5` must leave
  `get_min()` at `5`, which is why duplicates are pushed with `<=`, not `<`.
- Strictly increasing pushes: the min stack holds just the first element.
- `pop`, `top`, and `get_min` on an empty stack raise `IndexError` —
  callers are expected to check the stack is non-empty first.
