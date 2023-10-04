import re
import sys
import math

EVALUATE_PATTERN = r"(?<=[+\-/*])|(?=[+\-/*])"


def get_inverse_op(op):
    return {"*": "/", "/": "*", "+": "-", "-": "+"}[op]


def round2(num):
    return math.floor(num * 100 + 0.5) / 100


def compute(a, operator, b):
    a, b = int(a), int(b)
    if operator == "*":
        ans = a * b
    elif operator == "/":
        ans = a / b
    elif operator == "+":
        ans = a + b
    elif operator == "-":
        ans = a - b
    print(f"{round2(ans):.2f}")


def solve(eqn):
    lhs, rhs = eqn.split("=")

    # Simple Case: 'x' is already isolated. In this case,
    # we just need to compute the answer directly.
    if lhs == "x" or rhs == "x":
        if rhs == "x":
            lhs, rhs = rhs, lhs
        a, operator, b = re.split(EVALUATE_PATTERN, rhs)
        return compute(a, operator, b)

    # Annoying Case: 'x' is with some other operator, we need to
    # preprocess the string so that it becomes isolated

    # Always place 'x' on the left side, at this point we know 'x'
    # is accompanied with another number via some operator
    if "x" in rhs:
        lhs, rhs = rhs, lhs

    a, operator, b = re.split(EVALUATE_PATTERN, lhs)

    # Shift b to the other side by inverting the operator
    # Case: x + 2 = 0 OR x / 2 = 0 OR x * 2 = 0 OR x - 2 = 0
    if a == "x":
        operator = get_inverse_op(operator)
        return compute(rhs, operator, b)

    # Case: 515 / x = 824
    if operator == "/":
        return compute(a, "/", rhs)

    # Case: 2 - x = 1
    if operator == "-":
        return compute(a, "-", rhs)

    # Case: 5 * x = 0 / 5 + x = 0
    if operator in "+*":
        operator = get_inverse_op(operator)
        return compute(rhs, operator, a)


if __name__ == "__main__":
    for line in sys.stdin:
        solve(line.strip())
