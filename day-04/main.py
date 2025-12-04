with open("day-04/input.txt") as f:
    inputData = f.readlines()


def q1() -> int:
    total = 0

    height = len(inputData)
    width = len(inputData[0]) - 1

    for x in range(height):
        for y in range(width):
            if inputData[x][y] != "@":
                continue
            count = 0
            for dx, dy in [
                (-1, 1),
                (0, 1),
                (1, 1),
                (-1, 0),
                (1, 0),
                (-1, -1),
                (0, -1),
                (1, -1),
            ]:
                to_x = x + dx
                to_y = y + dy
                if to_x < 0 or to_x > height - 1:
                    continue
                elif to_y < 0 or to_y > width - 1:
                    continue
                if inputData[to_x][to_y] == "@":
                    count += 1

            if count < 4:
                total += 1

    return total


def q2() -> int:
    total = 0

    height = len(inputData)
    width = len(inputData[0]) - 1

    data = [list(row) for row in inputData]
    new_data = list(data)

    while total == 0 or total_round > 0:
        total_round = 0
        
        for x in range(height):
            for y in range(width):
                if data[x][y] != "@":
                    continue
                count = 0
                for dx, dy in [
                    (-1, 1),
                    (0, 1),
                    (1, 1),
                    (-1, 0),
                    (1, 0),
                    (-1, -1),
                    (0, -1),
                    (1, -1),
                ]:
                    to_x = x + dx
                    to_y = y + dy
                    if to_x < 0 or to_x > height - 1:
                        continue
                    elif to_y < 0 or to_y > width - 1:
                        continue
                    if data[to_x][to_y] == "@":
                        count += 1

                if count < 4:
                    total_round += 1
                    new_data[x][y] = "."
        total += total_round

    return total


def main() -> None:
    print(q1())
    print(q2())


if __name__ == "__main__":
    main()
