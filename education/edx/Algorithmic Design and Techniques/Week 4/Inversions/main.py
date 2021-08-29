# Uses python3
import sys


def merge(a, b):
    r = []

    l_count = 0
    c = 0

    i = j = 0
    while i + j < len(a) + len(b):
        # print(a[i:], b[j:], "->", r, c)

        if i == len(a):
            r.append(b[j])
            j += 1
            c += l_count
        elif j == len(b):
            r.append(a[i])
            i += 1
        elif a[i] < b[j]:
            r.append(b[j])
            j += 1
            c += l_count
        elif a[i] > b[j]:
            r.append(a[i])
            i += 1
            l_count += 1
        elif a[i] == b[j]:
            r.append(b[j])
            j += 1
            c += l_count

    # print(a[i:], b[j:], "->", r, c)

    return r, c


def merge_sort(a, l, r):
    if r - l == 1:
        return [a[l]], 0

    avg = (l + r) // 2
    l_side, l_inversions = merge_sort(a, l, avg)
    r_side, r_inversions = merge_sort(a, avg, r)

    # print(l_side, l_inversions)
    # print(r_side, r_inversions)

    lr, total = merge(l_side, r_side)

    return lr, total + l_inversions + r_inversions


# def get_number_of_inversions(a, b, l, r):
#     number_of_inversions = 0
#     if r - l <= 1:
#         return number_of_inversions
#     avg = (l + r) // 2
#     number_of_inversions += get_number_of_inversions(avg, b, l, a)
#     number_of_inversions += get_number_of_inversions(avg, b, a, r)
#     # write your code here
#     return number_of_inversions


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(merge_sort(a, 0, len(a))[1])

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
