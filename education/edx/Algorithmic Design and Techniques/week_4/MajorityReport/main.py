# Uses python3
import sys
from math import floor


# https://www.youtube.com/watch?v=mVpH8byx51Y&ab_channel=NideeshTerapalli


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    m = floor((right + left) / 2)
    l_side = get_majority_element(a, left, m)
    r_side = get_majority_element(a, m, right)

    if l_side == r_side:
        return l_side

    count_r = 0
    count_l = 0
    for i in range(left, right):
        if a[i] == r_side:
            count_r += 1
        elif a[i] == l_side:
            count_l += 1

    if count_l > (right - left) / 2:
        return l_side
    elif count_r > (right - left) / 2:
        return r_side

    return -1


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # print(get_majority_element(a, 0, n))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
