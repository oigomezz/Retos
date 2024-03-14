class Polygon:
    def area(self):
        # This method should be overridden in subclasses.
        pass

    def print_area(self):
        # This method should be overridden in subclasses.
        pass


class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2

    def print_area(self):
        print(f"El área del triángulo es {self.area()}")


class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def print_area(self):
        print(f"El área del rectángulo es {self.area()}")


class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def print_area(self):
        print(f"El área del cuadrado es {self.area()}")


def area(polygon):
    polygon.print_area()
    return polygon.area()


area(Triangle(10.0, 5.0))
area(Rectangle(5.0, 7.0))
area(Square(4.0))
