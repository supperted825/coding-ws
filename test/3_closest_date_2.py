import sys
import bisect

from datetime import datetime


def get_valid_date(date):
    try:
        date = datetime.strptime(date, "%Y%m%d")
        return date if date.year > 1600 else None
    except:
        return None


def abs_date_diff(d1, d2):
    return abs((d1 - d2).days)


def main():
    valid_dates = []
    min_diff = 4000000

    for line_idx, line in enumerate(sys.stdin):
        line = line.strip()
        date = get_valid_date(line)

        # Always print this out, even if first date is not valid
        if line_idx == 0:
            print(min_diff)

        # Nothing to print or update if this is not a valid date
        if not date:
            continue

        insertion_idx = bisect.bisect(valid_dates, date)
        valid_dates.insert(insertion_idx, date)

        # Do not make updates if there are not at least 2 valid dates
        # the smallest diff is still 4 million, and printed on line 0.
        if len(valid_dates) < 2:
            continue

        # Insertion is at the end, compare with date in front
        if insertion_idx == len(valid_dates) - 1:
            before_date = valid_dates[len(valid_dates) - 2]
            new_min_diff = min(min_diff, abs_date_diff(before_date, date))

        # Insertion is at the front, compare with second date
        elif insertion_idx == 0:
            after_date = valid_dates[1]
            new_min_diff = min(min_diff, abs_date_diff(after_date, date))

        # Insertion is in between, compare with before and after dates
        else:
            before_date = valid_dates[insertion_idx - 1]
            after_date = valid_dates[insertion_idx + 1]
            new_min_diff = min(
                min_diff,
                abs_date_diff(before_date, date),
                abs_date_diff(after_date, date),
            )

        if new_min_diff < min_diff and line_idx > 0:
            print(new_min_diff)
            min_diff = new_min_diff


if __name__ == "__main__":
    main()
