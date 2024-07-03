t = int(input())

for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    k = 1
    for a in range(n-1):
        if (lst[a] > lst[a+1]):
            k += 1

    print(k)
