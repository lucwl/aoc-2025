import sys

from scrape import *


def update(day: int | str, headers: dict) -> None:
    print(f"Updating day-{day}...")
    dayF1 = str(int(day))
    dayF2 = dayF1 if int(dayF1) >= 10 else "0" + dayF1
    path = f"day-{dayF2}"

    articles = scrape_articles(int(dayF1), headers)

    if len(articles) == 0:
        assert "Could not scrape article."

    with open(path + "/challenge.md", "w") as f:
        f.write("\n".join(articles))

    inputs = scrape_inputs(int(dayF1), headers, articles)

    with open(path + "/input.txt", "w") as f:
        f.write(inputs[0])

    for i in range(1, len(inputs)):
        with open(path + f"/input{str(i)}.txt", "w") as f:
            f.write(inputs[i])


def main() -> None:
    USAGE = "python setup/update.py [day: int]"
    if len(sys.argv) != 2:
        sys.exit(f"update.py requires one argument day\n{USAGE}")

    if not sys.argv[1].isdigit():
        sys.exit(f"day argument should be of type integer\n{USAGE}")

    update(sys.argv[1], get_headers())
    print("Finished.")


if __name__ == "__main__":
    main()
