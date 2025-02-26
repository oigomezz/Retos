n, m, g = map(int, input().split())
t = list(map(int, input().split()))
a = list(map(int, input().split()))

mm = max(t[i] - t[i-1] for i in range(1, n))
a.sort()
count = sum(1 for x in a if x <= mm)

print(count)
