from bisect import bisect_left

n = int(input())
B = [0] * (2 * n)
A = [(0, 0)] * (2 * n)
ans = 0
S = [[float('inf')] * 1000010 for _ in range(2)]

for i in range(n):
    B[i], a = map(int, input().split())
    A[i] = (i, a)

for i in range(n, 2 * n):
    A[i] = (i, B[i - n])
    B[i] = A[i - n][1]

n *= 2

A.sort(key=lambda x: (B[x[0]], -x[1]))

for i in range(n):
    A[i] = (A[i][0] >= n // 2, A[i][1])

for i in range(n):
    pos = bisect_left(S[1 - A[i][0]], A[i][1])
    if pos > 0:
        S[A[i][0]][pos - 1] = min(S[A[i][0]][pos - 1], A[i][1])
    S[A[i][0]][pos] = min(S[A[i][0]][pos], A[i][1])
    ans = max(ans, pos + 1)

print(ans)
