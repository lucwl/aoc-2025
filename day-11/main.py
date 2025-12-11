with open("day-11/input.txt") as f:
    input_data = f.readlines()

graph = {}
for line in input_data:
    parts = line.strip().split(": ")
    graph[parts[0]] = set(parts[1].split(" "))

reverse_graph = {key: set() for key in graph.keys()}
reverse_graph["out"] = set()

for node, edges in graph.items():
    for edge in edges:
        if edge not in reverse_graph:
            reverse_graph[edge] = set()
        reverse_graph[edge].add(node)


def q1() -> int:
    stack = ["you"]
    paths = 0

    while stack:
        cur = stack.pop()

        if cur == "out":
            paths += 1
            continue

        for node in graph[cur]:
            stack.append(node)

    return paths


def total_paths(topo, start, end):
    paths = dict.fromkeys(graph.keys(), 0)
    paths[start] = 1

    for node in topo[topo.index(start) + 1 : topo.index(end) + 1]:
        paths[node] = sum(paths[incoming] for incoming in reverse_graph[node])

    return paths[end]


def q2() -> int:
    # https://en.wikipedia.org/wiki/Topological_sorting
    L = []
    S = set(["svr"])
    graph_temp = dict(graph)

    while S:
        n = S.pop()
        L.append(n)

        if n not in graph:
            continue
        for m in set(graph_temp[n]):
            graph_temp[n].remove(m)

            if all(m not in edges for edges in graph_temp.values()):
                S.add(m)

    return (
        total_paths(L, "svr", "dac")
        * total_paths(L, "dac", "fft")
        * total_paths(L, "fft", "out")
    ) + (
        total_paths(L, "svr", "fft")
        * total_paths(L, "fft", "dac")
        * total_paths(L, "dac", "out")
    )


def main() -> None:
    print(q1())
    print(q2())


if __name__ == "__main__":
    main()
