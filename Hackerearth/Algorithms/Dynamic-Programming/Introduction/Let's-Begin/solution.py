t = int(input())
for _ in range(t):
    x = int(input())
    if x == 1:
        print(-1)
    elif x == 2 or x == 3 or x == 5 or x == 7:
        print(1)
    elif x % 7 == 0:
        print(x // 7)
    elif x % 7 == 1 or x % 7 == 2 or x % 7 == 3 or x % 7 == 5:
        print(x // 7 + 1)
    elif x % 7 == 4 or x % 7 == 6:
        print(x // 7 + 2)
