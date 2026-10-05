# Day 4 — Container With Most Water

**Topic:** Arrays

## Problem

Given an integer array `height` of length `n`, where each element is the
height of a vertical line at that index, find the two lines that together
with the x-axis form a container holding the most water. Return the area.

## Approach

Two pointers starting at opposite ends. The area between `l` and `r` is
`min(height[l], height[r]) * (r - l)`. The shorter line limits the area, so
move the shorter pointer inward — only a taller line on that side can
possibly improve the answer. Each step discards one side, so every pair
that could be optimal is considered exactly once.

## Complexity

- Time: O(n)
- Space: O(1)

## Edge cases

- Descending heights (`[4, 3, 2, 1, 4]`) — pointers still sweep every
  candidate pair; max area 16 comes from the two `4`s.
- Minimum input (`[1, 1]`) — loop runs once, area 1.
