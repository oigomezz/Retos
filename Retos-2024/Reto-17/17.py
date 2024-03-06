import re


def capitalize(text):
    capitalized_text = text

    for word in re.sub("[^A-zÀ-ú]", " ", text).split(" "):
        capitalized_text = capitalized_text.replace(word, word.capitalize())

    return capitalized_text


print(capitalize("¿hola qué tal estás?"))
print(capitalize("¿hola      qué tal estás?"))
print(capitalize("El niño ñoño"))
