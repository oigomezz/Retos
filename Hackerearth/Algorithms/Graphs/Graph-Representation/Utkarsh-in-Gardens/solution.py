N = int(input())
G = [[0] * N for _ in range(N)]

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        G[i][j] = (line[j] == 1)

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        temp = sum(G[i][k] and G[j][k] for k in range(N))
        ans += temp * (temp - 1) // 2

print(ans // 2)
