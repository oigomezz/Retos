k = int(input())
input_strings = [input() for _ in range(k)]
n = int(input())
search_strings = list(map(str, input().split()))
remaining_count = 0

for input_string in input_strings:
    for i in range(n):
        if input_string == search_strings[i]:
            search_strings[i] = ""

for search_string in search_strings:
    if search_string != "":
        remaining_count += 1
        if remaining_count == 1:
            print(search_string[0].upper(), end="")
        else:
            print("." + search_string[0].upper(), end="")
