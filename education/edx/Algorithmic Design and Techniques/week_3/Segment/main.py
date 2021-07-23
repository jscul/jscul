# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple("Segment", "start end")


def optimal_points(segments):
    segments.sort(key=lambda s: s.start)

    points = [None]

    for start, end in segments:
        if points[-1] is None:
            points[-1] = end

        if end < points[-1]:
            points[-1] = end
        elif start > points[-1]:
            points.append(end)

    return points


if __name__ == "__main__":

    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))

    points = optimal_points(segments)
    print(len(points))

    for p in points:
        print(p, end=" ")
