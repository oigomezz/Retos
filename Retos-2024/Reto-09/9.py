def decimal_to_binary(decimal):
    number = decimal
    binary = ""
    while number != 0:
        reminder = number % 2
        number //= 2
        binary = str(reminder) + binary
    return binary if binary else "0"

print(decimal_to_binary(387))
print(decimal_to_binary(0))
