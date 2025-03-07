t = int(input())

for _ in range(t):
    n = int(input())
    a = [0] * n
    for i in range(n):
        x = input()
        if 'a' in x:
            a[i] |= 1
        if 'e' in x:
            a[i] |= 2
        if 'i' in x:
            a[i] |= 4
        if 'o' in x:
            a[i] |= 8
        if 'u' in x:
            a[i] |= 16

    arr = [[0] * 4 for _ in range(32)]
    for i in range(31, -1, -1):
        arr[i] = [0] * 4

    for i in range(len(a), -1, -1):
        for j in range(31, -1, -1):
            for z in range(3, -1, -1):
                if z == 0 and j == 0:
                    arr[j][z] = 0
                elif z == 0:
                    arr[j][z] = 1
                elif i == len(a):
                    arr[j][z] = 0
                else:
                    arr[j][z] = arr[j & a[i]][z - 1] + arr[j][z]

    print(arr[31][3])
