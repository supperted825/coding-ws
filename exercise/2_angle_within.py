import sys


def check(a, b, c):
    # In the entire circle
    if b == c:
        return "TRUE"

    # Regular case, a is simply between b and c
    if b < c:
        if b <= a <= c:
            return "TRUE"
        return "FALSE"

    # Reflex case, a is at start or end of circle
    else:
        if a >= b or a <= c:
            return "TRUE"
        return "FALSE"


def main():
    for line in sys.stdin:
        line = line.strip()
        a, b, c = [int(i) % 360 for i in line.split()]
        print(check(a, b, c))


if __name__ == "__main__":
    main()
