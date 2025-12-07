with open("day-07/input.txt") as f:
    inputData = f.readlines()

width = len(inputData[0])
height = len(inputData)

memo_splits = set()


def splits(i, j):
    n = 0

    if (i, j) in memo_splits:
        return 0

    if i == height - 1:
        return 0

    if inputData[i + 1][j] == ".":
        return splits(i + 1, j)
    else:
        n += 1
        if j > 0:
            n += splits(i + 1, j - 1)
        if j < width:
            n += splits(i + 1, j + 1)

    memo_splits.add((i, j))

    return n


def q1() -> int:
    return splits(0, inputData[0].index("S"))


memo_paths = {}


def paths(i, j):
    n = 0

    if (i, j) in memo_paths:
        return memo_paths[(i, j)]

    if i == height - 1:
        return 1

    if inputData[i + 1][j] == ".":
        return paths(i + 1, j)
    else:
        if j > 0:
            n += paths(i + 1, j - 1)
        if j < width:
            n += paths(i + 1, j + 1)

    memo_paths[(i, j)] = n

    return n


def q2() -> int:
    return paths(0, inputData[0].index("S"))


def main() -> None:
    print(q1())
    print(q2())


if __name__ == "__main__":
    main()
