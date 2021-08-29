# Uses python3

import sys
import functools
import random


def comp(a, b):
    return int(b + a) - int(a + b)


def largest_number(a):
    a = sorted(a, key=functools.cmp_to_key(comp))
    return "".join(a)


# if __name__ == "__main__":
#     tests = 100000
#     while tests != 0:
#         a = [str(random.randint(0, 10000)), str(random.randint(1, 100))]
#         res = largest_number(a)

#         option1 = a[0] + a[1]
#         option2 = a[1] + a[0]

#         if res == option1 and int(option1) < int(option2):
#             print(a, res)
#         elif res == option2 and int(option2) < int(option1):
#             print(a, res)

#         tests -= 1

if __name__ == "__main__":
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
