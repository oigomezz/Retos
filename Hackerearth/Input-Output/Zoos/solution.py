word = input().rstrip()
count_z = word.count('z')
count_o = word.count('o')
print("{}".format("Yes" if count_z << 1 == count_o else "No"))
