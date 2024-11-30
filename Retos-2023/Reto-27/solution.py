class PolygonType:
    SQUARE = 1
    TRIANGLE = 2


def draw_polygon(size, type):
    if size < 2:
        print("El tamaño debe ser mayor a 1")

    total_size = size

    for value in range(1, total_size + 1):
        if type == PolygonType.SQUARE:
            print("* " * total_size)
        elif type == PolygonType.TRIANGLE:
            print("* " * value)

    print("")


draw_polygon(10, PolygonType.SQUARE)
draw_polygon(15, PolygonType.TRIANGLE)
