def is_anagram(one, two):
    word_one = one.lower()
    word_two = two.lower()
    if word_one == word_two:
        return False
    word_one_to_array = [char for char in word_one]
    word_two_to_array = [char for char in word_two]
    word_one_to_array.sort()
    word_two_to_array.sort()
    return word_one_to_array == word_two_to_array

print(is_anagram("amor", "roma"))