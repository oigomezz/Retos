t = int(input())
while t > 0:
    n = int(input())
    l = list(map(int, input().split()))
    count = 0
    for i in l:
        while (i % 2 != 1):
            count += 1
            i //= 2
    print("Alan" if (count % 2 == 0) else "Charlie")

    t -= 1
