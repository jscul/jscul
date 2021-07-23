# Uses python3
import sys


def fast_count_segments(starts, ends, points):
    starts = sorted(starts)
    ends = sorted(ends)
    points = sorted(zip(points, range(0, len(points))), key=lambda x: x[0])

    s, e, p = 0, 0, 0
    segment_overlap = 0

    res = [None] * len(points)
    while p < len(points):
        while s < len(starts) and starts[s] <= points[p][0]:
            s += 1
            segment_overlap += 1

        while e < len(ends) and ends[e] < points[p][0]:
            e += 1
            segment_overlap -= 1

        res[points[p][1]] = segment_overlap

        p += 1

    return res


def naive_count_segments(starts, ends, points):

    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2 : 2 * n + 2 : 2]
    ends = data[3 : 2 * n + 2 : 2]
    points = data[2 * n + 2 :]
    # use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=" ")
