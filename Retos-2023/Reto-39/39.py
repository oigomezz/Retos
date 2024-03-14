def binary_to_decimal(binary):
    length = len(binary) - 1
    decimal = None

    for index in range(length + 1):
        digit_char = binary[length - index]
        if digit_char == "0" or digit_char == "1":
            if decimal is None:
                decimal = 0
            decimal += int(digit_char) * 2**index
        else:
            return None

    return decimal


print(binary_to_decimal("00110"))
print(binary_to_decimal("01100"))
print(binary_to_decimal("000000000"))
print(binary_to_decimal("00210"))
print(binary_to_decimal("001101001110"))
print(binary_to_decimal("00b10"))
print(binary_to_decimal(""))
print(binary_to_decimal("-00110"))
print(binary_to_decimal(" "))
print(binary_to_decimal(" 10011"))
print(binary_to_decimal("1O1OO11"))
