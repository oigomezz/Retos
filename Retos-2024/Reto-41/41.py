def pascal_triangle(size):
    last_row = []

    for row in range(size):
        current_row = []
        triangle_row = ""

        for element in range(row + 1):
            if 1 <= element < row:
                value = last_row[element - 1] + last_row[element]
                triangle_row += f"{value} "
                current_row.append(value)
            else:
                triangle_row += "1 "
                current_row.append(1)

        print(" " * (size - row) + triangle_row)

        last_row = current_row


pascal_triangle(5)
pascal_triangle(1)
pascal_triangle(0)
pascal_triangle(-5)
