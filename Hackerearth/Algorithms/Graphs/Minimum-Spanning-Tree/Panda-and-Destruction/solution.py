n, m = map(int, input().strip().split())
destroying = {}
energy = 0
for _ in range(m):
    a, b = map(int, input().split())
    if a not in destroying:
        destroying[a] = None
        energy += 1
print(energy)
