t = int(input())
for _ in range(t):
    a, b = map(int, input().strip().split())
    if b & 1:
        val = b - 1
    else:
        val = b - 2
    print(val if val >= a else a & b)
