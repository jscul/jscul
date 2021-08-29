# Uses python3
import sys


def optimal_sequence(n):
    # there is no 0 n
    sequence = [None, 0]
    for i in range(2, n + 1):
        if i % 3 == 0:
            sequence.append(min(sequence[int(i / 3)], sequence[i - 1]) + 1)
        elif i % 2 == 0:
            sequence.append(min(sequence[int(i / 2)], sequence[i - 1]) + 1)
        else:
            sequence.append(sequence[-1] + 1)

    i = n
    ret = []
    while i != 0:
        ret.append(i)
        if i % 3 == 0 and sequence[int(i / 3)] < sequence[i - 1]:
            i = int(i / 3)
            continue
        elif i % 2 == 0 and sequence[int(i / 2)] < sequence[i - 1]:
            i = int(i / 2)
            continue
        i -= 1


    return reversed(ret)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
