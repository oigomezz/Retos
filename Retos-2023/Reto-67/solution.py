def to_octal_and_hex(decimal: int):
    current_decimal = decimal

    # Octal
    _octal = ""
    while current_decimal > 0:
        _octal = str(current_decimal % 8) + _octal
        current_decimal //= 8

    _octal = 0 if _octal == "" else _octal
    print(f"{decimal} en octal es {_octal}")

    current_decimal = decimal

    # Hex
    hex_values = "0123456789ABCDEF"
    _hex = ""
    while current_decimal > 0:
        _hex = hex_values[current_decimal % 16] + _hex
        current_decimal //= 16

    _hex = 0 if _hex == "" else _hex
    print(f"{decimal} en hexadecimal es {_hex}")


to_octal_and_hex(0)
to_octal_and_hex(100)
to_octal_and_hex(1000)
