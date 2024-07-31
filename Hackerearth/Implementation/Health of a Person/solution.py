T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    health_points = list(map(int, input().split()))
    reduction = [-1] * n
    b = list(map(int, input().split()))
    for i in range(1, m+1):
        for j in range(i-1, n, i):
            if reduction[j] == -1 and health_points[j] <= b[i-1]:
                reduction[j] = i
    for i in range(n):
        print(reduction[i])
