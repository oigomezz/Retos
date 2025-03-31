from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    houses = defaultdict(int)
    total = 0
    for _ in range(n):
        x, y, h = map(int, input().split())
        houses[y - x] += h
        total += h
    avg = total / 2
    i = 0
    for key in sorted(houses.keys()):
        i += houses[key]
        if i >= avg:
            print('YES' if i == avg or total == 2 * i - houses[key] else 'NO')
            break
