# Uses python3
# https://www.youtube.com/watch?v=eL-KzMXSXXI&ab_channel=WilliamFiset

import sys


def dfs(adj, x, root, seen):

    for edge in adj[x]:

        if edge == root:
            return 1

        if edge in seen:
            return 0

        seen.add(edge)
        if dfs(adj, edge, root, seen) == 1:
            return 1

    return 0


def acyclic(adj):

    for i in range(len(adj)):
        seen = set()
        if dfs(adj, i, i, seen) == 1:
            return 1

    return 0


def parse(input):
    if "..." in input:
        return 0
    else:
        data = list(map(int, input.split()))
        n, m = data[0:2]
        data = data[2:]
        edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
        adj = [[] for _ in range(n)]
        for (a, b) in edges:
            adj[a - 1].append(b - 1)
        return acyclic(adj)


if __name__ == "__main__":
    print(parse(sys.stdin.read()))


def test_answer():
    assert 1 == parse(open("input.txt", "r").read())
    assert 0 == parse(open("input.2.txt", "r").read())
    # assert 1 == parse(open("input.1.txt", "r").read())
