# Uses python3

# https://www.youtube.com/watch?v=4ZlRH0eK-qQ&ab_channel=AbdulBari

import heapq
import math
import sys


def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def get_graph(x, y):
    adj = []
    for i in range(len(x)):
        adj.append([])

    min_edge = None

    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            d = dist(x[i], y[i], x[j], y[j])
            adj[i].append((j, d))
            adj[j].append((i, d))

            if min_edge == None or d < min_edge[0]:
                min_edge = (d, i, j)

    return adj, min_edge


def minimum_distance(x, y):

    if len(x) == 1:
        return 0

    adj, min_edge = get_graph(x, y)

    seen = set()
    edges = [min_edge]

    result = 0.0

    while edges:
        d, i, j = heapq.heappop(edges)

        if i in seen and j in seen:
            continue

        seen.add(j)
        seen.add(i)

        for e, _d in adj[i]:
            heapq.heappush(edges, (_d, i, e))

        for e, _d in adj[j]:
            heapq.heappush(edges, (_d, j, e))

        result += d

    return result


def parse(input):
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    return "{0:.9f}".format(minimum_distance(x, y))


if __name__ == "__main__":
    input = sys.stdin.read()
    print(parse(input))


def test_parse():
    assert "3.000000000" == parse(open("input.1.txt").read())
    assert "7.064495102" == parse(open("input.2.txt").read())
    assert "4.000000000" == parse(open("input.3.txt").read())
    assert "5.000000000" == parse(open("input.4.txt").read())
    assert "0.000000000" == parse(open("input.5.txt").read())
