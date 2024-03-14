def reverse(text):
    text_count = len(text) - 1
    reversed_text = ""
    for index in range(text_count + 1):
        reversed_text += text[text_count - index]
    return reversed_text


def recursive_reverse(text, index=0, reversed_text=""):
    text_count = len(text) - 1
    new_reversed_text = reversed_text
    new_reversed_text += text[text_count - index]
    if index < text_count:
        new_index = index + 1
        new_reversed_text = recursive_reverse(text, new_index, new_reversed_text)
    return new_reversed_text


print(reverse("Hola mundo"))
print(recursive_reverse("Hola mundo"))
