from point import Point

class Rectangle(Point):
    def __init__(self, x=0.0, y=0.0, width=1.0, height=1.0):
        super().__init__(x, y)  # Ärver x och y från Point
        if not (isinstance(width, (int, float)) and isinstance(height, (int, float))):
            raise TypeError("Width och height måste vara tal (int eller float)")
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def __repr__(self):
        return f"Rectangle(x={self.x}, y={self.y}, width={self.width}, height={self.height})"
