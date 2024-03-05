def count_words(text):
    words = {}
    for key in text.lower().replace("[^a-z0-9]", " ").split(" "):
        if key == "":
            continue
        if key in words:
            words[key] += 1
        else:
            words[key] = 1
    for word, count in words.items():
        print(f"{word} se ha repetido {count} {'vez' if count == 1 else 'veces'}")

count_words("Hola, mi nombre es brais. Mi nombre completo es Brais Moure (MoureDev).")
