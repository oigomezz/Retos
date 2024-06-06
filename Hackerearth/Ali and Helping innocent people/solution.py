tag = input()
vowel = ("A", "E", "I", "O", "U", "Y")

first = (int(tag[0])+int(tag[1])) % 2 == 0
second = (int(tag[3])+int(tag[4])) % 2 == 0
third = (int(tag[4])+int(tag[5])) % 2 == 0
fourth = (int(tag[7])+int(tag[8])) % 2 == 0

if (tag[2] in vowel):
    print("invalid")
elif (first and second and third and fourth):
    print("valid")
else:
    print("invalid")
