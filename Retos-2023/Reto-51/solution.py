def karaca(text, is_karaca):
    result = ""

    for word in text.lower().split():
        if is_karaca:
            result += (
                word[:-3]
                .replace("0", "a")
                .replace("1", "e")
                .replace("2", "i")
                .replace("3", "o")
                .replace("4", "u")[::-1]
                + " "
            )
        else:
            result += (
                word[::-1]
                .replace("a", "0")
                .replace("e", "1")
                .replace("i", "2")
                .replace("o", "3")
                .replace("u", "4")
                + "aca "
            )

    return result


print(karaca("placa", False))
print(karaca("0c0lpaca", True))

print(karaca("Este es el penúltimo reto de programación del año", False))
print(
    karaca(
        "1ts1aca s1aca l1aca 3m2tlún1paca 3t1raca 1daca nó2c0m0rg3rpaca l1daca 3ñ0aca",
        True,
    )
)

# El algoritmo no soporta estos casos
print(karaca("1", False))
print(karaca("1aca ", True))
