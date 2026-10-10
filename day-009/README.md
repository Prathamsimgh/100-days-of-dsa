# Trapping Rain Water

Given `n` non-negative integers representing an elevation map where the
width of each bar is 1, compute how much water it can trap after raining.

Example: `[0,1,0,2,1,0,1,3,2,1,2,1]` traps 6 units.

## Approach

Two pointers starting at both ends, tracking the tallest bar seen so far
from each side. Move the pointer on the side with the smaller height: the
water trapped at that index is bounded by `min(left_max, right_max)`, and
the smaller side's max is always the limiting one — so the amount is fully
determined. No prefix/suffix arrays needed.

## Complexity

- Time: O(n)
- Space: O(1)

## Edge cases

- Empty array or a single bar → 0 water
- Strictly increasing or decreasing heights → 0 water
- A single dip between two tall bars → filled up to the lower bar
