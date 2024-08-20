import itertools


def f(p, n):
    special_count = 0
    for i in range(1, n+1):
        special_count += abs(p[i-1] - i)
    return special_count


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    permutatons = list(itertools.permutations(range(1, n+1)))
    ans = "NO"
    for p in permutatons:
        if f(p, n) == k:
            ans = "YES"
            break
    print(ans)
