# Uses python3

import queue
import sys
from math import inf


def dijkstra(adj, cost, s, t):

    # if s == t:
    #     return cost[s][adj[s].index(t)]

    seen = set([s])
    dist = [inf] * len(adj)
    dist[s] = 0
    prev = [None] * len(adj)

    q = queue.Queue()
    q.put(s)

    while not q.empty():

        n = q.get()

        edges = []
        for i, adjacent in enumerate(adj[n]):
            edges.append((adjacent, cost[n][i] + dist[n]))

        edges = sorted(edges, key=lambda x: x[1])
        for (e, w) in edges:
            if not e in seen:
                seen.add(e)
                q.put(e)

            if w < dist[e]:
                dist[e] = w
                prev[e] = n

    # pprint(list(zip(dist, prev)))

    return dist[t] if dist[t] is not inf else -1


def parse(input):
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0 : (3 * m) : 3], data[1 : (3 * m) : 3]), data[2 : (3 * m) : 3]))
    data = data[3 * m :]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    return dijkstra(adj, cost, s, t)


if __name__ == "__main__":
    input = sys.stdin.read()
    print(parse(input))


def test_parse():
    assert 3 == parse(open("input.txt").read())
    assert 6 == parse(open("input.1.txt").read())
    assert -1 == parse(open("input.2.txt").read())
    assert 3 == parse(open("input.3.txt").read())
    assert 0 == parse(open("input.4.txt").read())
    assert 0 == parse(open("input.5.txt").read())
