# Uses python3
import sys


def optimal_summands(n):
    summands = []

    i = 1
    while n > 0:
        n -= i
        if n < 0:
            n += i
            break

        summands.append(i)

        i += 1

    summands[-1] += n
    return summands


if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=" ")
