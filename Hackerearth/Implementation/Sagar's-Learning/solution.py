t = int(input())
for _ in range(t):
    num = int(input())
    if num <= 2:
        print("-1")
    else:
        j = num//3
        print(j, j*2, j*3)
