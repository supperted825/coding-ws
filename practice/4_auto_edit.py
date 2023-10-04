import re
import sys


def main():
    for line in sys.stdin:
        mo = re.search(r"\b(strlen)\(([\w]+)\)", line)

        if not mo:
            print(line, end="")
            continue

        args = mo.group(2)
        line = line.replace("strlen", "strnlen")
        line = line.replace(args, f"{args}, sizeof({args})")
        print(line, end="")


if __name__ == "__main__":
    main()
