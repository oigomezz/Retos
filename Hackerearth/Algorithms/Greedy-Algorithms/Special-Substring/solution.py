import random


def cmp(a, b):
    if a == b:
        return False
    return s[a] < s[b]


s = ""
t = 1
while t > 0:
    n, k = map(int, input().split())
    s = input().strip()
    v = []
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            v.append(i)
    for i in range(n - 1):
        if len(v) < k - 1 and s[i] != s[i + 1]:
            v.append(i)
    perm = [0] * k
    random.shuffle(v)
    while len(v) >= k:
        v.pop()
    v.append(n - 1)
    v.sort()
    for i in v:
        print(i + 1)
    v.sort(key=lambda x: cmp(x, x))
    mp = {}
    for i in v:
        mp[i] = 1
    cnt = 0
    for i in mp:
        cnt += 1
        mp[i] = cnt
    random.shuffle(v)
    for i in range(len(v) // 2):
        print(mp[v[i]], mp[v[len(v) - i - 1]], end=" ")
    if len(v) % 2 == 1:
        print(mp[v[len(v) // 2]])
