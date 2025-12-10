with open("day-09/input.txt") as f:
    input_data = f.readlines()


def q1() -> int:
    tiles = [eval(p) for p in input_data]

    largest = max(
        [
            (abs(t1[0] - t2[0]) + 1) * (abs(t1[1] - t2[1]) + 1)
            for t1 in tiles
            for t2 in tiles
        ]
    )

    return largest


def q2() -> int:
    tiles = [[int(n) for n in p.split(",")] for p in input_data]

    vertical_segments = []
    horizontal_segments = []

    for i in range(len(tiles)):
        x1, y1 = tiles[i]
        x2, y2 = tiles[(i + 1) % len(tiles)]
        if x1 == x2:
            y_min, y_max = min(y1, y2), max(y1, y2)
            vertical_segments.append((x1, y_min, y_max))
        else:
            x_min, x_max = min(x1, x2), max(x1, x2)
            horizontal_segments.append((x_min, x_max, y2))

    def inside(t1, t2):
        min_x, min_y = min(t1[0], t2[0]), min(t1[1], t2[1])

        intersections = 0
        for vx, vmin_y, vmax_x in vertical_segments:
            if vx > min_x:
                if vmin_y <= min_y < vmax_x:
                    intersections += 1

        return intersections % 2 == 1

    def intersects(t1, t2):
        min_x, min_y = min(t1[0], t2[0]), min(t1[1], t2[1])
        max_x, max_y = max(t1[0], t2[0]), max(t1[1], t2[1])

        for vx, vy_min, vy_max in vertical_segments:
            if min_x < vx < max_x:
                overlap_min = max(vy_min, min_y)
                overlap_max = min(vy_max, max_y)
                if overlap_min < overlap_max:
                    return True

        for hx_min, hx_max, hy in horizontal_segments:
            if min_y < hy < max_y:
                overlap_min = max(hx_min, min_x)
                overlap_max = min(hx_max, max_x)
                if overlap_min < overlap_max:
                    return True

        return False

    largest = max(
        [
            (abs(t1[0] - t2[0]) + 1) * (abs(t1[1] - t2[1]) + 1)
            for t1 in tiles
            for t2 in tiles
            if inside(t1, t2) and not intersects(t1, t2)
        ]
    )

    return largest


def main() -> None:
    print(q1())
    print(q2())


if __name__ == "__main__":
    main()
