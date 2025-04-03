t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    low = min(a)
    high = max(a)
    if n > 2 and high == a[0] and low == a[-1]:
        print(max(high - min(a[1:-1]), max(a[1:-1]) - low))
    else:
        print(high - low)
