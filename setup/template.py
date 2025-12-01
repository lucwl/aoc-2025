import os
import sys

from scrape import get_headers
from constants import *
from update import update

TEMPLATE = """with open("PATH/input.txt") as f:
    inputData = f.readlines()

def q1() -> int:
    a = 0
    for line in inputData.split():
        pass
    return -1

def q2() -> int:
    return -1

def main() -> None:
    print(q1())
    print(q2())

if __name__ == "__main__":
    main()
"""


def main() -> None:
    USAGE = "Usage: python template.py [day: int] [scrapeArticle: Optional[bool]]"

    if not (1 < len(sys.argv) <= 3):
        sys.exit(f"template.py requires at least one argument [day]\n{USAGE}")

    if not sys.argv[1].isdigit():
        sys.exit(f"[day] argument should be of type integer not {sys.argv[1]}\n{USAGE}")

    if not (0 < int(sys.argv[1]) <= 25):
        sys.exit(
            f"[day] argument should be between 1 and 25 inclusive not {sys.argv[1]}\n{USAGE}"
        )

    dayF1 = str(int(sys.argv[1]))
    dayF2 = dayF1 if int(dayF1) >= 10 else "0" + dayF1

    path = f"day-{dayF2}"

    if os.path.isdir(path):
        sys.exit(f"Directory {path} already exists.")

    os.mkdir(path)

    with open(path + "/main.py", "w") as f:
        f.write(TEMPLATE.replace("PATH", path))

    with open(path + "/input.txt", "w") as f:
        f.write(f"Get your input from {INPUT_ENDPOINT.replace('XX', dayF1)}")

    with open(path + "/challenge.md", "w") as f:
        f.write(
            f"Get the challenge article from {ARTICLE_ENDPOINT.replace('XX', dayF1)}"
        )

    if len(sys.argv) == 3:
        update(dayF1, get_headers())

    print(f"Finished. Have fun coding day {dayF2}!")


if __name__ == "__main__":
    main()
