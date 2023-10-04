import cmath


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


def on_segment(p: Point, p1: Point, p2: Point):
    p0 = p1.x - p.x, p1.y - p.y
    p1 = p2.x - p.x, p2.y - p.y

    det = p0[0] * p1[1] - p1[0] * p0[1]
    prod = p0[0] * p1[0] + p0[1] * p1[1]

    return (
        (det == 0 and prod < 0)
        or (p0[0] == 0 and p0[1] == 0)
        or (p1[0] == 0 and p1[1] == 0)
    )


def direction(p1: Point, p2: Point, p3: Point):
    return (p3.y - p1.y) * (p2.x - p1.x) > (p2.y - p1.y) * (p3.x - p1.x)


def on_line(p: Point, q: Point, r: Point):
    return (
        q.x <= max(p.x, r.x)
        and q.x >= min(p.x, r.x)
        and q.y <= max(p.y, r.y)
        and q.y >= min(p.y, r.y)
    )


def is_intersect(p1: Point, p2: Point, p3: Point, p4: Point):
    d0 = direction(p1, p3, p4)
    d1 = direction(p2, p3, p4)
    d2 = direction(p1, p2, p3)
    d3 = direction(p1, p2, p4)
    return d0 != d1 and d2 != d3


def check_intersect(line: Line, polygon: list):
    for i in range(len(polygon)):
        v0, v1 = polygon[i], polygon[(i + 1) % len(polygon)]
        if is_intersect(line.p1, line.p2, v0, v1):
            return True
    return False


def is_in_polygon(p: Point, polygon: list):
    sum_ = complex(0, 0)

    for i in range(len(polygon)):
        v0, v1 = polygon[i], polygon[(i + 1) % len(polygon)]
        if on_segment(p, v0, v1):
            in_polygon, on_border = False, True
            return in_polygon, on_border
        sum_ += cmath.log(
            (complex(v1.x, v1.y) - complex(p.x, p.y))
            / (complex(v0.x, v0.y) - complex(p.x, p.y))
        )

    in_polygon, on_border = abs(sum_) > 1, False
    return in_polygon, on_border


def main(vehicles, polygons):
    for vehicle in vehicles:
        output = "Sea"
        for polygon in polygons:
            if check_intersect(vehicle, polygon):
                output = "Land/Sea"
                break
            else:
                front, front_border = is_in_polygon(vehicle.p1, polygon)
                back, back_border = is_in_polygon(vehicle.p2, polygon)

                if front_border or back_border:
                    output = "Land/Sea"
                    break
                elif front and back:
                    output = "Land"
                    break
        print(output)


if __name__ == "__main__":
    vehicles = []
    polygons = []

    N = int(input())
    for _ in range(N):
        x1, y1, x2, y2 = map(int, input().strip().split())
        vehicle = Line(Point(x1, y1), Point(x2, y2))
        vehicles.append(vehicle)

    M = int(input())
    for _ in range(M):
        P = int(input())
        polygon_points = []
        for _ in range(P):
            x, y = map(int, input().strip().split())
            polygon_points.append(Point(x, y))
        polygons.append(polygon_points)

    main(vehicles, polygons)
