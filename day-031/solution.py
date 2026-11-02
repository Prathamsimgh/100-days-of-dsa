"""Min Stack.

Design a stack that supports push, pop, top, and retrieving the minimum
element, all in constant time.
"""


class MinStack:
    """Stack with O(1) get_min, backed by an auxiliary min stack."""

    def __init__(self) -> None:
        self._stack: list[int] = []
        self._mins: list[int] = []

    def push(self, val: int) -> None:
        """Push val, tracking the new minimum if val is at most the old one."""
        self._stack.append(val)
        if not self._mins or val <= self._mins[-1]:
            self._mins.append(val)

    def pop(self) -> int:
        """Remove and return the top element."""
        val = self._stack.pop()
        if val == self._mins[-1]:
            self._mins.pop()
        return val

    def top(self) -> int:
        """Return the top element without removing it."""
        return self._stack[-1]

    def get_min(self) -> int:
        """Return the minimum element in the stack."""
        return self._mins[-1]

    def __len__(self) -> int:
        return len(self._stack)


if __name__ == "__main__":
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    assert s.get_min() == -3
    assert s.pop() == -3
    assert s.top() == 0
    assert s.get_min() == -2

    # Duplicate minima: popping one copy must not lose the other.
    s2 = MinStack()
    s2.push(5)
    s2.push(5)
    s2.push(3)
    assert s2.get_min() == 3
    s2.pop()
    assert s2.get_min() == 5
    s2.pop()
    assert s2.get_min() == 5
    assert len(s2) == 1

    # Increasing sequence: the minimum stays the first element.
    s3 = MinStack()
    for v in (1, 2, 3, 4):
        s3.push(v)
    assert s3.get_min() == 1
    assert s3.top() == 4
    print("all tests passed")
