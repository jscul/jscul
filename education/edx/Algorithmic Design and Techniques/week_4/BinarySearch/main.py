# Uses python3
import sys
from math import floor


def binary_search(a, x):
    l, r = 0, len(a)
    # write your code here
    while l <= r:
        m = floor((l + r) / 2)
        if m >= len(a) or m < 0:
            return -1
        if x < a[m]:
            r = m - 1
        elif x > a[m]:
            l = m + 1
        else:
            return m

    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2 :]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end=" ")
