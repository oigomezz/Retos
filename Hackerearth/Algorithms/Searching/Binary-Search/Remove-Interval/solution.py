from bisect import bisect_left, bisect_right

n = int(input())
t = []
for _ in range(n):
    a, b = map(int, input().split())
    t.append((a, b))
left = [a for a, b in t]
right = [b for a, b in t]

left.sort()
right.sort()

ans = float("inf")
for a, b in t:
    ind = bisect_left(right, a)
    t = ind
    ind1 = n-bisect_right(left, b)
    ans = min(ans, n-ind-ind1-1)
print(ans)
