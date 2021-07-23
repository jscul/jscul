# Uses python3
import math
import sys


def get_change(m):
    # write your code here for 1, 3, 4
    ret = [0]

    for i in range(1, m + 1):
        if i in (1, 3, 4):
            ret.append(1)
        else:
            min_val = i
            for j in range(1, math.ceil(i / 2) + 1):
                min_val = min(ret[j] + ret[i - j], min_val)
                if min_val == 2:
                    break
            ret.append(min_val)

    return ret[-1]


if __name__ == "__main__":
    m = int(sys.stdin.read())
    print(get_change(m))
