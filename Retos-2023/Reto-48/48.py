import unicodedata


def most_repeated_vowel(text):
    vowel_count = {}

    normalized_text = unicodedata.normalize("NFD", text.lower())

    for character in normalized_text:
        if character in ["a", "e", "i", "o", "u"]:
            vowel_count[character] = vowel_count.get(character, 0) + 1

    most_repeated = []
    max_repeated = 0

    for vowel, count in vowel_count.items():
        if count >= max_repeated:
            if count > max_repeated:
                most_repeated = []
            most_repeated.append(vowel)
            max_repeated = count

    return most_repeated


print(most_repeated_vowel("aaaaaeeeeiiioou"))
print(most_repeated_vowel("AáaaaEeeeIiiOoU"))
print(most_repeated_vowel("eeeeiiioouaaaaa"))
print(most_repeated_vowel(".-Aá?aaaBbEeeweIiiOoU:"))
print(most_repeated_vowel(".-Aá?aaa BbEeew eIiiOoU:"))
print(most_repeated_vowel(".-Aá?aaa BbEeew eEIiiOoU:"))
print(most_repeated_vowel(".-Aá?aaa BbEeew eEIiiOoUuuuuu:"))
print(most_repeated_vowel("aeiou"))
print(most_repeated_vowel("brp qyz"))
