n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

val = {}
for i in range(n):
    val[A[i]] = max(B[i], val.get(A[i], 0))

for i in range(n):
    print(val[A[i]], end=" ")
