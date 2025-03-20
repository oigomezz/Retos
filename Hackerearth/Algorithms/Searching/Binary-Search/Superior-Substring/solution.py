from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    if n <= 3:
        print(n)
    else:
        adj = defaultdict(list)
        for i in range(n):
            adj[ord(s[i]) - 97].append(i)
        v = 3
        for u in adj.values():
            size = len(u)
            if 2 * size + 1 > v:
                for i in range(size):
                    u[i] -= 2 * i
                for i in range(size):
                    j = (v + 2 * i - 3) // 2 + 1
                    while j < size:
                        diff = u[j] - u[i]
                        if diff <= 2:
                            w = 2 * (j - i + 1) + 1
                            v = max(v, w)
                            j += 1
                        else:
                            j += diff - 2
        print(min(v, n))
