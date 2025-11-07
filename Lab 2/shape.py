# shape.py

class Shape:
    def __init__(self, x=0, y=0):
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            raise TypeError("x and y must be numeric values (int or float).")
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        """Move the shape by dx and dy."""
        if not (isinstance(dx, (int, float)) and isinstance(dy, (int, float))):
            raise TypeError("dx and dy must be numeric values (int or float).")
        self.x += dx
        self.y += dy

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"

    def __str__(self):
        return f"{self.__class__.__name__} centered at ({self.x}, {self.y})"
