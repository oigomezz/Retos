from collections import defaultdict

T = int(input())
results = []

for _ in range(T):
    n = int(input())
    x = int(input())
    y = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    c = defaultdict(int)
    ans = 0

    for value in a:
        c[(value & x) ^ (value & y)] += 1

    for value in b:
        ans += c[(value & x) ^ (value & y)]

    results.append(ans)

print("\n".join(map(str, results)))
