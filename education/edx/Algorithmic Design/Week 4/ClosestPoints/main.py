# Uses python3
import sys
import math


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def minimum_distance(p, l, r):
    # write your code here
    if r - l <= 1:
        return None
    elif r - l == 2:
        return dist(p[l], p[l + 1])

    m = (r + l) // 2

    d1 = minimum_distance(p, l, m)
    d2 = minimum_distance(p, m, r)

    if d1 is not None and d2 is None:
        d = d1
    elif d2 is not None and d1 is None:
        d = d2
    elif d1 is None and d2 is None:
        return None
    else:
        d = min(d1, d2)

    remaining = []

    for i in range(m - 1, l - 1, -1):
        if abs(p[i][0] - p[m][0]) <= d:
            remaining.append(p[i])
        else:
            break

    for i in range(m, r):
        if abs(p[i][0] - p[m][0]) <= d:
            remaining.append(p[i])
        else:
            break

    # remaining = filter(lambda x: abs(x[0] - m) <= d, p)

    remaining = sorted(remaining, key=lambda x: x[1])

    for i in range(0, len(remaining) - 1):
        for j in range(i + 1, min(len(remaining), i + 7)):
            d = min(d, dist(remaining[i], remaining[j]))

    return d


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(sorted(zip(x, y), key=lambda x: x[0]), 0, n)))
