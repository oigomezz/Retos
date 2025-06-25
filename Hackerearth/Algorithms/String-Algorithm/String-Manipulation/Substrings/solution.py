s = input()
counter = []
count = 0
cur = None
for i in range(len(s)):
    if s[i] == cur:
        count += 1
    else:
        if cur is not None:
            counter.append((cur, count))
        cur = s[i]
        count = 1

counter.append((cur, count))
ans = 0
for _, count in counter:
    ans += (count * (count + 1)) // 2
for i in range(1, len(counter) - 1):
    if counter[i - 1][0] == counter[i + 1][0] and counter[i][1] == 1:
        ans += min(counter[i - 1][1], counter[i + 1][1])
print(ans)
