from functools import reduce
import operator

with open("day-06/input.txt") as f:
    inputData = f.readlines()


def q1() -> int:
    total = 0
    lines = [
        [p.strip() for p in line.split(" ") if len(p.strip()) > 0] for line in inputData
    ]

    for prob in zip(*lines):
        prob = list(prob)
        op = prob.pop()
        nums = [int(n) for n in prob]

        if op == "*":
            total += reduce(operator.mul, nums, 1)
        elif op == "+":
            total += sum(nums)

    return total


def q2() -> int:
    total = 0

    height = len(inputData)
    width = max([len(line) for line in inputData])

    problems = []
    cur_prob = []

    for i in range(width + 1):
        if i == width or all(inputData[j][i] == " " for j in range(height)):
            problems.append(cur_prob)
            cur_prob = []
            continue

        nums = []
        for j in range(height):
            try:
                nums.append(inputData[j][i])
            except IndexError:
                nums.append("")
        cur_prob.append(nums)

    for prob in problems:
        op = prob[0][-1]

        nums = [
            int("".join([d for d in n if len(d) > 0 and d.isdigit()]))
            for n in prob
            if "\n" not in n
        ]
        if op == "*":
            total += reduce(operator.mul, nums, 1)
        elif op == "+":
            total += sum(nums)

    return total


def main() -> None:
    print(q1())
    print(q2())


if __name__ == "__main__":
    main()
