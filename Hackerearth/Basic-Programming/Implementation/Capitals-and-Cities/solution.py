N = 300005
id = N
A = [0] * N
P = [0] * N
tot = 0
Mn = float('inf')

n, k = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(1, n + 1):
    A[i] = arr[i - 1]
    P[i] = i

P[1:n + 1] = sorted(P[1:n + 1], key=lambda x: A[x])
for i in range(1, n + 1):
    tot += A[P[i]] - A[P[1]]
for i in range(1, n + 1):
    if tot >= k and Mn > tot - k:
        Mn = tot - k
        id = P[i]
    if tot >= k and Mn >= tot - k:
        Mn = tot - k
        id = min(id, P[i])
    if tot < k and Mn > ((k - tot) & 1):
        Mn = (k - tot) & 1
        id = P[i]
    if tot < k and Mn >= ((k - tot) & 1):
        Mn = (k - tot) & 1
        id = min(id, P[i])
    if i < n:  # Prevent index out of range
        tot += (A[P[i + 1]] - A[P[i]]) * (i + i - n)
print(id, Mn)
