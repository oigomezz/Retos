s, k = map(str, input().split())
k = int(k)
n = len(s)
a = [s[i:n] for i in range(n)]
a.sort()
print(a[k - 1])
