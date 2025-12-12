with open("day-12/input.txt") as f:
    input_data = f.read()


def q1() -> int:
    split = input_data.split("\n\n")

    presents = []
    for present in split[:-1]:
        s = set()
        for j, line in enumerate(present.split("\n")[1:]):
            for i, char in enumerate(line):
                if char == "#":
                    s.add((i, j))
        presents.append(s)

    total = 0

    for region in split[-1].split("\n"):
        split = region.split(": ")
        width, height = tuple([int(n) for n in split[0].split("x" "")])
        indexes = [int(n) for n in split[1].split(" ")]

        grid = set()

        for y in range(height):
            for x in range(width):
                for p in range(len(presents)):
                    if indexes[p] <= 0:
                        continue
                    out = set()
                    for i, j in presents[p]:
                        if (
                            x + i > width
                            or y + j > height
                            or (x + i, y + j) in grid
                            or (x + i, y + j) in out
                        ):
                            break

                        out.add((x + i, y + j))
                    else:
                        grid.update(out)
                        indexes[p] -= 1

        if all([c == 0 for c in indexes]):
            total += 1

    return total


def q2() -> int:
    return -1


def main() -> None:
    print(q1())
    print(q2())


if __name__ == "__main__":
    main()
