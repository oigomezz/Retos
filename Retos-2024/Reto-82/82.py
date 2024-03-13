def infiltrated_characters(first_text: str, second_text: str) -> list:

    characters = []

    if len(first_text) == len(second_text):
        for index in range(0, len(first_text)):
            if first_text[index] != second_text[index]:
                characters.append(second_text[index])
    else:
        print("Las dos cadenas de texto tienen longitud diferentes")

    return characters


print(infiltrated_characters("Me llamo oigomezz", "Me llemo oigomezz"))
print(infiltrated_characters("Me llamo.Oscar Gomez", "Me llamo oscar gomez"))
print(infiltrated_characters("Me llamo.Oscar Gomez", "Me llamo oscar gomez "))
print(infiltrated_characters("", ""))
