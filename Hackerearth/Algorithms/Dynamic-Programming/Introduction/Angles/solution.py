N, K = map(int, input().strip().split())
raju = list(map(int, input().strip().split()))
angles = set()
for i in raju:
    j = 1
    existed = set()
    while True:
        x = i * j % 360
        if x in existed:
            break
        angles.add(x)
        existed.add(x)
        j += 1
rani = list(map(int, input().strip().split()))
for i in rani:
    print('YES' if i in angles else 'NO')
