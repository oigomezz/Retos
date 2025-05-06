def op(x): return x * 3 if x > 0 else x * -5


t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    a = sorted(map(int, input().strip().split()))
    print(min(sum(sorted(map(op, (i - j for j in a)))[:k]) for i in a))
