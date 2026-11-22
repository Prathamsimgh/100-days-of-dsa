# Day 51 — Last Stone Weight

**Topic:** Heaps

## Problem

Given the weights of a pile of stones, repeatedly smash the two
heaviest stones together. If they weigh the same, both are destroyed;
otherwise the lighter one is destroyed and a stone weighing the
difference remains. Repeat until at most one stone is left and return
its weight (0 if none remain).

## Approach

Push all the stones into a max-heap (negated, since Python's heap is
a min-heap). Each round pops the two heaviest stones: equal weights
destroy both, a mismatch pushes back the difference as a new stone.
The heap always holds exactly the stones still in play, so the loop
ends when zero or one stone remains.

## Complexity

- Time: O(n log n) — each stone is pushed and popped at most once per
  smash, and there are at most n smashes
- Space: O(n) — the heap holds the stones

## Edge cases

- A single stone — it is the answer, no smashes happen.
- Two equal stones — both destroyed, answer 0.
- One stone much heavier than the rest — it absorbs the others one by
  one, the answer is the leftover difference.
