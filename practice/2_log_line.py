import re
import sys
from typing import Tuple


def process_line(s) -> Tuple[str, bool]:
    """
    Checks if the input is an EOL line, and returns the line
    without the strings that are encased in double quotes.
    """
    is_open_quote = False
    is_eol = False
    new_string = ""

    for i in range(len(s)):
        if s[i] == '"':
            is_open_quote = not is_open_quote
            continue
        if not is_open_quote:
            if s[i] == ";":
                is_eol = True
            if i < len(s) - 1 and s[i : i + 2] == "//":
                break
            new_string += s[i]

    return new_string, is_eol


def logger_body_is_prob(s):
    """
    Checks for problematic logger body. Note that the input to this function
    has already been sanitized, i.e. quoted characters have already been removed.
    """
    has_func_call = re.search(r"(?<!\(\) -> )\b\w+\(\)", s)
    has_concat = "+" in s
    return has_func_call or has_concat


def main():
    is_continue = False
    curr_start = None
    buffer = ""

    for line_idx, line in enumerate(sys.stdin):
        # Do regex check to validate this is a uncommented logger.debug()
        valid_debug = re.match(r"(?<!\/\/)[\s]*(logger\.debug\()", line)

        if not (valid_debug or is_continue):
            continue

        # Process the string for EOL or comment markers
        line, is_eol = process_line(line)

        # If not ending, switch cont to True and append current line to buffer
        if not is_eol:
            is_continue = True
            curr_start = curr_start if curr_start else (line_idx + 1)
            buffer += line
            continue

        # This is the terminal line for the statement, first merge with buffer if any
        # and extract
        mo = re.search(r"(?<=logger\.debug\().*(?=\);)", buffer + line)
        full_line = mo.group(0)

        # Then do the checks and print
        if logger_body_is_prob(full_line):
            if curr_start:
                print(curr_start)
            else:
                print(line_idx + 1)

        # Reset the tracking variables
        is_continue = False
        curr_start = None
        buffer = ""


if __name__ == "__main__":
    main()
