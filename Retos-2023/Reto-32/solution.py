def find_second_greater(numbers):
    sorted_numbers = []

    for number in numbers:
        found = False

        for index, sorted_number in enumerate(sorted_numbers):
            if number >= sorted_number:
                if number != sorted_number:
                    sorted_numbers.insert(index, number)
                found = True
                break

        if not found:
            sorted_numbers.append(number)

    return sorted_numbers[1] if len(sorted_numbers) >= 2 else None


print(find_second_greater([4, 6, 1, 8, 2]))
print(find_second_greater([4, 6, 8, 8, 6]))
print(find_second_greater([4, 4]))
print(find_second_greater([]))
