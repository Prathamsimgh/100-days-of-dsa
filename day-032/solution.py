"""Daily Temperatures.

Given daily temperatures, return for each day how many days you have to
wait until a warmer temperature. If there is no future warmer day, the
answer for that day is 0.
"""


def daily_temperatures(temperatures: list[int]) -> list[int]:
    """Monotonic decreasing stack of indices awaiting a warmer day."""
    n = len(temperatures)
    answer = [0] * n
    stack: list[int] = []  # indices with strictly decreasing temperatures
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer


if __name__ == "__main__":
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
        1, 1, 4, 2, 1, 1, 0, 0
    ]
    # No warmer day anywhere: all zeros.
    assert daily_temperatures([90, 80, 70, 60]) == [0, 0, 0, 0]
    # Strictly increasing: every day waits exactly one day.
    assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    # Equal temperatures are not warmer, so they never resolve a wait.
    assert daily_temperatures([70, 70, 70, 71]) == [3, 2, 1, 0]
    # Single day and empty input.
    assert daily_temperatures([55]) == [0]
    assert daily_temperatures([]) == []
    print("all tests passed")
