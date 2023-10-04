import sys
import datetime


def main():
    past_date = None

    for i, line in enumerate(sys.stdin):
        date = line.strip()

        try:
            curr_date = datetime.datetime.strptime(date, "%d%m%Y")
        except:
            curr_date = None

        if not curr_date or curr_date.date() < datetime.date(1600, 1, 1):
            print(f"Line {i+1}: Illegal")
            curr_date = None

        if past_date and curr_date and curr_date < past_date:
            print(f"Line {i+1}: Older")

        past_date = curr_date


if __name__ == "__main__":
    main()
