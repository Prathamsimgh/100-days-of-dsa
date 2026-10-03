# Day 2 — Best Time to Buy and Sell Stock

**Topic:** Arrays

## Problem

Given an array `prices` where `prices[i]` is the price on day `i`, choose a
single day to buy and a later day to sell to maximize profit. Return the
maximum profit; return 0 if no profit is possible.

## Approach

Single pass, greedy. Keep the minimum price seen so far; for each day, the
best profit ending that day is `price - min_price`. Track the max over all
days. Buy-then-sell order is enforced because `min_price` only looks
backwards.

A brute-force O(n²) check of every buy/sell pair also works, but the running
minimum collapses it to a single pass with constant extra space.

## Complexity

- Time: O(n)
- Space: O(1)

## Edge cases

- Strictly decreasing prices — no profitable trade, answer stays 0.
- Empty or single-day input — no transaction possible, return 0.
