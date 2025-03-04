hsh = [[] for _ in range(1001000)]

n = int(input().strip())
left, right, ans = 0, float('inf'), 0
pw = [1] * 1001000
for i in range(1, 1000001):
    pw[i] = pw[i - 1] * 31

for i in range(1, n + 1):
    str_input = input().strip()
    right = min(right, len(str_input))
    hsh[i].append(0)
    for j in range(len(str_input)):
        hsh[i].append(hsh[i][-1] * 31 + (ord(str_input[j]) - ord('a') + 1))

while left <= right:
    mid = (left + right) // 2
    cur, prev = 0, 1
    s = [set(), set()]
    for i in range(1, n + 1):
        for j in range(mid, len(hsh[i])):
            k = j - mid
            h = hsh[i][j] - (pw[mid] * hsh[i][k])
            if i == 1:
                s[cur].add(h)
            else:
                if h in s[prev]:
                    s[cur].add(h)
        s[prev].clear()
        cur = 1 - cur
        prev = 1 - prev
    if len(s[prev]) > 0:
        left = mid + 1
        ans = mid
    else:
        right = mid - 1

print(ans)
