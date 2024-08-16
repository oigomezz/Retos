n = int(input())
buildings = [0] * n
for i in range(n):
    a = int(input())
    buildings[i] = a

q = int(input())
for i in range(q):
    count = 0
    k = int(input())
    for j in range(n):
        if buildings[j] % k == 0:
            count += 1
    print(count)
