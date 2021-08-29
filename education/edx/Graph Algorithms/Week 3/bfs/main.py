# Uses python3

import queue
import sys
from math import inf


def distance(adj, s, t):

    seen = set()

    q = queue.Queue()
    q.put(s)

    d = 0
    while True:

        same_depth_nodes = []
        while not q.empty():
            same_depth_nodes.append(q.get())

        if len(same_depth_nodes) == 0:
            break

        for same_depth_node in same_depth_nodes:

            if same_depth_node == t:
                return d

            for node in adj[same_depth_node]:
                if node not in seen:
                    seen.add(node)
                    q.put(node)

        d += 1

    return -1


def parse(input):
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    return distance(adj, s, t)


if __name__ == "__main__":
    input = sys.stdin.read()
    print(parse(input))


def test_parse():
    assert 2 == parse(open("input.txt").read())
