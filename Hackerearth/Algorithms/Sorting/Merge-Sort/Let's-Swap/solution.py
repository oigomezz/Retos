n = int(input())
p = list(map(int, input().strip().split()))
ans = 0
min_right = n
max_left = -1
for i in range(n):
    left = i + 1
    right = p[i]
    ans += abs(right - i - 1)
    if left > right:
        left, right = right, left
    min_right = min(min_right, right)
    max_left = max(max_left, left)

if max_left > min_right:
    ans += 2 * (max_left - min_right)

print(ans)
