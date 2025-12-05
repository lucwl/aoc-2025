with open("day-05/input1.txt") as f:
    inputData = f.readlines()


def q1() -> int:
    total = 0

    ranges = []
    range_mode = True

    for line in inputData:
        line = line.strip()
        if range_mode and line == "":
            range_mode = False
            continue

        if range_mode:
            parts = line.split("-")
            ranges.append((int(parts[0]), int(parts[1])))
        else:
            num = int(line)
            for lower, upper in ranges:
                if lower <= num <= upper:
                    total += 1
                    break

    return total


def q2() -> int:
    total = 0

    ranges = []

    for line in inputData:
        line = line.strip()
        if line == "":
            ranges.sort(key=lambda p: p[0])
            break

        parts = line.split("-")
        ranges.append((int(parts[0]), int(parts[1])))

    i = 0
    while i < len(ranges):
        lower, upper = ranges[i]
        lower_prev, upper_prev = ranges[i - 1]
        if (
            lower_prev <= lower <= upper_prev
            or lower_prev <= upper <= upper_prev
            or lower <= lower_prev <= upper
            or lower <= upper_prev <= upper
        ):
            ranges[i - 1] = (min(lower_prev, lower), max(upper_prev, upper))
            ranges.pop(i)
        else:
            i += 1

    for lower, upper in ranges:
        total += upper - lower + 1

    return total


def main() -> None:
    print(q1())
    print(q2())


if __name__ == "__main__":
    main()
