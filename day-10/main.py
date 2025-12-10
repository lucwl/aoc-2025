from collections import deque
from functools import cache
from pulp import *

with open("day-10/input.txt") as f:
    input_data = f.readlines()


def q1() -> int:
    min_depth = 0

    for line in input_data:
        split = line.split("] ")
        target = frozenset(i for i, char in enumerate(split[0][1:]) if char == "#")

        split = split[1].split(" {")
        buttons = [
            frozenset(int(n) for n in button[1:][:-1].split(","))
            for button in split[0].split(" ")
        ]

        queue: list[(int, frozenset[int])] = []
        visited: set[frozenset[int]] = set()
        queue.append(
            (
                0,
                frozenset(),
            )
        )

        while len(queue):
            depth, current = queue.pop(0)

            for button in buttons:
                toggled = current.symmetric_difference(button)
                if toggled in visited:
                    continue
                if toggled == target:
                    queue = []
                    min_depth += depth + 1
                    break

                visited.add(toggled)
                queue.append((depth + 1, toggled))

    return min_depth


def q2() -> int:
    total_min_depth = 0
    for line in input_data:
        split = line.split("] ")

        split = split[1].split(" {")
        buttons = frozenset(
            frozenset(int(n) for n in button[1:][:-1].split(","))
            for button in split[0].split(" ")
        )
        target_joltage = tuple([int(n) for n in split[1].strip()[:-1].split(",")])

        vars = [LpVariable(str(i), 0, cat="Integer") for i in range(len(buttons))]
        prob = LpProblem("myProblem", LpMinimize)

        for i, joltage in enumerate(target_joltage):
            prob += (
                lpSum([vars[j] for j, button in enumerate(buttons) if i in button])
                == joltage
            )

        objective = lpSum(vars)
        prob += objective

        prob.solve(PULP_CBC_CMD(msg=0))
        total_min_depth += int(value(objective))

    return total_min_depth


# SOLUTION GRAVEYARD

# @cache
# def combi(depth, buttons, joltage) -> int:
#     if all([j == 0 for j in joltage]):
#         return depth

#     minimum = float("inf")

#     for button in buttons:
#         new_joltage = tuple(j - 1 if c in button else j for c, j in enumerate(joltage))
#         if -1 in new_joltage:
#             continue
#         minimum = min(minimum, combi(depth + 1, buttons, new_joltage))

#     return minimum


# def q2() -> int:
#     total_min_depth = 0
#     for line in input_data:
#         split = line.split("] ")

#         split = split[1].split(" {")
#         buttons = frozenset(
#             frozenset(int(n) for n in button[1:][:-1].split(","))
#             for button in split[0].split(" ")
#         )
#         target_joltage = tuple([int(n) for n in split[1].strip()[:-1].split(",")])

#         total_min_depth += combi(0, buttons, target_joltage)

#     return total_min_depth


# def q2() -> int:
#     min_depth = 0

#     for line in input_data:
#         split = line.split("] ")

#         split = split[1].split(" {")
#         buttons = [
#             frozenset(int(n) for n in button[1:][:-1].split(","))
#             for button in split[0].split(" ")
#         ]
#         target_joltage = tuple([int(n) for n in split[1].strip()[:-1].split(",")])

#         queue = deque()
#         visited: set[tuple[int]] = set()
#         queue.append((0, tuple(0 for _ in target_joltage)))

#         while len(queue) > 0:
#             depth, joltage = queue.popleft()

#             for button in buttons:
#                 new_joltage = tuple(
#                     j + 1 if c in button else j for c, j in enumerate(joltage)
#                 )

#                 if new_joltage in visited:
#                     continue
#                 if new_joltage == target_joltage:
#                     queue = []
#                     min_depth += depth + 1
#                     break

#                 visited.add(new_joltage)

#                 if any([a > b for a, b in zip(new_joltage, target_joltage)]):
#                     continue

#                 queue.append((depth + 1, new_joltage))

#     return min_depth


def main() -> None:
    print(q1())
    print(q2())


if __name__ == "__main__":
    main()
