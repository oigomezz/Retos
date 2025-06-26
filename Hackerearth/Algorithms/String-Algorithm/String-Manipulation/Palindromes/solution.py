s = input().strip()
temp = s
if len(set(s)) > 1:
    while s == temp[::-1]:
        temp = temp[:-1]
    print(len(temp))
else:
    print(0)
