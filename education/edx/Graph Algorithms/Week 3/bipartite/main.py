# Uses python3

import queue
import sys


def bipartite(adj):

    dist = [None] * len(adj)

    # floating nodes check
    for i in range(len(adj)):

        # if we've seen the node already, no need to check bipartite
        if dist[i] is not None:
            continue

        q = queue.Queue()
        q.put(i)

        d = 0
        while True:

            same_depth_nodes = []
            while not q.empty():
                same_depth_nodes.append(q.get())

            if len(same_depth_nodes) == 0:
                break

            for same_depth_node in same_depth_nodes:

                for node in adj[same_depth_node]:
                    if dist[node] is None:
                        dist[node] = d
                        q.put(node)
                    elif dist[node] % 2 != d % 2:
                        return 0

            d += 1

    return 1


def parse(input):
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    return bipartite(adj)


if __name__ == "__main__":
    input = sys.stdin.read()
    print(parse(input))


def test_parse():
    assert 0 == parse(open("input.txt").read())
    assert 1 == parse(open("input.1.txt").read())
