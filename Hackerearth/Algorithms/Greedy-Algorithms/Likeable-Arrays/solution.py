from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    counter = Counter(a)
    ans = 0
    for i in counter:
        if i != counter[i]:
            ans += min(counter[i], abs(i - counter[i]))
    print(ans)
