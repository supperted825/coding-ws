import sys
import datetime


def get_legal_date(date_str):
    date_str = date_str.strip()
    try:
        date = datetime.datetime.strptime(date_str, "%Y%m%d")
    except:
        return None
    if date.year < 1600:
        return None
    return date


def main():
    valid_dates = []

    for line in sys.stdin:
        date = get_legal_date(line)
        if date:
            valid_dates.append(date)

    if len(valid_dates) < 2:
        print(-1)
        return

    valid_dates.sort()
    min_diff = min(
        (valid_dates[i] - valid_dates[i - 1]).days for i in range(1, len(valid_dates))
    )
    print(min_diff)


if __name__ == "__main__":
    main()
