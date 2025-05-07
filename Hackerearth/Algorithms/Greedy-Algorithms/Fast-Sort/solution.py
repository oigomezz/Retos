from collections import Counter

t = int(input())
for _ in range(t):
    p = input()
    f = input()
    ans = ''
    counter = Counter(list(f))
    for i in p:
        if i in counter.keys():
            ans += i * counter[i]
    print(ans)
