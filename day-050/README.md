# Day 50 — Task Scheduler

**Topic:** Heaps

## Problem

Given a list of tasks (each labelled with a capital letter) and a
cooldown `n`, return the fewest time intervals needed to run all of
them. Two tasks of the same type must be at least `n` intervals
apart; idle slots are allowed when nothing is eligible to run.

## Approach

Count how often each task occurs and push the counts into a max-heap
(negated, since Python's heap is a min-heap). Then work in cycles of
`n + 1` slots: pop up to `n + 1` tasks, run each once, and push back
any that still have occurrences left. If the heap empties mid-cycle,
the remaining tasks are done and no idle slots are added for that
cycle; otherwise the cycle is padded with idle slots up to `n + 1`.

The idle time is forced by the most frequent task — every other task
fits into its gaps, so the heap only ever needs to track what is left
to schedule, not the exact placement.

## Complexity

- Time: O(n log k) — each task is pushed and popped once, where k is
  the number of distinct task types
- Space: O(k) — the heap holds one entry per distinct task

## Edge cases

- `n = 0` — no cooldown, the answer is just the number of tasks.
- A single task type — the answer is `(count - 1) * (n + 1) + 1`,
  idle slots filling every gap.
- All tasks distinct — no cooldown ever applies, answer is the task
  count regardless of `n`.
- `n` larger than the number of tasks — the last cycle ends early
  with no idle padding.
