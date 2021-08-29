# Uses python3

import sys


def dfs(adj, used, order, x):
    # write your code here
    if used[x] == 1:
        return

    for i in adj[x]:
        dfs(
            adj,
            used,
            order,
            i,
        )

    if used[x] == 0:
        used[x] = 1
        order.append(x)


def toposort(adj):
    order = []
    used = [0] * len(adj)

    for i in range(len(adj)):
        dfs(
            adj,
            used,
            order,
            i,
        )

    return reversed(order)


def parse(input):
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    return " ".join([str(x + 1) for x in order])


if __name__ == "__main__":
    input = sys.stdin.read()
    print(parse(input))


def test_answer():
    # test doesn't work here because order can vary, but still be right
    print(parse(open("input.txt", "r").read()))
    assert "4 3 1 2" == parse(open("input.txt", "r").read())
    assert "4 1 3 1" == parse(open("input.1.txt", "r").read())
    assert "5 4 3 2 1" == parse(open("input.2.txt", "r").read())
