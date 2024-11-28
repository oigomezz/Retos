def decoder(input_text):
    decoded_input = ""

    natural_dict = {
        "A": ".—",
        "B": "—...",
        "C": "—.—.",
        "CH": "————",
        "D": "—..",
        "E": ".",
        "F": "..—.",
        "G": "——.",
        "H": "....",
        "I": "..",
        "J": ".———",
        "K": "—.—",
        "L": ".—..",
        "M": "——",
        "N": "—.",
        "Ñ": "——.——",
        "O": "———",
        "P": ".——.",
        "Q": "——.—",
        "R": ".—.",
        "S": "...",
        "T": "—",
        "U": "..—",
        "V": "...—",
        "W": ".——",
        "X": "—..—",
        "Y": "—.——",
        "Z": "——..",
        "0": "—————",
        "1": ".————",
        "2": "..———",
        "3": "...——",
        "4": "....—",
        "5": ".....",
        "6": "—....",
        "7": "——...",
        "8": "———..",
        "9": "————.",
        ".": ".—.—.—",
        ",": "——..——",
        "?": "..——..",
        '"': ".—..—.",
        "/": "—..—.",
    }

    morse_dict = {}
    for key, value in natural_dict.items():
        morse_dict[value] = key

    if any(char.isalnum() for char in input_text):
        # Natural
        index = 0
        is_ch = False

        for character in input_text.upper():
            if not is_ch and character != " ":
                next_index = index + 1
                if (
                    character == "C"
                    and next_index < len(input_text)
                    and input_text.upper()[next_index] == "H"
                ):
                    decoded_input += natural_dict["CH"]
                    is_ch = True
                else:
                    decoded_input += natural_dict.get(character, "")

                decoded_input += " "
            else:
                if not is_ch:
                    decoded_input += " "
                is_ch = False

            index += 1

    elif "." in input_text or "—" in input_text:
        # Morse
        for word in input_text.split("  "):
            for symbols in word.split(" "):
                if symbols:
                    decoded_input += morse_dict.get(symbols, "")
            decoded_input += " "

    return decoded_input


natural_text = "Chocapic. Es una marca de cereales?"
morse_text = decoder(natural_text)
print(morse_text)
print(decoder(morse_text))
