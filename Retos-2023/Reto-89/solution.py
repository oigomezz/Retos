def permutations(word: str) -> list:
    if len(word) <= 1:
        return [word]

    result = []
    for index in range(len(word)):
        current_letter = word[index]
        rest_word = word[:index] + word[index + 1:]
        for permutation in permutations(rest_word):
            result.append(current_letter + permutation)

    return result


word = "solas"
print(f"Permutations of {word}:")
for index, permutation in enumerate(permutations(word)):
    print(f"{index + 1}. {permutation}")
