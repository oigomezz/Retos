import unicodedata


def is_palindrome(text):
    normalized_text = unicodedata.normalize("NFD", text.lower())
    normalized_text = "".join(
        c for c in normalized_text if unicodedata.category(c) != "Mn"
    )
    normalized_text = "".join(e for e in normalized_text if e.isalnum())
    return normalized_text == normalized_text[::-1]


print(is_palindrome("Ana lleva al oso la avellana."))
print(
    is_palindrome(
        "Adivina ya te opina, ya ni miles origina, ya ni cetro me domina, ya ni monarcas, a repaso ni mulato carreta, acaso nicotina, ya ni cita vecino, anima cocina, pedazo gallina, cedazo terso nos retoza de canilla goza, de pánico camina, ónice vaticina, ya ni tocino saca, a terracota luminosa pera, sacra nómina y ánimo de mortecina, ya ni giros elimina, ya ni poeta, ya ni vida"
    )
)
print(is_palindrome("¿Qué os ha parecido el reto?"))
