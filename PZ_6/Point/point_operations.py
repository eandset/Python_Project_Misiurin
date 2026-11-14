from input_number import get_float


class Point:
    x: float
    y: float


    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


    def __str__(self):
        return f"({self.x}, {self.y})"


def distance_sqr(a: Point, b: Point) -> float:
    return ((a.x - b.x) ** 2 +
            (a.y - b.y) ** 2)


def get_point(msg: str) -> Point:
    print(msg)

    x = get_float("\tx: ")
    y = get_float("\ty: ")

    return Point(x, y)
