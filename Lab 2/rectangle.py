from shape import Shape

class Rectangle(Shape):
    def __init__(self, x=0, y=0, width=1, height=1):
        super().__init__(x, y)
        if not (isinstance(width, (int, float)) and isinstance(height, (int, float))):
            raise TypeError("width and height must be numeric values (int or float).")
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be positive.")
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

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area < other.area
        raise TypeError("Can only compare Rectangle with Rectangle.")

    def __le__(self, other): return self == other or self < other
    def __gt__(self, other): return not self <= other
    def __ge__(self, other): return not self < other

    def __repr__(self):
        return f"Rectangle(x={self.x}, y={self.y}, width={self.width}, height={self.height})"

    def __str__(self):
        return f"Rectangle centered at ({self.x}, {self.y}) with width={self.width} and height={self.height}"