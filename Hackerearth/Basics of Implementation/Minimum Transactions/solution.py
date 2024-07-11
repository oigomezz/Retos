n, m = map(int, input().split())
trans = []
for i in range(n):
    trans.append(0)
for r in range(m):
    taker, giver, amount = map(int, input().split())
    trans[taker - 1] += amount
    trans[giver - 1] -= amount

ans = 0
for i in range(len(trans)):
    if trans[i] > 0:
        ans += trans[i]
print(ans)
