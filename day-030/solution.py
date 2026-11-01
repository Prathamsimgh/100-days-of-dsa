"""Valid Parentheses.

Given a string containing only '(', ')', '{', '}', '[' and ']', determine
whether the brackets are balanced: every opening bracket is closed by the
same type of bracket, in the correct nesting order.
"""


def is_valid(s: str) -> bool:
    """Return True if the brackets in s are correctly nested and matched."""
    pairs = {")": "(", "}": "{", "]": "["}
    stack: list[str] = []
    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            # Outside the problem's alphabet; treat as invalid input.
            return False
    return not stack


if __name__ == "__main__":
    cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(", False),
        (")", False),
        ("((()))", True),
        ("([{}])", True),
    ]
    for s, expected in cases:
        result = is_valid(s)
        assert result == expected, f"is_valid({s!r}) = {result}, expected {expected}"
    print("all tests passed")
