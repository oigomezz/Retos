def is_armstrong(number):
    if number < 0:
        return False
    else:
        sum_value = 0
        pow_value = len(str(number))

        for character in str(number):
            sum_value += int(character) ** pow_value

        return number == sum_value


print(is_armstrong(371))
print(is_armstrong(-371))
print(is_armstrong(372))
print(is_armstrong(0))
