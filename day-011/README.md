# Day 11 — Sort Colors

**Problem:** Given an array `nums` with `n` objects colored red (0), white
(1) and blue (2), sort them in-place so that objects of the same color are
adjacent, in the order red, white, blue.

**Approach — Dutch National Flag (3-way partition):** maintain three
pointers. `[0..low)` holds 0s, `[low..mid)` holds 1s, `[mid..high]` is
unprocessed, `(high..n)` holds 2s. Walk `mid` forward: swap a 0 to `low`,
skip 1s, swap a 2 to `high` and shrink the unprocessed tail. Each element is
examined once and every swap places at least one element in its final
region.

**Complexity:** O(n) time, O(1) extra space.

**Edge cases:**
- Empty array and single-element arrays need no work.
- Already sorted input is handled without extra swaps on the 1s region.
- Arrays of all one color exercise each branch independently.
