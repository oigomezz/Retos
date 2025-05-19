temp = [int(x) for x in input().split()]
r = temp[0]
c = temp[1]

data = []

for i in range(0, r):
    data.append([int(j) for j in input().split()])
for i in range(r):
    for j in range(len(data[i])):
        if data[i][j] != 0:
            data[i][j] = 1
print(r, c, sep=" ")
for i in range(r):
    for j in range(len(data[i])):
        print(data[i][j], end=" ")
    print()
