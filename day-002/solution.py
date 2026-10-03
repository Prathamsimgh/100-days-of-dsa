from typing import List


def max_profit(prices: List[int]) -> int:
    """Return the max profit from one buy-sell transaction.

    One pass: track the lowest price seen so far, and the best profit
    achievable by selling at the current price. O(n) time, O(1) space.
    """
    min_price = float("inf")
    best = 0
    for p in prices:
        if p < min_price:
            min_price = p
        elif p - min_price > best:
            best = p - min_price
    return best


if __name__ == "__main__":
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([1, 2]) == 1
    assert max_profit([]) == 0
    print("all cases passed")
