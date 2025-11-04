class Point:
# point.py
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def translate(self, dx, dy):
        """Flyttar punkten i x- och y-led."""
        if not (isinstance(dx, (int, float)) and isinstance(dy, (int, float))):
            raise TypeError("dx och dy måste vara tal (int eller float)")
        self.x += dx
        self.y += dy