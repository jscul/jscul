# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.0
    # write your code here

    vals = list(zip(values, weights))
    vals.sort(key=lambda a: a[0] / a[1])
    vals.reverse()

    for i, val in enumerate(vals):
        if capacity == 0:
            break
        v, w = val
        if w >= capacity:
            value += capacity * (v / w)
            capacity -= capacity
        else:
            value += v
            capacity -= w

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2 : (2 * n + 2) : 2]
    weights = data[3 : (2 * n + 2) : 2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
