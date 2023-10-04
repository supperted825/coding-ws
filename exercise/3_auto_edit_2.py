import sys


def main():
    for line in sys.stdin:
        clean_line = line.strip()
        if clean_line.startswith("//") and (
            clean_line.endswith(";") or clean_line.endswith("{")
        ):
            continue
        print(line, end="")


if __name__ == "__main__":
    main()
