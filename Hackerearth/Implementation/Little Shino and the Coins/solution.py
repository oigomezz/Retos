k = int(input())
s = input()

count = 0
slength = len(s)

for start in range(slength):
    index = start
    distinct = set()
    distinctlen = 0

    while index < slength:
        if s[index] not in distinct:
            distinct.add(s[index])
            distinctlen += 1

        if distinctlen == k:
            count += 1
        elif distinctlen > k:
            break

        index += 1


print(count)
