def sort(numbers, asc):
    sorted_numbers = []

    for number in numbers:
        added = False

        for index, sorted_number in enumerate(sorted_numbers):
            if (number < sorted_number) if asc else (number > sorted_number):
                sorted_numbers.insert(index, number)
                added = True
                break

        if not added:
            sorted_numbers.append(number)

    return sorted_numbers


print(sort([4, 6, 1, 8, 2], True))  # [1, 2, 4, 6, 8]
print(sort([4, 6, 1, 8, 2], False))  # [8, 6, 4, 2, 1]
