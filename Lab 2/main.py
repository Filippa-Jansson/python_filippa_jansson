from circle import Circle
from rectangle import Rectangle
from point import Point


def main():
    # Skapa objekt
    c1 = Circle(x=0, y=0, radius=1)
    r1 = Rectangle(x=0, y=0, width=2, height=4)

    # Testa utskrift
    print("Cirkeln:", c1)
    print("Rektangeln:", r1)

    # Testa metoder
    print("Cirkelyta:", c1.area)
    print("Rektangelyta:", r1.area)

    print("Är cirkeln en enhetscirkel?", c1.is_unit_circle())
    print("Är rektangeln en kvadrat?", r1.is_square())

    # Testa förflyttning
    print("\nFlyttar cirkeln...")
    c1.translate(2, 3)
    print("Ny position:", c1)

if __name__ == "__main__":
    main()
