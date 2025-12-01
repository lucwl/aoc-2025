import os

from scrape import get_headers
from update import update


def main() -> None:
    days = []

    for f in os.scandir():
        if f.is_dir() and (day := f.name[-2:]).isdigit():
            if f.name == f"day-{day}":
                days.append(day)

    days.sort()
    headers = get_headers()

    for day in days:
        update(day, headers)

    print(f"Finished updating {str(len(days))} days.")


if __name__ == "__main__":
    main()
