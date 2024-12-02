def number_of_boomerangs(numbers):
    if len(numbers) < 3:
        return 0

    boomerangs = 0

    for index in range(1, len(numbers) - 1):
        prev = numbers[index - 1]
        current = numbers[index]
        next_num = numbers[index + 1]

        if prev == next_num and prev != current:
            print(f"[{prev}, {current}, {next_num}]")
            boomerangs += 1

    return boomerangs


print(number_of_boomerangs([2, 1, 2, 3, 3, 4, 2, 4]))
print(number_of_boomerangs([2, 1, 2, 1, 2]))
print(number_of_boomerangs([1, 2, 3, 4, 5]))
print(number_of_boomerangs([2, 2, 2, 2, 2]))
print(number_of_boomerangs([2, -2, 2, -2, 2]))
print(number_of_boomerangs([2, -2]))
print(number_of_boomerangs([2]))
print(number_of_boomerangs([]))
