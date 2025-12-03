with open("day-03/input.txt") as f:
    inputData = f.readlines()


def q1() -> int:
    total = 0

    for line in inputData:
        line = line.strip()

        largest = 0
        a = 0
        b = 0

        for i in range(len(line)):
            if i == len(line) - 1:
                continue
            a = max(a, int(line[i]))

            for j in range(i + 1, len(line)):
                b = max(b, int(line[j]))

            largest = max(largest, int(str(a) + str(b)))
            a = 0
            b = 0

        total += largest

    return total


def q2() -> int:
    total = 0

    for line in inputData:
        line = line.strip()

        length = 12
        num = [0 for _ in range(12)]
        last = 0
        while length > 0:
            for i in range(last, len(line)):
                if i > len(line) - length:
                    continue
                if int(line[i]) > num[12-length]:
                    num[12-length] = int(line[i])
                    last = i + 1
            length -= 1

        total += int(''.join([str(d) for d in num]))

    return total


def main() -> None:
    print(q1())
    print(q2())


if __name__ == "__main__":
    main()
