# Uses python3
import sys
from math import floor
from pprint import pprint


def optimal_weight(W, w):
    # write your code here
    dp = [[0 for _ in range(W + 1)] for _ in range(len(w))]

    for i in range(len(w)):
        for j in range(W + 1):
            # print("weight", j)
            # print("item_weight", w[i])

            if i == 0 and j >= w[i]:
                dp[i][j] = w[i]
            elif j < w[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], w[i] + (dp[i - 1][j - w[i]]))

    return dp[-1][-1]
    # pprint(dp)


if __name__ == "__main__":
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
