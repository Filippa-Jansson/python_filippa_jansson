from point import Point
import math

class Circle(Point):
    def __init__(self, x=0.0, y=0.0, radius=1.0):
        super().__init__(x, y)
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius måste vara ett tal (int eller float)")
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    def is_unit_circle(self):
        return self.radius == 1

    def __repr__(self):
        return f"Circle(x={self.x}, y={self.y}, radius={self.radius})"