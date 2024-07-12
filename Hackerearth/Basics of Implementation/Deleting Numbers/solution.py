n, k = map(int, input().split())
A = [0]+[int(x) for x in input().split()]

N = n-k
Middle = (N+1)//2
End = Middle+k

a = A[Middle:End+1]

print(max(a))
