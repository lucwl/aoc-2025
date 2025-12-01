with open("day-01/input.txt") as f:
    inputData = f.readlines()


def q1() -> int:
    counter = 50
    total = 0
    for line in inputData:
        if line[0] == "L":
            counter = (counter - int(line[1:])) % 100
        elif line[0] == "R":
            counter = (counter + int(line[1:])) % 100

        if counter == 0:
            total += 1

    return total


def q2() -> int:
    counter = 50
    total = 0
    for line in inputData:
        if line[0] == "L":
            for _ in range(int(line[1:])):
                counter -= 1
                if counter == 0:
                    total += 1
                if counter == -1:
                    counter = 99

        elif line[0] == "R":
            for _ in range(int(line[1:])):
                counter += 1
                if counter == 100:
                    total += 1
                    counter = 0

    return total


def main() -> None:
    print(q1())
    print(q2())


if __name__ == "__main__":
    main()
