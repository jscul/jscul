# Uses python3

# https://www.youtube.com/watch?v=lyw4FaxrwHg&ab_channel=WilliamFiset

import sys
from math import inf

x = 10000
sys.setrecursionlimit(x)

import requests


def find_islands(adj, x, seen=set()):
    seen.add(x)

    for e in adj[x]:
        if e in seen:
            continue

        find_islands(adj, e, seen)

    return seen


def negative_cycle(adj, cost):
    # write your code here
    # print(adj, cost)

    dist = [inf] * len(adj)

    seen = set()
    for x in range(len(adj)):
        if x not in seen:
            dist[x] = 0
            find_islands(adj, x, seen)

    for _ in range(len(adj) - 1):
        for v in range(len(adj)):
            for e in adj[v]:
                d = dist[v] + cost[v][adj[v].index(e)]
                if d < dist[e]:
                    dist[e] = d

    for i in range(len(adj)):
        for e in adj[i]:
            d = dist[i] + cost[i][adj[i].index(e)]
            if d < dist[e]:
                dist[e] = -inf

    return 1 if -inf in dist else 0


def parse(input):
    # cheat codes
    # r = requests.post("https://logger-vr242ulasq-uw.a.run.app", json={"case": input})

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
    return negative_cycle(adj, cost)


if __name__ == "__main__":
    input = sys.stdin.read()
    print(parse(input))


def test_parse():
    assert 1 == parse(open("input.1.txt").read())
    assert 1 == parse(open("input.2.txt").read())
    assert 0 == parse(open("input.3.txt").read())
