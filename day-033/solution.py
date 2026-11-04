"""Evaluate Reverse Polish Notation.

Given an array of tokens in Reverse Polish Notation (postfix), evaluate
the expression and return the result as an integer. Division truncates
toward zero.
"""


def eval_rpn(tokens: list[str]) -> int:
    """Evaluate with a stack: operands go on, operators pop two and push back."""
    stack: list[int] = []
    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:
                # int() truncates toward zero, unlike floor division.
                stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack[-1]


if __name__ == "__main__":
    assert eval_rpn(["2", "1", "+", "3", "*"]) == 9
    assert eval_rpn(["4", "13", "5", "/", "+"]) == 6
    assert eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    # Division truncates toward zero, not toward negative infinity.
    assert eval_rpn(["-7", "2", "/"]) == -3
    assert eval_rpn(["7", "-2", "/"]) == -3
    # A single operand is just itself.
    assert eval_rpn(["42"]) == 42
    # Negative operands in a longer expression.
    assert eval_rpn(["-3", "-2", "*"]) == 6
    print("all tests passed")
