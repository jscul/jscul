# Uses python3
import sys
import random


def p(*args, **kwargs):
    if False:
        print(*args, **kwargs)


def partition3(a, l, r):
    if l == r:
        return l, r

    j = l  # greatest index  < a[i]
    k = l  # greatest index == a[i]

    p(a[l:r])

    for i in range(l + 1, r + 1):
        if a[i] > a[l]:
            pass
        elif a[i] == a[l]:
            k += 1
            a[k], a[i] = a[i], a[k]
        elif a[i] < a[l]:
            j += 1
            k += 1
            a[i], a[k], a[j] = a[k], a[j], a[i]

    p(a[l:r])

    return j, k


def randomized_quick_sort(a, l, r):
    if l >= r:
        return

    rand = random.randint(l, r)
    a[l], a[rand] = a[rand], a[l]
    j, k = partition3(a, l, r)
    a[l], a[j] = a[j], a[l]

    randomized_quick_sort(a, l, j - 1)
    randomized_quick_sort(a, k + 1, r)


if __name__ == "__main__":
    input = sys.stdin.read()
    # for i in range(0, 100):
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, len(a) - 1)
    print(" ".join(map(str, a)), end=" ")

# if __name__ == "__main__":
#     input = sys.stdin.read()
#     for i in range(0, 100):
#         a = []
#         for j in range(0, random.randint(0, 10)):
#             a.append(random.randint(0, 20))

#         randomized_quick_sort(a, 0, len(a) - 1)
#         if " ".join(map(str, sorted(a))) != " ".join(map(str, a)):
#             print("HERE")
#             print(" ".join(map(str, sorted(a))), " ".join(map(str, a)))
#             break
