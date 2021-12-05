## puzzle 1

from typing import List, Tuple
from collections import defaultdict, namedtuple

Point = namedtuple("Point", ("x", "y"))


def point_from_coords(coords: str):
    x, y = map(int, coords.split(","))
    return Point(x, y)


def inclusive_range(a, b):
    # python range is fucky
    step = 1 if a < b else -1
    end = b + 1 if a < b else b - 1
    for i in range(a, end, step):
        yield i


def is_diagonal(start, stop):
    if abs(start.x - stop.x) == abs(start.y - stop.y):
        return True
    return False

def diagonal_range(start: Point, stop: Point):
    for x, y in zip(inclusive_range(start.x, stop.x), inclusive_range(start.y, stop.y)):
        yield x, y

with open("data.txt", "r") as fin:
    points: List[Tuple[Point, Point]] = []  # store points as tuple of pairs
    for row in fin:
        start, stop = row.strip().split(" -> ")
        points.append((point_from_coords(start), point_from_coords(stop)))

    map = defaultdict(int)
    for start, stop in points:
        # traverse from start to stop
        if start.x == stop.x:
            for i in inclusive_range(start.y, stop.y):
                map[(start.x, i)] += 1
        elif start.y == stop.y:
            for i in inclusive_range(start.x, stop.x):
                map[(i, start.y)] += 1
        else:
            if is_diagonal(start, stop):
                for x, y in diagonal_range(start, stop):
                    map[(x, y)] += 1
            else:
              raise Exception("Shouldn't be in here")

    filtered = list(filter(lambda x: x > 1, map.values()))

    # print(map)
    print(len(filtered))
