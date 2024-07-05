T = int(input())
for _ in range(T):
    i, j = map(int, input().split())
    print(i) if (i >= j) and (j >= 0) else print(-1)
