# Uses python3

import sys
from pprint import pprint


def lcs3(a, b, c):
    # write your code here

    dp = [[[0 for _ in range(len(c) + 1)] for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

    for i in range(1, len(c) + 1):
        for j in range(1, len(b) + 1):
            for k in range(1, len(a) + 1):
                if a[k - 1] == b[j - 1] == c[i - 1]:
                    dp[k][j][i] = dp[k - 1][j - 1][i - 1] + 1
                else:
                    dp[k][j][i] = max(dp[k][j - 1][i], dp[k][j][i - 1], dp[k - 1][j][i])

    # pprint(dp)

    return dp[-1][-1][-1]


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
