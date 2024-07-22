n = int(input())
arr = list(input().split())

for string in arr:
    x = 0
    for c in string:
        x = x * 10 + (ord(c) - ord('0'))
    assert 1 <= x <= 1e18

cnt = [0] * 10

for string in arr:
    sz = len(string)
    ss = set()
    for j in range(sz):
        ss.add(ord(string[j]) - ord('0'))
    val = 0
    for x in ss:
        val = max(val, cnt[x])
    for x in ss:
        cnt[x] = val + 1

ans = 0
for i in range(10):
    ans = max(ans, cnt[i])

print(ans)
