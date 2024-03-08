def draw_frame(text):
    words = text.split(" ")
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)

    print("*" * (max_length + 4))

    for word in words:
        if word:
            print("* " + word + " " * (max_length - len(word)) + " *")

    print("*" * (max_length + 4))


draw_frame("¿Qué te parece el reto?")
draw_frame("¿Qué te     parece el reto?")
draw_frame("¿Cuántos retos de código de la comunidad has resuelto?")
