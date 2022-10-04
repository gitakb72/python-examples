import math
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

    def print(self):
        return f"({self.x}, {self.y})"

    def length(self, other: 'Point' = None):
        if other is None:
            other = Point(0, 0)
        x_diff = self.x - other.x
        y_diff = self.y - other.y
        return math.sqrt(x_diff ** 2 + y_diff ** 2)

p1 = Point(5, 0)
p2 = Point(5, 12)

assert p2.length() == 13
assert p2.length(p1) == 12
