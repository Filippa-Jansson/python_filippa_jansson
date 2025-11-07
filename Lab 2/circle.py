from shape import Shape
import math

class Circle(Shape):
    def __init__(self, x=0, y=0, radius=1):
        super().__init__(x, y)
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be numeric")
        if radius <= 0:
            raise ValueError("radius must be positive")
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    def is_unit_circle(self):
        return self.radius == 1

    def __eq__(self, other):
        return isinstance(other, Circle) and self.radius == other.radius

    def __lt__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("Can only compare Circle with Circle")
        return self.radius < other.radius

    def __le__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("Can only compare Circle with Circle")
        return self.radius <= other.radius

    def __gt__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("Can only compare Circle with Circle")
        return self.radius > other.radius

    def __ge__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("Can only compare Circle with Circle")
        return self.radius >= other.radius

    def __repr__(self):
        return f"Circle(x={self.x}, y={self.y}, radius={self.radius})"

    def __str__(self):
        return f"Circle with center ({self.x}, {self.y}) and radius {self.radius}"
