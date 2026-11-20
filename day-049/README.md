# Day 49 — K Closest Points to Origin

**Topic:** Heaps

## Problem

Given a list of points on a 2D plane and an integer `k`, return the `k`
points closest to the origin `(0, 0)`. The answer may be in any order;
if two points are equally close, either may be returned.

## Approach

Keep a max-heap of size `k` holding the best candidates seen so far,
keyed by squared distance from the origin. The squared distance is used
instead of the Euclidean distance because taking the square root does not
change the ordering and only adds work. Each point is pushed onto the heap
and, whenever the heap grows past `k`, the farthest point (the heap top) is
evicted — so after one pass only the `k` closest points remain.

Sorting all points by distance would also work, but the heap only ever
holds `k` entries, which is cheaper when `k` is much smaller than `n`.

## Complexity

- Time: O(n log k) — one heap operation per point
- Space: O(k) — the heap never holds more than `k` points

## Edge cases

- `k` equals the number of points — every point is returned.
- The origin itself (`[0, 0]`) — distance zero, always among the closest.
- Ties on distance — either tied point is a valid answer.
- Negative coordinates — squaring handles them; the heap stores the
  original coordinates so the result is unaffected.
