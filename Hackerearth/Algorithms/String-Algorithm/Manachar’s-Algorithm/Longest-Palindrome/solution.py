import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def ints():
    return list(map(int, input().split()))


p = 10**9+7
inf = 10**20+7
n, k = ints()
a = input().strip()
for i in range(n-k, n):
    print(i+1)

print(*[i+1 for i in range(k)])
