import sys


def main():
    # Anomaly if there is a logout when the user is not logged in
    # or there is a login when the user is already logged in.

    logged_in = set()

    for line_idx, line in enumerate(sys.stdin):
        line = line.strip()
        log_type, user, _ = line.split(" ")

        if log_type == "login":
            if user in logged_in:
                print(f"{line_idx + 1} " + line)
            else:
                logged_in.add(user)
        elif log_type == "logout":
            if user not in logged_in:
                print(f"{line_idx + 1} " + line)
            else:
                logged_in.remove(user)


if __name__ == "__main__":
    main()
