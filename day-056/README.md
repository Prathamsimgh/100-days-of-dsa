# Day 56 — Course Schedule

**Topic:** Graphs

## Problem

There are `numCourses` courses labelled `0` to `numCourses - 1`. Each
prerequisite pair `[a, b]` means course `b` must be completed before
course `a`. Determine whether it is possible to finish all courses,
and if so, return one valid order to take them in.

## Approach

Model the prerequisites as a directed graph: an edge `b -> a` for each
pair `[a, b]`. A valid schedule exists exactly when the graph has no
cycle, which is a topological sort problem.

Kahn's algorithm: count each course's in-degree (number of unmet
prerequisites), start with all courses at in-degree 0, and repeatedly
take one, decrementing the in-degree of everything it unlocks. Courses
reaching in-degree 0 join the queue. If every course is taken, the
recorded order is valid; if some remain, they sit in a cycle and no
schedule exists. `find_order` is the same pass with the order recorded.

## Complexity

- **Time:** O(V + E) — each course and prerequisite is processed once.
- **Space:** O(V + E) — the adjacency list plus the in-degree array.

## Edge cases

- No prerequisites: any order works, in-degree 0 for all.
- A self-loop (`[0, 0]`) is a cycle of one — impossible.
- A cycle hidden among otherwise finishable courses still blocks the
  whole schedule — the count check catches it.
- An empty result from `find_order` means "no valid order" (also the
  result for zero courses), so pair it with `can_finish` when that
  distinction matters.
