# Uses python3
import itertools
import sys


def partition3(A):
    s = sum(A)
    if s % 3 != 0:
        return 0

    s /= 3

    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))
