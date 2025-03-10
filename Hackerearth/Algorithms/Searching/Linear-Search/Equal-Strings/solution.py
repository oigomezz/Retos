num_probs = int(input())
for _ in range(num_probs):
    n, x = (int(x) for x in input().strip().split())
    s = input().strip()
    t = input().strip()

    s = [int(ch) for ch in s]
    t = [int(ch) for ch in t]

    if s.count(0) % 2 != t.count(0) % 2:
        print(-1)
        continue

    p = []
    for i in range(n):
        if s[i] != t[i]:
            p.append(i)

    r = len(p)
    if r == 0:
        print(0)
        continue

    val = [0 for _ in range(r+1)]
    val[r] = 0
    val[r-1] = x

    for i in range(r-2, -1, -1):
        v0 = x + val[i+1]
        v1 = 2 * (p[i+1] - p[i]) + val[i+2]
        val[i] = min(v0, v1)
    print(val[0] // 2)
