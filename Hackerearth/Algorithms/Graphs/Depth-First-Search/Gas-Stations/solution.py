n, x = map(int, input().strip().split())
p = list(map(int, input().strip().split()))
for i, v in enumerate(p):
    if x <= 0:
        print(i)
        break
    else:
        x -= v
