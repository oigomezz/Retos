from collections import deque

n = int(input())
a = list(map(int, input().split()))
prfx = [0] * n
sfx = [0] * n
ans = float('inf')

sfx[n - 1] = 0
stk = deque()

for i in range(n - 2, -1, -1):
    sfx[i] = sfx[i + 1]
    nxt = a[i + 1]
    cur = a[i]

    while nxt < cur:
        val = (n - 1 if not stk else stk[-1])
        sfx[i] += (val - i) * 2
        if stk:
            stk.pop()
        nxt *= 4

    while nxt >= cur * 4:
        stk.append(i)
        cur *= 4

stk.clear()
prfx[0] = 1

for i in range(1, n):
    prfx[i] = prfx[i - 1] + 1
    cur = a[i]
    prv = a[i - 1]

    while prv < cur:
        val = (0 if not stk else stk[-1])
        prfx[i] += (i - val) * 2
        if stk:
            stk.pop()
        prv *= 4

    while prv >= cur * 4:
        stk.append(i)
        cur *= 4

ans = min(prfx[n - 1], sfx[0])

for i in range(n):
    ans = min(ans, prfx[i] + sfx[i + 1])

print(ans)
