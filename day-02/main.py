with open("day-02/input.txt") as f:
    inputData = f.readlines()


def q1() -> int:
    pairs = inputData[0].split(",")
    total = 0

    for id_pair in pairs:
        parts = id_pair.split("-")
        a = parts[0]
        b = parts[1]

        n = int(a)
        m = int(b)

        while n <= m:
            if len(a) % 2 == 0 and a[: int(len(a) / 2)] == a[int(len(a) / 2) :]:
                total += n
            n += 1
            a = str(n)

    return total


def q2() -> int:
    pairs = inputData[0].split(",")
    total = 0

    for id_pair in pairs:
        parts = id_pair.split("-")
        a = parts[0]
        b = parts[1]

        n = int(a)
        m = int(b)

        while n <= m:
            for i in range(1, len(a)):
                if len(a) % i == 0:
                    cur = ""
                    parts = []

                    for j in range(len(a)):
                        if j % i == 0 and j != 0:
                            parts.append(cur)
                            cur = ""
                        cur += a[j]
                    parts.append(cur)

                    if len(parts) > 1 and all(map(lambda p: p == parts[0], parts)):
                        total += n
                        break
            n += 1
            a = str(n)

    return total


def main() -> None:
    print(q1())
    print(q2())


if __name__ == "__main__":
    main()
