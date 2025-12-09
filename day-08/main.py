from math import sqrt
from operator import mul
from itertools import chain
from functools import reduce

with open("day-08/input.txt") as f:
    inputData = f.readlines()


def euclidian_distance(p, q):
    x_p, y_p, z_p = p
    x_q, y_q, z_q = q
    return sqrt((x_p - x_q) ** 2 + (y_p - y_q) ** 2 + (z_p - z_q) ** 2)


def dfs(boxes, connections):
    sizes = []

    visited = {box: False for box in boxes}
    stack = []
    for box in boxes:
        if visited[box]:
            continue

        stack.append(box)
        visited[box] = True
        size = 1

        while len(stack) > 0:
            value = stack.pop()
            for conn in connections[value]:
                if visited[conn]:
                    continue
                size += 1
                visited[conn] = True
                stack.append(conn)

        sizes.append(size)

    return sizes


def q1() -> int:
    boxes = [tuple([int(n) for n in line.split(",")]) for line in inputData]

    connections = {box: set() for box in boxes}

    closest = sorted(
        (
            (box, q, euclidian_distance(box, q))
            for box in boxes
            for q in boxes
            if q != box
        ),
        key=lambda x: x[2],
    )

    print(closest)

    for i in range(len(inputData) * 2):
        p, q, _ = closest[i]

        connections[p].add(q)

    sizes = dfs(boxes, connections)

    return reduce(mul, sorted(sizes, reverse=True)[x:3], 1)


def q2() -> int:
    boxes = [tuple([int(n) for n in line.split(",")]) for line in inputData]

    connections = {box: set() for box in boxes}

    closest = sorted(
        (
            (box, q, euclidian_distance(box, q))
            for box in boxes
            for q in boxes
            if q != box
        ),
        key=lambda x: x[2],
    )

    for i in range(len(closest)):
        p, q, _ = closest[i]
        connections[p].add(q)

        if i < len(inputData) * 2:
            continue

        sizes = dfs(boxes, connections)

        if len(sizes) == 1:
            return p[0] * q[0]


def main() -> None:
    print(q1())
    print(q2())


if __name__ == "__main__":
    main()
