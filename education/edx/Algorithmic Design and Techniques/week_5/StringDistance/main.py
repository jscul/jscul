# https://www.youtube.com/watch?v=MiqoA-yF-0M&ab_channel=DestinyDestinyVerified


def edit_distance(s, t):
    # write your code here
    dp = []
    for i in range(0, len(s) + 1):
        dp.append([0] * (len(t) + 1))
        dp[i][0] = i

    dp[0] = list(range(0, len(t) + 1))

    for x in range(1, len(s) + 1):
        for y in range(1, len(t) + 1):
            if s[x - 1] == t[y - 1]:
                dp[x][y] = dp[x - 1][y - 1]
            else:
                dp[x][y] = min(dp[x - 1][y - 1], dp[x - 1][y], dp[x][y - 1]) + 1

    return dp[-1][-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
