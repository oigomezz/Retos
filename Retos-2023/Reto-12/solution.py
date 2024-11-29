def find_non_common(str1, str2):
    out = ""
    str1 = str1.lower()
    str2 = str2.lower()

    for char in str1:
        if char not in str2:
            out += char

    return out


def print_non_common(str1, str2):
    out1 = find_non_common(str1, str2)
    out2 = find_non_common(str2, str1)

    print(f"out1: {out1}")
    print(f"out2: {out2}")


def print_non_common_with_filter(str1, str2):
    out1 = "".join(filter(lambda x: x not in str2, str1.lower()))
    out2 = "".join(filter(lambda x: x not in str1, str2.lower()))

    print(f"out1: {out1}")
    print(f"out2: {out2}")


print_non_common("brais", "moure")
print_non_common("Me gusta Java", "Me gusta Kotlin")
print_non_common(
    'Usa el canal de nuestro discord (https://mouredev.com/discord) "Reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad',
    "Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.",
)

print_non_common_with_filter(
    'Usa el canal de nuestro discord (https://mouredev.com/discord) "Reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad',
    "Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.",
)
