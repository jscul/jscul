# Uses python3
# https://www.youtube.com/watch?v=eL-KzMXSXXI&ab_channel=WilliamFiset

# import sys


# def dfs(adj, x, seen):

#     for edge in adj[x]:

#         if edge in seen:
#             return 1

#         seen.add(edge)
#         if dfs(adj, edge, seen) == 1:
#             return 1

#     return 0


def acyclic(adj):

    for i in range(len(adj)):
        if dfs(adj, i, set()) == 1:
            return 1

    return 0


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
