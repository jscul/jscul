# Uses python3
import sys

p = [
    1,
    1,
    2,
    3,
    5,
    8,
    3,
    1,
    4,
    5,
    9,
    4,
    3,
    7,
    0,
    7,
    7,
    4,
    1,
    5,
    6,
    1,
    7,
    8,
    5,
    3,
    8,
    1,
    9,
    0,
    9,
    9,
    8,
    7,
    5,
    2,
    7,
    9,
    6,
    5,
    1,
    6,
    7,
    3,
    0,
    3,
    3,
    6,
    9,
    5,
    4,
    9,
    3,
    2,
    5,
    7,
    2,
    9,
    1,
]


def pisano_period(m):
    """
    5 should give 20
    """

    if m == 0:
        return 0

    prev = 0
    curr = 1

    for i in range(m * m):
        prev, curr = curr, (curr + prev)
        if prev % m == 0 and curr % m == 1:
            return i + 1

    return m


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    # find out what the sequence length of 10 is
    # p = pisano_period(10)
    # print(p)

    # gather all values in array of 60 for calulation (inside p = [])
    # previous = 0
    # current = 1
    # sum = [current]
    # # _sum = current
    # for i in range(0, p):
    #     previous, current = current, previous + current
    #     sum.append(current % 10)
    #     # _sum += current

    return ((n // 60) * sum(p) + sum(p[0 : n % 60])) % 10

    # print(_sum)
    # print(sum)


def fibonacci_subsequence(m, n):
    if m == 0:
        return fibonacci_sum_naive(n)
    if m == n:
        return p[m % 60 - 1]

    sum = fibonacci_sum_naive(n) - fibonacci_sum_naive(m - 1)
    if sum < 0:
        sum = 10 + sum

    return sum


if __name__ == "__main__":
    input = sys.stdin.read()
    for line in input.split("\n"):
        if not line:
            continue
        m, n = map(int, line.split(" "))
        # print(pisano_period(10))
        # for i in range(30):
        #     print(pisano_period(i))

        print(fibonacci_subsequence(m, n))
